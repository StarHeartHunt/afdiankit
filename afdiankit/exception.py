from typing import TYPE_CHECKING

import httpx

if TYPE_CHECKING:
    from .response import Response


class AfdianException(Exception):
    ...


class AuthCredentialError(AfdianException):
    """Auth Credential Error"""


class AuthExpiredError(AfdianException):
    """Auth Expired Error"""


class RequestError(AfdianException):
    """Simple API request failed with unknown error"""


class RequestTimeout(AfdianException):
    """Simple API request timeout"""

    def __init__(self, request: httpx.Request):
        self.request = request

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(method={self.request.method}, "
            f"url={self.request.url})"
        )


class RequestFailed(AfdianException):
    """Simple API request failed with error status code"""

    def __init__(self, response: "Response"):
        self.request = response.raw_request
        self.response = response

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(method={self.request.method}, "
            f"url={self.request.url}, status_code={self.response.status_code})"
        )


class WebhookTypeNotFound(AfdianException):
    """Webhook event type not found"""

    def __init__(self, name: str):
        self.name = name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name})"
