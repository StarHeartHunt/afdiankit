"""DO NOT EDIT THIS FILE!

This file is automatically @generated by afdiankit using the follow command:

    python -m codegen && isort . && black .
"""

from typing import TYPE_CHECKING, Dict, Literal, Optional

from pydantic import BaseModel, TypeAdapter

from afdiankit.utils import UNSET, exclude_unset

from .types import PostUploadGetUrlRequestBody, PostUploadGetSignRequestBody

if TYPE_CHECKING:
    from afdiankit import AfdianCore


class UploadClient:
    def __init__(self, afdian: "AfdianCore"):
        self._afdian = afdian

    def get_upload_snapshot(
        self,
        snapshot_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/upload/snapshot"

        params = {
            "snapshot_id": snapshot_id,
        }

        return self._afdian.request(
            "GET",
            url,
            params=exclude_unset(params),
        )

    async def async_get_upload_snapshot(
        self,
        snapshot_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/upload/snapshot"

        params = {
            "snapshot_id": snapshot_id,
        }

        return await self._afdian.arequest(
            "GET",
            url,
            params=exclude_unset(params),
        )

    def post_upload_get_sign(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/upload/get-sign"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostUploadGetSignRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._afdian.request(
            "POST",
            url,
            json=exclude_unset(json),
        )

    async def async_post_upload_get_sign(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/upload/get-sign"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostUploadGetSignRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._afdian.arequest(
            "POST",
            url,
            json=exclude_unset(json),
        )

    def post_upload_get_url(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/upload/get-url"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostUploadGetUrlRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._afdian.request(
            "POST",
            url,
            json=exclude_unset(json),
        )

    async def async_post_upload_get_url(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/upload/get-url"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostUploadGetUrlRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._afdian.arequest(
            "POST",
            url,
            json=exclude_unset(json),
        )

    def get_upload_get_obj_sign(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/upload/get-obj-sign"

        return self._afdian.request(
            "GET",
            url,
        )

    async def async_get_upload_get_obj_sign(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/upload/get-obj-sign"

        return await self._afdian.arequest(
            "GET",
            url,
        )

    def get_upload_get_message_sign(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/upload/get-message-sign"

        return self._afdian.request(
            "GET",
            url,
        )

    async def async_get_upload_get_message_sign(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/upload/get-message-sign"

        return await self._afdian.arequest(
            "GET",
            url,
        )
