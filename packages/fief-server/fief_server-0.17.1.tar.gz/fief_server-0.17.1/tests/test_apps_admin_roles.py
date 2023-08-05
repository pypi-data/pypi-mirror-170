import uuid
from typing import Any, Dict
from unittest.mock import MagicMock

import httpx
import pytest
from fastapi import status

from fief.db import AsyncSession
from fief.errors import APIErrorCode
from fief.models import Workspace
from fief.repositories import UserPermissionRepository
from fief.tasks import on_role_updated
from tests.data import TestData, data_mapping


@pytest.mark.asyncio
@pytest.mark.workspace_host
class TestListRoles:
    async def test_unauthorized(self, test_client_admin: httpx.AsyncClient):
        response = await test_client_admin.get("/roles/")

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @pytest.mark.parametrize(
        "params,nb_results",
        [
            ({}, len(data_mapping["roles"])),
            ({"query": "manager"}, 1),
        ],
    )
    @pytest.mark.authenticated_admin
    async def test_valid(
        self,
        params: Dict[str, Any],
        nb_results: int,
        test_client_admin: httpx.AsyncClient,
        test_data: TestData,
    ):
        response = await test_client_admin.get("/roles/", params=params)

        assert response.status_code == status.HTTP_200_OK

        json = response.json()
        assert json["count"] == nb_results

        for result in json["results"]:
            assert "permissions" in result
            for permission in result["permissions"]:
                assert "id" in permission
                assert "name" in permission
                assert "codename" in permission


@pytest.mark.asyncio
@pytest.mark.workspace_host
class TestCreateRole:
    async def test_unauthorized(self, test_client_admin: httpx.AsyncClient):
        response = await test_client_admin.post("/roles/", json={})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @pytest.mark.authenticated_admin
    async def test_not_existing_permission(
        self, test_client_admin: httpx.AsyncClient, not_existing_uuid: uuid.UUID
    ):
        response = await test_client_admin.post(
            "/roles/",
            json={
                "name": "New role",
                "granted_by_default": False,
                "permissions": [str(not_existing_uuid)],
            },
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST

        json = response.json()
        assert json["detail"] == APIErrorCode.ROLE_CREATE_NOT_EXISTING_PERMISSION

    @pytest.mark.authenticated_admin
    async def test_valid(
        self, test_client_admin: httpx.AsyncClient, test_data: TestData
    ):
        response = await test_client_admin.post(
            "/roles/",
            json={
                "name": "New role",
                "granted_by_default": False,
                "permissions": [
                    str(test_data["permissions"]["castles:read"].id),
                    str(test_data["permissions"]["castles:create"].id),
                ],
            },
        )

        assert response.status_code == status.HTTP_201_CREATED

        json = response.json()
        assert json["name"] == "New role"
        assert json["granted_by_default"] is False

        permissions = json["permissions"]
        assert len(permissions) == 2
        permission_ids = [permission["id"] for permission in permissions]
        assert str(test_data["permissions"]["castles:read"].id) in permission_ids
        assert str(test_data["permissions"]["castles:create"].id) in permission_ids


@pytest.mark.asyncio
@pytest.mark.workspace_host
class TestUpdateRole:
    async def test_unauthorized(
        self, test_client_admin: httpx.AsyncClient, test_data: TestData
    ):
        role = test_data["roles"]["castles_visitor"]
        response = await test_client_admin.patch(f"/roles/{role.id}", json={})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @pytest.mark.authenticated_admin
    async def test_not_existing(
        self, test_client_admin: httpx.AsyncClient, not_existing_uuid: uuid.UUID
    ):
        response = await test_client_admin.patch(f"/roles/{not_existing_uuid}", json={})

        assert response.status_code == status.HTTP_404_NOT_FOUND

    @pytest.mark.authenticated_admin
    async def test_not_existing_permission(
        self,
        test_client_admin: httpx.AsyncClient,
        test_data: TestData,
        not_existing_uuid: uuid.UUID,
    ):
        role = test_data["roles"]["castles_visitor"]
        response = await test_client_admin.patch(
            f"/roles/{role.id}",
            json={
                "permissions": [str(not_existing_uuid)],
            },
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST

        json = response.json()
        assert json["detail"] == APIErrorCode.ROLE_UPDATE_NOT_EXISTING_PERMISSION

    @pytest.mark.authenticated_admin
    async def test_valid(
        self,
        test_client_admin: httpx.AsyncClient,
        test_data: TestData,
        workspace: Workspace,
        send_task_mock: MagicMock,
    ):
        role = test_data["roles"]["castles_visitor"]
        response = await test_client_admin.patch(
            f"/roles/{role.id}",
            json={
                "name": "Updated name",
                "permissions": [
                    str(test_data["permissions"]["castles:create"].id),
                    str(test_data["permissions"]["castles:update"].id),
                ],
            },
        )

        assert response.status_code == status.HTTP_200_OK

        json = response.json()
        assert json["name"] == "Updated name"

        permissions = json["permissions"]
        assert len(permissions) == 2
        permission_ids = [permission["id"] for permission in permissions]
        assert str(test_data["permissions"]["castles:create"].id) in permission_ids
        assert str(test_data["permissions"]["castles:update"].id) in permission_ids

        send_task_mock.assert_called_once()
        assert send_task_mock.call_args[0][0] == on_role_updated
        assert send_task_mock.call_args[0][1] == str(role.id)
        assert set(send_task_mock.call_args[0][2]) == {
            str(test_data["permissions"]["castles:create"].id),
            str(test_data["permissions"]["castles:update"].id),
        }
        assert set(send_task_mock.call_args[0][3]) == {
            str(test_data["permissions"]["castles:read"].id)
        }
        assert send_task_mock.call_args[0][4] == str(workspace.id)


@pytest.mark.asyncio
@pytest.mark.workspace_host
class TestDeleteRole:
    async def test_unauthorized(
        self, test_client_admin: httpx.AsyncClient, test_data: TestData
    ):
        role = test_data["roles"]["castles_visitor"]
        response = await test_client_admin.delete(f"/roles/{role.id}")

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @pytest.mark.authenticated_admin
    async def test_not_existing(
        self, test_client_admin: httpx.AsyncClient, not_existing_uuid: uuid.UUID
    ):
        response = await test_client_admin.delete(f"/roles/{not_existing_uuid}")

        assert response.status_code == status.HTTP_404_NOT_FOUND

    @pytest.mark.authenticated_admin
    async def test_valid(
        self,
        test_client_admin: httpx.AsyncClient,
        test_data: TestData,
        workspace_session: AsyncSession,
    ):
        role = test_data["roles"]["castles_visitor"]
        response = await test_client_admin.delete(f"/roles/{role.id}")

        assert response.status_code == status.HTTP_204_NO_CONTENT

        user = test_data["users"]["regular"]
        user_permission_repository = UserPermissionRepository(workspace_session)
        user_permissions = await user_permission_repository.list(
            user_permission_repository.get_by_user_statement(user.id)
        )
        assert len(user_permissions) == 1
