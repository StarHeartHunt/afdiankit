from functools import cached_property
from typing_extensions import ParamSpec
from typing import (
    TYPE_CHECKING,
    List,
    Union,
    TypeVar,
    Callable,
    Optional,
    Awaitable,
    overload,
)

from .core import AfdianCore
from .response import Response
from .rest import RestNamespace
from .auth import BaseAuthStrategy

if TYPE_CHECKING:
    import httpx

    from .config import Config
    from .auth import TokenAuthStrategy, UnauthAuthStrategy


A = TypeVar("A", bound=BaseAuthStrategy)
A_o = TypeVar("A_o", bound=BaseAuthStrategy)

CP = ParamSpec("CP")
CT = TypeVar("CT")
RT = TypeVar("RT")

R = Union[
    Callable[CP, Response[RT]],
    Callable[CP, Awaitable[Response[RT]]],
]


class Afdian(AfdianCore[A]):
    if TYPE_CHECKING:
        # none auth with config
        @overload
        def __init__(
            self: "Afdian[UnauthAuthStrategy]",
            auth: None = None,
            *,
            config: Config,
        ):
            ...

        # token auth with config
        @overload
        def __init__(
            self: "Afdian[TokenAuthStrategy]",
            auth: str,
            *,
            config: Config,
        ):
            ...

        # other auth strategies with config
        @overload
        def __init__(
            self: "Afdian[A]",
            auth: A,
            *,
            config: Config,
        ):
            ...

        # none auth without config
        @overload
        def __init__(
            self: "Afdian[UnauthAuthStrategy]",
            auth: None = None,
            *,
            base_url: Optional[Union[str, httpx.URL]] = None,
            accept_format: Optional[str] = None,
            previews: Optional[List[str]] = None,
            user_agent: Optional[str] = None,
            follow_redirects: bool = True,
            timeout: Optional[Union[float, httpx.Timeout]] = None,
        ):
            ...

        # token auth without config
        @overload
        def __init__(
            self: "Afdian[TokenAuthStrategy]",
            auth: str,
            *,
            base_url: Optional[Union[str, httpx.URL]] = None,
            accept_format: Optional[str] = None,
            previews: Optional[List[str]] = None,
            user_agent: Optional[str] = None,
            follow_redirects: bool = True,
            timeout: Optional[Union[float, httpx.Timeout]] = None,
        ):
            ...

        # other auth strategies without config
        @overload
        def __init__(
            self: "Afdian[A]",
            auth: A,
            *,
            base_url: Optional[Union[str, httpx.URL]] = None,
            accept_format: Optional[str] = None,
            previews: Optional[List[str]] = None,
            user_agent: Optional[str] = None,
            follow_redirects: bool = True,
            timeout: Optional[Union[float, httpx.Timeout]] = None,
        ):
            ...

        def __init__(self, *args, **kwargs):
            ...

    # copy afdian instance with other auth
    def with_auth(self, auth: A_o) -> "Afdian[A_o]":
        return Afdian(auth=auth, config=self.config.copy())

    # rest api
    @cached_property
    def rest(self) -> RestNamespace:
        return RestNamespace(self)
