"""DO NOT EDIT THIS FILE!

This file is automatically @generated by afdiankit using the follow command:

    python -m codegen && isort . && black .
"""


from typing import TYPE_CHECKING, Dict, Optional

if TYPE_CHECKING:
    from afdiankit import AfdianCore


class CategoryClient:
    def __init__(self, afdian: "AfdianCore"):
        self._afdian = afdian

    def get_category_list(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/category/list"

        return self._afdian.request(
            "GET",
            url,
        )

    async def async_get_category_list(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/category/list"

        return await self._afdian.arequest(
            "GET",
            url,
        )

    def get_category_edit_list(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/category/edit-list"

        return self._afdian.request(
            "GET",
            url,
        )

    async def async_get_category_edit_list(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/category/edit-list"

        return await self._afdian.arequest(
            "GET",
            url,
        )
