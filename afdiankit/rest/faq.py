"""DO NOT EDIT THIS FILE!

This file is automatically @generated by afdiankit using the follow command:

    python -m codegen && isort . && black .
"""

from typing import TYPE_CHECKING, Dict, Literal, Optional

from pydantic import BaseModel, TypeAdapter

from afdiankit.utils import UNSET, exclude_unset

from .types import PostApiFaqAskRequestBody, PostApiFaqAnswerRequestBody

if TYPE_CHECKING:
    from afdiankit import AfdianCore


class FaqClient:
    def __init__(self, afdian: "AfdianCore"):
        self._afdian = afdian

    def get_api_faq_list_faq(
        self,
        user_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/faq/list-faq"

        params = {
            "user_id": user_id,
        }

        return self._afdian.request(
            "GET",
            url,
            params=exclude_unset(params),
        )

    async def async_get_api_faq_list_faq(
        self,
        user_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/faq/list-faq"

        params = {
            "user_id": user_id,
        }

        return await self._afdian.arequest(
            "GET",
            url,
            params=exclude_unset(params),
        )

    def post_api_faq_ask(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/faq/ask"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostApiFaqAskRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._afdian.request(
            "POST",
            url,
            json=exclude_unset(json),
        )

    async def async_post_api_faq_ask(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/faq/ask"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostApiFaqAskRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._afdian.arequest(
            "POST",
            url,
            json=exclude_unset(json),
        )

    def post_api_faq_answer(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/faq/answer"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostApiFaqAnswerRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._afdian.request(
            "POST",
            url,
            json=exclude_unset(json),
        )

    async def async_post_api_faq_answer(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/faq/answer"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostApiFaqAnswerRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._afdian.arequest(
            "POST",
            url,
            json=exclude_unset(json),
        )
