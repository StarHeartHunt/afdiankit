"""DO NOT EDIT THIS FILE!

This file is automatically @generated by afdiankit using the follow command:

    python -m codegen && isort . && black .
"""


from typing import TYPE_CHECKING, Dict, Literal, Optional

from pydantic import BaseModel, TypeAdapter
from afdiankit.utils import UNSET, exclude_unset

from .types import (
    PostRegRequestBody,
    PostLoginRequestBody,
    PostQuickLoginRequestBody,
    PostSendQlCodeRequestBody,
    PostVerifyCodeRequestBody,
    PostResetPasswordRequestBody,
    PostQuickLoginCodeRequestBody,
    PostSendForgetCodeRequestBody,
    PostCheckForgetCodeRequestBody,
)

if TYPE_CHECKING:
    from afdiankit import AfdianCore


class PassportClient:
    def __init__(self, afdian: "AfdianCore"):
        self._afdian = afdian

    def post_verify_code(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/passport/send-verify-code"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostVerifyCodeRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._afdian.request(
            "POST",
            url,
            json=exclude_unset(json),
        )

    async def async_post_verify_code(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/passport/send-verify-code"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostVerifyCodeRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._afdian.arequest(
            "POST",
            url,
            json=exclude_unset(json),
        )

    def post_reg(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/passport/register"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostRegRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._afdian.request(
            "POST",
            url,
            json=exclude_unset(json),
        )

    async def async_post_reg(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/passport/register"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostRegRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._afdian.arequest(
            "POST",
            url,
            json=exclude_unset(json),
        )

    def post_login(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/passport/login"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostLoginRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._afdian.request(
            "POST",
            url,
            json=exclude_unset(json),
        )

    async def async_post_login(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/passport/login"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostLoginRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._afdian.arequest(
            "POST",
            url,
            json=exclude_unset(json),
        )

    def post_quick_login(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/passport/quick-login"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostQuickLoginRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._afdian.request(
            "POST",
            url,
            json=exclude_unset(json),
        )

    async def async_post_quick_login(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/passport/quick-login"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostQuickLoginRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._afdian.arequest(
            "POST",
            url,
            json=exclude_unset(json),
        )

    def post_send_ql_code(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/passport/send-ql-code"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostSendQlCodeRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._afdian.request(
            "POST",
            url,
            json=exclude_unset(json),
        )

    async def async_post_send_ql_code(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/passport/send-ql-code"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostSendQlCodeRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._afdian.arequest(
            "POST",
            url,
            json=exclude_unset(json),
        )

    def post_quick_login_code(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/passport/send-quick-login-code"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostQuickLoginCodeRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._afdian.request(
            "POST",
            url,
            json=exclude_unset(json),
        )

    async def async_post_quick_login_code(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/passport/send-quick-login-code"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostQuickLoginCodeRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._afdian.arequest(
            "POST",
            url,
            json=exclude_unset(json),
        )

    def post_send_forget_code(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/passport/send-forget-code"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostSendForgetCodeRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._afdian.request(
            "POST",
            url,
            json=exclude_unset(json),
        )

    async def async_post_send_forget_code(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/passport/send-forget-code"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostSendForgetCodeRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._afdian.arequest(
            "POST",
            url,
            json=exclude_unset(json),
        )

    def post_check_forget_code(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/passport/check-forget-code"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostCheckForgetCodeRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._afdian.request(
            "POST",
            url,
            json=exclude_unset(json),
        )

    async def async_post_check_forget_code(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/passport/check-forget-code"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostCheckForgetCodeRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._afdian.arequest(
            "POST",
            url,
            json=exclude_unset(json),
        )

    def post_reset_password(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/passport/reset-password"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostResetPasswordRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._afdian.request(
            "POST",
            url,
            json=exclude_unset(json),
        )

    async def async_post_reset_password(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/passport/reset-password"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostResetPasswordRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._afdian.arequest(
            "POST",
            url,
            json=exclude_unset(json),
        )
