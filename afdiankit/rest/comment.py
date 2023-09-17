"""DO NOT EDIT THIS FILE!

This file is automatically @generated by afdiankit using the follow command:

    python -m codegen && isort . && black .
"""


from typing import TYPE_CHECKING, Dict, Literal, Optional, overload

from pydantic import BaseModel, TypeAdapter
from afdiankit.utils import UNSET, Missing, exclude_unset

from .types import (
    PostCommentLikeRequestBody,
    PostCommentDeleteRequestBody,
    PostCommentUnlikeRequestBody,
    PostCommentPublishRequestBody,
)

if TYPE_CHECKING:
    from afdiankit import AfdianCore
    from afdiankit.response import Response


class CommentClient:
    def __init__(self, afdian: "AfdianCore"):
        self._afdian = afdian

    def post_comment_like(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/comment/like"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostCommentLikeRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._afdian.request(
            "POST",
            url,
            json=exclude_unset(json),
        )

    async def async_post_comment_like(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/comment/like"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostCommentLikeRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._afdian.arequest(
            "POST",
            url,
            json=exclude_unset(json),
        )

    def post_comment_unlike(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/comment/unlike"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostCommentUnlikeRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._afdian.request(
            "POST",
            url,
            json=exclude_unset(json),
        )

    async def async_post_comment_unlike(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/comment/unlike"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostCommentUnlikeRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._afdian.arequest(
            "POST",
            url,
            json=exclude_unset(json),
        )

    def get_comment_get_list(
        self,
        post_id: str,
        publish_sn: str,
        type: str,
        hot: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/comment/get-list"

        params = {
            "post_id": post_id,
            "publish_sn": publish_sn,
            "type": type,
            "hot": hot,
        }

        return self._afdian.request(
            "GET",
            url,
            params=exclude_unset(params),
        )

    async def async_get_comment_get_list(
        self,
        post_id: str,
        publish_sn: str,
        type: str,
        hot: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/comment/get-list"

        params = {
            "post_id": post_id,
            "publish_sn": publish_sn,
            "type": type,
            "hot": hot,
        }

        return await self._afdian.arequest(
            "GET",
            url,
            params=exclude_unset(params),
        )

    def post_comment_publish(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/comment/publish"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostCommentPublishRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._afdian.request(
            "POST",
            url,
            json=exclude_unset(json),
        )

    async def async_post_comment_publish(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/comment/publish"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostCommentPublishRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._afdian.arequest(
            "POST",
            url,
            json=exclude_unset(json),
        )

    def post_comment_delete(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/comment/delete"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostCommentDeleteRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._afdian.request(
            "POST",
            url,
            json=exclude_unset(json),
        )

    async def async_post_comment_delete(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/comment/delete"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostCommentDeleteRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._afdian.arequest(
            "POST",
            url,
            json=exclude_unset(json),
        )
