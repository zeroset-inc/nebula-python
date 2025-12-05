# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nebula import Nebula, AsyncNebula
from tests.utils import assert_matches_type
from nebula.types import (
    TokenResponse,
    NebulaResultsUser,
    UserFetchLimitsResponse,
    NebulaResultsGenericBooleanResponse,
)
from nebula.types.collections import PaginatedNebulaResultListUser, NebulaResultsGenericMessageResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Nebula) -> None:
        user = client.users.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(NebulaResultsUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Nebula) -> None:
        response = client.users.with_raw_response.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(NebulaResultsUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Nebula) -> None:
        with client.users.with_streaming_response.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(NebulaResultsUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.users.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Nebula) -> None:
        user = client.users.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Nebula) -> None:
        user = client.users.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            bio="bio",
            email="dev@stainless.com",
            is_superuser=True,
            limits_overrides={"foo": "bar"},
            metadata={"foo": "string"},
            name="name",
            profile_picture="profile_picture",
        )
        assert_matches_type(NebulaResultsUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Nebula) -> None:
        response = client.users.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(NebulaResultsUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Nebula) -> None:
        with client.users.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(NebulaResultsUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.users.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Nebula) -> None:
        user = client.users.list()
        assert_matches_type(PaginatedNebulaResultListUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Nebula) -> None:
        user = client.users.list(
            ids=["string"],
            limit=1,
            offset=0,
        )
        assert_matches_type(PaginatedNebulaResultListUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Nebula) -> None:
        response = client.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(PaginatedNebulaResultListUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Nebula) -> None:
        with client.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(PaginatedNebulaResultListUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Nebula) -> None:
        user = client.users.delete(
            id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(NebulaResultsGenericBooleanResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Nebula) -> None:
        user = client.users.delete(
            id="550e8400-e29b-41d4-a716-446655440000",
            delete_vector_data=True,
            password="password",
        )
        assert_matches_type(NebulaResultsGenericBooleanResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Nebula) -> None:
        response = client.users.with_raw_response.delete(
            id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(NebulaResultsGenericBooleanResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Nebula) -> None:
        with client.users.with_streaming_response.delete(
            id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(NebulaResultsGenericBooleanResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.users.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_change_password(self, client: Nebula) -> None:
        user = client.users.change_password(
            current_password="current_password",
            new_password="new_password",
        )
        assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_change_password(self, client: Nebula) -> None:
        response = client.users.with_raw_response.change_password(
            current_password="current_password",
            new_password="new_password",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_change_password(self, client: Nebula) -> None:
        with client.users.with_streaming_response.change_password(
            current_password="current_password",
            new_password="new_password",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_export(self, client: Nebula) -> None:
        user = client.users.export()
        assert_matches_type(object, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_export_with_all_params(self, client: Nebula) -> None:
        user = client.users.export(
            columns=["string"],
            filters={"foo": "bar"},
            include_header=True,
        )
        assert_matches_type(object, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_export(self, client: Nebula) -> None:
        response = client.users.with_raw_response.export()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(object, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_export(self, client: Nebula) -> None:
        with client.users.with_streaming_response.export() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(object, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_fetch_limits(self, client: Nebula) -> None:
        user = client.users.fetch_limits(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UserFetchLimitsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_fetch_limits(self, client: Nebula) -> None:
        response = client.users.with_raw_response.fetch_limits(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserFetchLimitsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_fetch_limits(self, client: Nebula) -> None:
        with client.users.with_streaming_response.fetch_limits(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserFetchLimitsResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_fetch_limits(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.users.with_raw_response.fetch_limits(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_current_user(self, client: Nebula) -> None:
        user = client.users.get_current_user()
        assert_matches_type(NebulaResultsUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_current_user(self, client: Nebula) -> None:
        response = client.users.with_raw_response.get_current_user()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(NebulaResultsUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_current_user(self, client: Nebula) -> None:
        with client.users.with_streaming_response.get_current_user() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(NebulaResultsUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_login(self, client: Nebula) -> None:
        user = client.users.login(
            password="password",
            username="username",
        )
        assert_matches_type(TokenResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_login_with_all_params(self, client: Nebula) -> None:
        user = client.users.login(
            password="password",
            username="username",
            client_id="client_id",
            client_secret="client_secret",
            grant_type="password",
            scope="scope",
        )
        assert_matches_type(TokenResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_login(self, client: Nebula) -> None:
        response = client.users.with_raw_response.login(
            password="password",
            username="username",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(TokenResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_login(self, client: Nebula) -> None:
        with client.users.with_streaming_response.login(
            password="password",
            username="username",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(TokenResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_logout(self, client: Nebula) -> None:
        user = client.users.logout()
        assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_logout(self, client: Nebula) -> None:
        response = client.users.with_raw_response.logout()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_logout(self, client: Nebula) -> None:
        with client.users.with_streaming_response.logout() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_refresh_token(self, client: Nebula) -> None:
        user = client.users.refresh_token(
            body="body",
        )
        assert_matches_type(TokenResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_refresh_token(self, client: Nebula) -> None:
        response = client.users.with_raw_response.refresh_token(
            body="body",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(TokenResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_refresh_token(self, client: Nebula) -> None:
        with client.users.with_streaming_response.refresh_token(
            body="body",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(TokenResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_register(self, client: Nebula) -> None:
        user = client.users.register(
            email="dev@stainless.com",
            password="password",
        )
        assert_matches_type(NebulaResultsUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_register_with_all_params(self, client: Nebula) -> None:
        user = client.users.register(
            email="dev@stainless.com",
            password="password",
            bio="bio",
            is_verified=True,
            name="name",
            profile_picture="profile_picture",
        )
        assert_matches_type(NebulaResultsUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_register(self, client: Nebula) -> None:
        response = client.users.with_raw_response.register(
            email="dev@stainless.com",
            password="password",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(NebulaResultsUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_register(self, client: Nebula) -> None:
        with client.users.with_streaming_response.register(
            email="dev@stainless.com",
            password="password",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(NebulaResultsUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_request_password_reset(self, client: Nebula) -> None:
        user = client.users.request_password_reset(
            body="dev@stainless.com",
        )
        assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_request_password_reset(self, client: Nebula) -> None:
        response = client.users.with_raw_response.request_password_reset(
            body="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_request_password_reset(self, client: Nebula) -> None:
        with client.users.with_streaming_response.request_password_reset(
            body="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reset_password(self, client: Nebula) -> None:
        user = client.users.reset_password(
            new_password="new_password",
            reset_token="reset_token",
        )
        assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_reset_password(self, client: Nebula) -> None:
        response = client.users.with_raw_response.reset_password(
            new_password="new_password",
            reset_token="reset_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_reset_password(self, client: Nebula) -> None:
        with client.users.with_streaming_response.reset_password(
            new_password="new_password",
            reset_token="reset_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_metrics(self, client: Nebula) -> None:
        user = client.users.retrieve_metrics()
        assert_matches_type(object, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_metrics_with_all_params(self, client: Nebula) -> None:
        user = client.users.retrieve_metrics(
            days=0,
        )
        assert_matches_type(object, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_metrics(self, client: Nebula) -> None:
        response = client.users.with_raw_response.retrieve_metrics()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(object, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_metrics(self, client: Nebula) -> None:
        with client.users.with_streaming_response.retrieve_metrics() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(object, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_verification_email(self, client: Nebula) -> None:
        user = client.users.send_verification_email(
            body="dev@stainless.com",
        )
        assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send_verification_email(self, client: Nebula) -> None:
        response = client.users.with_raw_response.send_verification_email(
            body="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send_verification_email(self, client: Nebula) -> None:
        with client.users.with_streaming_response.send_verification_email(
            body="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_verify_email(self, client: Nebula) -> None:
        user = client.users.verify_email(
            email="dev@stainless.com",
            verification_code="verification_code",
        )
        assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_verify_email(self, client: Nebula) -> None:
        response = client.users.with_raw_response.verify_email(
            email="dev@stainless.com",
            verification_code="verification_code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_verify_email(self, client: Nebula) -> None:
        with client.users.with_streaming_response.verify_email(
            email="dev@stainless.com",
            verification_code="verification_code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncNebula) -> None:
        user = await async_client.users.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(NebulaResultsUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncNebula) -> None:
        response = await async_client.users.with_raw_response.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(NebulaResultsUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncNebula) -> None:
        async with async_client.users.with_streaming_response.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(NebulaResultsUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.users.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncNebula) -> None:
        user = await async_client.users.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncNebula) -> None:
        user = await async_client.users.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            bio="bio",
            email="dev@stainless.com",
            is_superuser=True,
            limits_overrides={"foo": "bar"},
            metadata={"foo": "string"},
            name="name",
            profile_picture="profile_picture",
        )
        assert_matches_type(NebulaResultsUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncNebula) -> None:
        response = await async_client.users.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(NebulaResultsUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncNebula) -> None:
        async with async_client.users.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(NebulaResultsUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.users.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncNebula) -> None:
        user = await async_client.users.list()
        assert_matches_type(PaginatedNebulaResultListUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncNebula) -> None:
        user = await async_client.users.list(
            ids=["string"],
            limit=1,
            offset=0,
        )
        assert_matches_type(PaginatedNebulaResultListUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncNebula) -> None:
        response = await async_client.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(PaginatedNebulaResultListUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncNebula) -> None:
        async with async_client.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(PaginatedNebulaResultListUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncNebula) -> None:
        user = await async_client.users.delete(
            id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(NebulaResultsGenericBooleanResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncNebula) -> None:
        user = await async_client.users.delete(
            id="550e8400-e29b-41d4-a716-446655440000",
            delete_vector_data=True,
            password="password",
        )
        assert_matches_type(NebulaResultsGenericBooleanResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncNebula) -> None:
        response = await async_client.users.with_raw_response.delete(
            id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(NebulaResultsGenericBooleanResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncNebula) -> None:
        async with async_client.users.with_streaming_response.delete(
            id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(NebulaResultsGenericBooleanResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.users.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_change_password(self, async_client: AsyncNebula) -> None:
        user = await async_client.users.change_password(
            current_password="current_password",
            new_password="new_password",
        )
        assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_change_password(self, async_client: AsyncNebula) -> None:
        response = await async_client.users.with_raw_response.change_password(
            current_password="current_password",
            new_password="new_password",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_change_password(self, async_client: AsyncNebula) -> None:
        async with async_client.users.with_streaming_response.change_password(
            current_password="current_password",
            new_password="new_password",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_export(self, async_client: AsyncNebula) -> None:
        user = await async_client.users.export()
        assert_matches_type(object, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_export_with_all_params(self, async_client: AsyncNebula) -> None:
        user = await async_client.users.export(
            columns=["string"],
            filters={"foo": "bar"},
            include_header=True,
        )
        assert_matches_type(object, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_export(self, async_client: AsyncNebula) -> None:
        response = await async_client.users.with_raw_response.export()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(object, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_export(self, async_client: AsyncNebula) -> None:
        async with async_client.users.with_streaming_response.export() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(object, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_fetch_limits(self, async_client: AsyncNebula) -> None:
        user = await async_client.users.fetch_limits(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UserFetchLimitsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_fetch_limits(self, async_client: AsyncNebula) -> None:
        response = await async_client.users.with_raw_response.fetch_limits(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserFetchLimitsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_fetch_limits(self, async_client: AsyncNebula) -> None:
        async with async_client.users.with_streaming_response.fetch_limits(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserFetchLimitsResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_fetch_limits(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.users.with_raw_response.fetch_limits(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_current_user(self, async_client: AsyncNebula) -> None:
        user = await async_client.users.get_current_user()
        assert_matches_type(NebulaResultsUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_current_user(self, async_client: AsyncNebula) -> None:
        response = await async_client.users.with_raw_response.get_current_user()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(NebulaResultsUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_current_user(self, async_client: AsyncNebula) -> None:
        async with async_client.users.with_streaming_response.get_current_user() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(NebulaResultsUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_login(self, async_client: AsyncNebula) -> None:
        user = await async_client.users.login(
            password="password",
            username="username",
        )
        assert_matches_type(TokenResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_login_with_all_params(self, async_client: AsyncNebula) -> None:
        user = await async_client.users.login(
            password="password",
            username="username",
            client_id="client_id",
            client_secret="client_secret",
            grant_type="password",
            scope="scope",
        )
        assert_matches_type(TokenResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_login(self, async_client: AsyncNebula) -> None:
        response = await async_client.users.with_raw_response.login(
            password="password",
            username="username",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(TokenResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_login(self, async_client: AsyncNebula) -> None:
        async with async_client.users.with_streaming_response.login(
            password="password",
            username="username",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(TokenResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_logout(self, async_client: AsyncNebula) -> None:
        user = await async_client.users.logout()
        assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_logout(self, async_client: AsyncNebula) -> None:
        response = await async_client.users.with_raw_response.logout()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_logout(self, async_client: AsyncNebula) -> None:
        async with async_client.users.with_streaming_response.logout() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_refresh_token(self, async_client: AsyncNebula) -> None:
        user = await async_client.users.refresh_token(
            body="body",
        )
        assert_matches_type(TokenResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_refresh_token(self, async_client: AsyncNebula) -> None:
        response = await async_client.users.with_raw_response.refresh_token(
            body="body",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(TokenResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_refresh_token(self, async_client: AsyncNebula) -> None:
        async with async_client.users.with_streaming_response.refresh_token(
            body="body",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(TokenResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_register(self, async_client: AsyncNebula) -> None:
        user = await async_client.users.register(
            email="dev@stainless.com",
            password="password",
        )
        assert_matches_type(NebulaResultsUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_register_with_all_params(self, async_client: AsyncNebula) -> None:
        user = await async_client.users.register(
            email="dev@stainless.com",
            password="password",
            bio="bio",
            is_verified=True,
            name="name",
            profile_picture="profile_picture",
        )
        assert_matches_type(NebulaResultsUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_register(self, async_client: AsyncNebula) -> None:
        response = await async_client.users.with_raw_response.register(
            email="dev@stainless.com",
            password="password",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(NebulaResultsUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_register(self, async_client: AsyncNebula) -> None:
        async with async_client.users.with_streaming_response.register(
            email="dev@stainless.com",
            password="password",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(NebulaResultsUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_request_password_reset(self, async_client: AsyncNebula) -> None:
        user = await async_client.users.request_password_reset(
            body="dev@stainless.com",
        )
        assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_request_password_reset(self, async_client: AsyncNebula) -> None:
        response = await async_client.users.with_raw_response.request_password_reset(
            body="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_request_password_reset(self, async_client: AsyncNebula) -> None:
        async with async_client.users.with_streaming_response.request_password_reset(
            body="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reset_password(self, async_client: AsyncNebula) -> None:
        user = await async_client.users.reset_password(
            new_password="new_password",
            reset_token="reset_token",
        )
        assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_reset_password(self, async_client: AsyncNebula) -> None:
        response = await async_client.users.with_raw_response.reset_password(
            new_password="new_password",
            reset_token="reset_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_reset_password(self, async_client: AsyncNebula) -> None:
        async with async_client.users.with_streaming_response.reset_password(
            new_password="new_password",
            reset_token="reset_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_metrics(self, async_client: AsyncNebula) -> None:
        user = await async_client.users.retrieve_metrics()
        assert_matches_type(object, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_metrics_with_all_params(self, async_client: AsyncNebula) -> None:
        user = await async_client.users.retrieve_metrics(
            days=0,
        )
        assert_matches_type(object, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_metrics(self, async_client: AsyncNebula) -> None:
        response = await async_client.users.with_raw_response.retrieve_metrics()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(object, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_metrics(self, async_client: AsyncNebula) -> None:
        async with async_client.users.with_streaming_response.retrieve_metrics() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(object, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_verification_email(self, async_client: AsyncNebula) -> None:
        user = await async_client.users.send_verification_email(
            body="dev@stainless.com",
        )
        assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send_verification_email(self, async_client: AsyncNebula) -> None:
        response = await async_client.users.with_raw_response.send_verification_email(
            body="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send_verification_email(self, async_client: AsyncNebula) -> None:
        async with async_client.users.with_streaming_response.send_verification_email(
            body="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_verify_email(self, async_client: AsyncNebula) -> None:
        user = await async_client.users.verify_email(
            email="dev@stainless.com",
            verification_code="verification_code",
        )
        assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_verify_email(self, async_client: AsyncNebula) -> None:
        response = await async_client.users.with_raw_response.verify_email(
            email="dev@stainless.com",
            verification_code="verification_code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_verify_email(self, async_client: AsyncNebula) -> None:
        async with async_client.users.with_streaming_response.verify_email(
            email="dev@stainless.com",
            verification_code="verification_code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(NebulaResultsGenericMessageResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True
