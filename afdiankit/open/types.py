import json
from typing import Any, Dict, List, Optional
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


class PostPingRequestBody(OpenAPIRequestBody): ...


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


class Request(BaseModel):
    model_config = ConfigDict(extra="allow")

    user_id: str
    params: str
    ts: int
    sign: str


class BaseResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    ec: int
    em: str
    data: Dict[str, Any]


class Pong(BaseModel):
    model_config = ConfigDict(extra="allow")

    page: Optional[int]
    request: Request
    uid: str


class PongResponse(BaseResponse):
    data: Pong


class SkuDetail(BaseModel):
    model_config = ConfigDict(extra="allow")

    sku_id: str
    count: int
    name: str
    album_id: str
    pic: str


class Order(BaseModel):
    model_config = ConfigDict(extra="allow")

    out_trade_no: str
    user_id: str
    plan_id: str
    month: int
    total_amount: str
    show_amount: str
    status: int
    remark: str
    redeem_id: str
    product_type: int
    discount: str
    sku_detail: List[SkuDetail]
    create_time: int
    plan_title: str
    user_private_id: str
    address_person: str
    address_phone: str
    address_address: str


class QueryOrder(BaseModel):
    model_config = ConfigDict(extra="allow")

    list: List[Order]
    total_count: int
    total_page: int
    request: Request


class QueryOrderResponse(BaseResponse):
    data: QueryOrder


class User(BaseModel):
    model_config = ConfigDict(extra="allow")

    user_id: str
    name: str
    avatar: str
    user_private_id: str


class Timing(BaseModel):
    model_config = ConfigDict(extra="allow")

    timing_on: int
    timing_off: int


class SponsorPlan(BaseModel):
    model_config = ConfigDict(extra="allow")

    can_ali_agreement: Optional[int] = None
    plan_id: str
    rank: Optional[int] = None
    user_id: Optional[str] = None
    status: Optional[int] = None
    name: str
    pic: Optional[str] = None
    desc: Optional[str] = None
    price: str
    update_time: Optional[int] = None
    timing: Optional[Timing] = None
    pay_month: Optional[int] = None
    show_price: Optional[str] = None
    show_price_after_adjust: Optional[str] = None
    has_coupon: Optional[int] = None
    coupon: Optional[List] = None
    favorable_price: Optional[int] = None
    independent: Optional[int] = None
    permanent: Optional[int] = None
    can_buy_hide: Optional[int] = None
    need_address: Optional[int] = None
    product_type: Optional[int] = None
    sale_limit_count: Optional[int] = None
    need_invite_code: Optional[bool] = None
    bundle_stock: Optional[int] = None
    bundle_sku_select_count: Optional[int] = None
    config: Optional[Dict[str, Any]] = None
    has_plan_config: Optional[int] = None
    expire_time: int
    sku_processed: List
    rankType: int


class CurrentPlan(BaseModel):
    model_config = ConfigDict(extra="allow")

    can_ali_agreement: Optional[int] = None
    plan_id: Optional[str] = None
    rank: Optional[int] = None
    user_id: Optional[str] = None
    status: Optional[int] = None
    name: str
    pic: Optional[str] = None
    desc: Optional[str] = None
    price: Optional[str] = None
    update_time: Optional[int] = None
    timing: Optional[Timing] = None
    pay_month: Optional[int] = None
    show_price: Optional[str] = None
    show_price_after_adjust: Optional[str] = None
    has_coupon: Optional[int] = None
    coupon: Optional[List] = None
    favorable_price: Optional[int] = None
    independent: Optional[int] = None
    permanent: Optional[int] = None
    can_buy_hide: Optional[int] = None
    need_address: Optional[int] = None
    product_type: Optional[int] = None
    sale_limit_count: Optional[int] = None
    need_invite_code: Optional[bool] = None
    bundle_stock: Optional[int] = None
    bundle_sku_select_count: Optional[int] = None
    config: Optional[Dict[str, Any]] = None
    has_plan_config: Optional[int] = None
    expire_time: Optional[int] = None
    sku_processed: Optional[List] = None
    rankType: Optional[int] = None


class Sponsor(BaseModel):
    model_config = ConfigDict(extra="allow")

    sponsor_plans: List[SponsorPlan]
    current_plan: CurrentPlan
    all_sum_amount: str
    first_pay_time: int
    last_pay_time: int
    user: User


class QuerySponsor(BaseModel):
    model_config = ConfigDict(extra="allow")

    list: List[Sponsor]
    total_count: int
    total_page: int
    request: Request


class QuerySponsorResponse(BaseResponse):
    data: QuerySponsor
