"""DO NOT EDIT THIS FILE!

This file is automatically @generated by afdiankit using the follow command:

    python -m codegen && isort . && black .
"""


from typing import TYPE_CHECKING, Dict, Literal, Optional, overload

if TYPE_CHECKING:
    from afdiankit import AfdianCore
    from afdiankit.response import Response


class InitClient:
    def __init__(self, afdian: "AfdianCore"):
        self._afdian = afdian

    def get_init_config(
        self,
    ):
        url = "/api/init/config"

        return self._afdian.request(
            "GET",
            url,
        )

    async def async_get_init_config(
        self,
    ):
        url = "/api/init/config"

        return await self._afdian.arequest(
            "GET",
            url,
        )
