"""DO NOT EDIT THIS FILE!

This file is automatically @generated by afdiankit using the follow command:

    python -m codegen && isort . && black .
"""

from typing import TYPE_CHECKING
from functools import cached_property

from .types import *
from .my import MyClient
from .faq import FaqClient
from .log import LogClient
from .bang import BangClient
from .init import InitClient
from .post import PostClient
from .user import UserClient
from .badge import BadgeClient
from .oauth import OauthClient
from .order import OrderClient
from .oauth2 import Oauth2Client
from .paypal import PaypalClient
from .upload import UploadClient
from .account import AccountClient
from .comment import CommentClient
from .creator import CreatorClient
from .message import MessageClient
from .welcome import WelcomeClient
from .category import CategoryClient
from .passport import PassportClient
from .suiyinzi import SuiyinziClient

if TYPE_CHECKING:
    from afdiankit import AfdianCore


class RestNamespace:
    def __init__(self, afdian: "AfdianCore"):
        self._afdian = afdian

    @cached_property
    def init(self) -> InitClient:
        return InitClient(self._afdian)

    @cached_property
    def log(self) -> LogClient:
        return LogClient(self._afdian)

    @cached_property
    def passport(self) -> PassportClient:
        return PassportClient(self._afdian)

    @cached_property
    def my(self) -> MyClient:
        return MyClient(self._afdian)

    @cached_property
    def category(self) -> CategoryClient:
        return CategoryClient(self._afdian)

    @cached_property
    def creator(self) -> CreatorClient:
        return CreatorClient(self._afdian)

    @cached_property
    def user(self) -> UserClient:
        return UserClient(self._afdian)

    @cached_property
    def order(self) -> OrderClient:
        return OrderClient(self._afdian)

    @cached_property
    def paypal(self) -> PaypalClient:
        return PaypalClient(self._afdian)

    @cached_property
    def message(self) -> MessageClient:
        return MessageClient(self._afdian)

    @cached_property
    def post(self) -> PostClient:
        return PostClient(self._afdian)

    @cached_property
    def comment(self) -> CommentClient:
        return CommentClient(self._afdian)

    @cached_property
    def account(self) -> AccountClient:
        return AccountClient(self._afdian)

    @cached_property
    def oauth(self) -> OauthClient:
        return OauthClient(self._afdian)

    @cached_property
    def upload(self) -> UploadClient:
        return UploadClient(self._afdian)

    @cached_property
    def welcome(self) -> WelcomeClient:
        return WelcomeClient(self._afdian)

    @cached_property
    def faq(self) -> FaqClient:
        return FaqClient(self._afdian)

    @cached_property
    def bang(self) -> BangClient:
        return BangClient(self._afdian)

    @cached_property
    def suiyinzi(self) -> SuiyinziClient:
        return SuiyinziClient(self._afdian)

    @cached_property
    def badge(self) -> BadgeClient:
        return BadgeClient(self._afdian)

    @cached_property
    def oauth2(self) -> Oauth2Client:
        return Oauth2Client(self._afdian)
