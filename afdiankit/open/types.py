import json
from typing import Any, Dict
from typing_extensions import TypedDict, NotRequired

from pydantic import Field, BaseModel, ConfigDict, computed_field, field_serializer

from .utils import sign


class OpenAPIRequestBody(BaseModel):
    model_config = ConfigDict(extra="allow")

    token: str = Field(exclude=True)
    user_id: str
    params: Dict[str, Any] = {}
    ts: int

    @field_serializer("params")
    def serialize_params(self, params: Dict[str, Any]):
        return json.dumps(params, ensure_ascii=False, separators=(",", ":"))

    @computed_field
    @property
    def sign(self) -> str:
        return sign(
            self.token,
            json.dumps(self.params, ensure_ascii=False, separators=(",", ":")),
            self.ts,
            self.user_id,
        )


class PostPingRequestBody(OpenAPIRequestBody):
    ...


class PostQueryOrderRequestParams(TypedDict):
    page: int
    out_trade_no: NotRequired[str]
    per_page: NotRequired[int]


class PostQueryOrderRequestBody(OpenAPIRequestBody):
    params: PostQueryOrderRequestParams


class PostQuerySponsorRequestParams(TypedDict):
    page: int
    per_page: NotRequired[int]
    user_id: NotRequired[str]


class PostQuerySponsorRequestBody(OpenAPIRequestBody):
    params: PostQuerySponsorRequestParams


class Ping(BaseModel):
    model_config = ConfigDict(extra="allow")


class QueryOrder(BaseModel):
    model_config = ConfigDict(extra="allow")


class QuerySponsor(BaseModel):
    model_config = ConfigDict(extra="allow")
