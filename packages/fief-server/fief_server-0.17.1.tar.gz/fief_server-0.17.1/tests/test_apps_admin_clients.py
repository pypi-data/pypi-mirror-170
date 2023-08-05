import uuid
from typing import List

import httpx
import pytest
from fastapi import status
from jwcrypto import jwk

from fief.db import AsyncSession
from fief.errors import APIErrorCode
from fief.repositories import ClientRepository
from tests.data import TestData


@pytest.mark.asyncio
@pytest.mark.workspace_host
class TestListClients:
    async def test_unauthorized(self, test_client_admin: httpx.AsyncClient):
        response = await test_client_admin.get("/clients/")

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @pytest.mark.authenticated_admin
    async def test_valid(
        self, test_client_admin: httpx.AsyncClient, test_data: TestData
    ):
        response = await test_client_admin.get("/clients/")

        assert response.status_code == status.HTTP_200_OK

        json = response.json()
        assert json["count"] == len(test_data["clients"])

        for result in json["results"]:
            assert "tenant" in result
            assert result["encrypt_jwk"] in [None, "**********"]


@pytest.mark.asyncio
@pytest.mark.workspace_host
class TestCreateClient:
    async def test_unauthorized(self, test_client_admin: httpx.AsyncClient):
        response = await test_client_admin.post("/clients/", json={})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @pytest.mark.authenticated_admin
    async def test_empty_redirect_uris(
        self, test_client_admin: httpx.AsyncClient, test_data: TestData
    ):
        tenant = test_data["tenants"]["default"]
        response = await test_client_admin.post(
            "/clients/",
            json={
                "name": "New client",
                "first_party": True,
                "client_type": "confidential",
                "redirect_uris": [],
                "tenant_id": str(tenant.id),
            },
        )

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

        json = response.json()
        assert json["detail"][0]["loc"] == ["body", "redirect_uris"]

    @pytest.mark.authenticated_admin
    async def test_redirect_uris_not_https(
        self, test_client_admin: httpx.AsyncClient, test_data: TestData
    ):
        tenant = test_data["tenants"]["default"]
        response = await test_client_admin.post(
            "/clients/",
            json={
                "name": "New client",
                "first_party": True,
                "client_type": "confidential",
                "redirect_uris": ["http://nantes.city/callback"],
                "tenant_id": str(tenant.id),
            },
        )

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

        json = response.json()
        assert json["detail"][0]["loc"] == ["body", "redirect_uris", 0]
        assert (
            json["detail"][0]["msg"]
            == APIErrorCode.CLIENT_HTTPS_REQUIRED_ON_REDIRECT_URIS
        )

    @pytest.mark.authenticated_admin
    async def test_unknown_tenant(
        self, test_client_admin: httpx.AsyncClient, not_existing_uuid: uuid.UUID
    ):
        response = await test_client_admin.post(
            "/clients/",
            json={
                "name": "New client",
                "first_party": True,
                "client_type": "confidential",
                "redirect_uris": ["https://nantes.city/callback"],
                "tenant_id": str(not_existing_uuid),
            },
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST

        json = response.json()
        assert json["detail"] == APIErrorCode.CLIENT_CREATE_UNKNOWN_TENANT

    @pytest.mark.authenticated_admin
    @pytest.mark.parametrize(
        "redirect_uris",
        [
            ["https://nantes.city/callback"],
            ["http://localhost:8000/callback"],
            ["http://test.localhost:8000/callback"],
            ["http://127.0.0.1:8000/callback"],
        ],
    )
    async def test_valid(
        self,
        redirect_uris: List[str],
        test_client_admin: httpx.AsyncClient,
        test_data: TestData,
    ):
        tenant = test_data["tenants"]["default"]
        response = await test_client_admin.post(
            "/clients/",
            json={
                "name": "New client",
                "first_party": True,
                "client_type": "confidential",
                "redirect_uris": redirect_uris,
                "tenant_id": str(tenant.id),
            },
        )

        assert response.status_code == status.HTTP_201_CREATED

        json = response.json()
        assert json["name"] == "New client"
        assert json["first_party"] is True
        assert json["redirect_uris"] == redirect_uris
        assert json["client_id"] is not None
        assert json["client_secret"] is not None
        assert json["tenant_id"] == str(tenant.id)


@pytest.mark.asyncio
@pytest.mark.workspace_host
class TestUpdateClient:
    async def test_unauthorized(
        self, test_client_admin: httpx.AsyncClient, test_data: TestData
    ):
        client = test_data["clients"]["default_tenant"]
        response = await test_client_admin.patch(f"/clients/{client.id}", json={})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @pytest.mark.authenticated_admin
    async def test_not_existing(
        self, test_client_admin: httpx.AsyncClient, not_existing_uuid: uuid.UUID
    ):
        response = await test_client_admin.patch(
            f"/clients/{not_existing_uuid}", json={}
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND

    @pytest.mark.authenticated_admin
    async def test_redirect_uris_not_https(
        self, test_client_admin: httpx.AsyncClient, test_data: TestData
    ):
        client = test_data["clients"]["default_tenant"]
        response = await test_client_admin.patch(
            f"/clients/{client.id}",
            json={"redirect_uris": ["http://nantes.city/callback"]},
        )

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

        json = response.json()
        assert json["detail"][0]["loc"] == ["body", "redirect_uris", 0]
        assert (
            json["detail"][0]["msg"]
            == APIErrorCode.CLIENT_HTTPS_REQUIRED_ON_REDIRECT_URIS
        )

    @pytest.mark.authenticated_admin
    async def test_cant_update_tenant(
        self, test_client_admin: httpx.AsyncClient, test_data: TestData
    ):
        client = test_data["clients"]["default_tenant"]
        response = await test_client_admin.patch(
            f"/clients/{client.id}",
            json={"tenant_id": str(test_data["tenants"]["secondary"])},
        )

        assert response.status_code == status.HTTP_200_OK

        json = response.json()
        assert json["tenant_id"] == str(client.tenant_id)

    @pytest.mark.authenticated_admin
    async def test_valid(
        self, test_client_admin: httpx.AsyncClient, test_data: TestData
    ):
        client = test_data["clients"]["default_tenant"]
        response = await test_client_admin.patch(
            f"/clients/{client.id}",
            json={"name": "Updated name"},
        )

        assert response.status_code == status.HTTP_200_OK

        json = response.json()
        assert json["name"] == "Updated name"


@pytest.mark.asyncio
@pytest.mark.workspace_host
class TestCreateEncryptionKey:
    async def test_unauthorized(
        self, test_client_admin: httpx.AsyncClient, test_data: TestData
    ):
        client = test_data["clients"]["default_tenant"]
        response = await test_client_admin.post(f"/clients/{client.id}/encryption-key")

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @pytest.mark.authenticated_admin
    async def test_success(
        self,
        test_client_admin: httpx.AsyncClient,
        test_data: TestData,
        workspace_session: AsyncSession,
    ):
        client = test_data["clients"]["default_tenant"]
        response = await test_client_admin.post(f"/clients/{client.id}/encryption-key")

        assert response.status_code == status.HTTP_201_CREATED

        key = jwk.JWK.from_json(response.text)

        assert key.has_private == True
        assert key.has_public == True

        repository = ClientRepository(workspace_session)
        updated_client = await repository.get_by_id(client.id)
        assert updated_client is not None
        assert updated_client.encrypt_jwk is not None

        tenant_key = jwk.JWK.from_json(updated_client.encrypt_jwk)
        assert tenant_key.has_private == False
        assert tenant_key.has_public == True
