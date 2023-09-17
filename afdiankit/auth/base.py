import abc
from typing import TYPE_CHECKING

import httpx

if TYPE_CHECKING:
    from afdiankit import AfdianCore


class BaseAuthStrategy(abc.ABC):
    @abc.abstractmethod
    def get_auth_flow(self, afdian: "AfdianCore") -> httpx.Auth:
        raise NotImplementedError
