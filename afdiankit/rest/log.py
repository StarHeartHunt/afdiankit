"""DO NOT EDIT THIS FILE!

This file is automatically @generated by afdiankit using the follow command:

    python -m codegen && isort . && black .
"""

from typing import TYPE_CHECKING, Dict, Literal, Optional

from pydantic import BaseModel, TypeAdapter

from afdiankit.utils import UNSET, exclude_unset

from .types import PostLogCollectRequestBody

if TYPE_CHECKING:
    from afdiankit import AfdianCore


class LogClient:
    def __init__(self, afdian: "AfdianCore"):
        self._afdian = afdian

    def post_log_collect(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/log/collect"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostLogCollectRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._afdian.request(
            "POST",
            url,
            json=exclude_unset(json),
        )

    async def async_post_log_collect(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/log/collect"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostLogCollectRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._afdian.arequest(
            "POST",
            url,
            json=exclude_unset(json),
        )
