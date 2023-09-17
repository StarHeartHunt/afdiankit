from dataclasses import dataclass
from typing import TYPE_CHECKING, Generator

import httpx

from .base import BaseAuthStrategy

if TYPE_CHECKING:
    from afdiankit import AfdianCore


@dataclass
class TokenAuth(httpx.Auth):
    token: str

    def __init__(self, token: str):
        self.token = token

    def auth_flow(
        self, request: httpx.Request
    ) -> Generator[httpx.Request, httpx.Response, None]:
        httpx.Cookies({"auth_token": self.token}).set_cookie_header(request)
        yield request


@dataclass
class TokenAuthStrategy(BaseAuthStrategy):
    token: str

    def get_auth_flow(self, afdian: "AfdianCore") -> httpx.Auth:
        return TokenAuth(self.token)
