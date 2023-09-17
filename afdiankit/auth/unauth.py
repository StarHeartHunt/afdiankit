from typing import TYPE_CHECKING

import httpx

from .base import BaseAuthStrategy

if TYPE_CHECKING:
    from afdiankit import AfdianCore


class UnauthAuthStrategy(BaseAuthStrategy):
    """Unauthenticated AfdianKit"""

    def get_auth_flow(self, afdian: "AfdianCore") -> httpx.Auth:
        return httpx.Auth()
