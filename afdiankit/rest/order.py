"""DO NOT EDIT THIS FILE!

This file is automatically @generated by afdiankit using the follow command:

    python -m codegen && isort . && black .
"""

from typing import TYPE_CHECKING, Dict, Literal, Optional

from pydantic import BaseModel, TypeAdapter

from afdiankit.utils import UNSET, exclude_unset

from .types import (
    GetOrderCancelRequestBody,
    GetOrderPrepareRequestBody,
    PostCreateOrderRequestBody,
    PostOrderUpdateAddressRequestBody,
    PostOrderUpdateExpressRequestBody,
    PostOrderUpdateCreatorRemarkRequestBody,
)

if TYPE_CHECKING:
    from afdiankit import AfdianCore


class OrderClient:
    def __init__(self, afdian: "AfdianCore"):
        self._afdian = afdian

    def get_order_prepare(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/order/prepare"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(GetOrderPrepareRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._afdian.request(
            "POST",
            url,
            json=exclude_unset(json),
        )

    async def async_get_order_prepare(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/order/prepare"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(GetOrderPrepareRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._afdian.arequest(
            "POST",
            url,
            json=exclude_unset(json),
        )

    def post_create_order(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/order/create-order"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostCreateOrderRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._afdian.request(
            "POST",
            url,
            json=exclude_unset(json),
        )

    async def async_post_create_order(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/order/create-order"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostCreateOrderRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._afdian.arequest(
            "POST",
            url,
            json=exclude_unset(json),
        )

    def post_order_check(
        self,
        out_trade_no: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/order/check"

        params = {
            "out_trade_no": out_trade_no,
        }

        return self._afdian.request(
            "GET",
            url,
            params=exclude_unset(params),
        )

    async def async_post_order_check(
        self,
        out_trade_no: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/order/check"

        params = {
            "out_trade_no": out_trade_no,
        }

        return await self._afdian.arequest(
            "GET",
            url,
            params=exclude_unset(params),
        )

    def get_order_sign(
        self,
        out_trade_no: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/order/sign"

        params = {
            "out_trade_no": out_trade_no,
        }

        return self._afdian.request(
            "GET",
            url,
            params=exclude_unset(params),
        )

    async def async_get_order_sign(
        self,
        out_trade_no: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/order/sign"

        params = {
            "out_trade_no": out_trade_no,
        }

        return await self._afdian.arequest(
            "GET",
            url,
            params=exclude_unset(params),
        )

    def get_order_cancel(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/order/cancel-order"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(GetOrderCancelRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._afdian.request(
            "POST",
            url,
            json=exclude_unset(json),
        )

    async def async_get_order_cancel(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/order/cancel-order"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(GetOrderCancelRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._afdian.arequest(
            "POST",
            url,
            json=exclude_unset(json),
        )

    def get_order_wxjsurl(
        self,
        url: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/order/wxjsurl"

        params = {
            "url": url,
        }

        return self._afdian.request(
            "GET",
            url,
            params=exclude_unset(params),
        )

    async def async_get_order_wxjsurl(
        self,
        url: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/order/wxjsurl"

        params = {
            "url": url,
        }

        return await self._afdian.arequest(
            "GET",
            url,
            params=exclude_unset(params),
        )

    def get_order_express_company_list(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/order/express-company-list"

        return self._afdian.request(
            "GET",
            url,
        )

    async def async_get_order_express_company_list(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/order/express-company-list"

        return await self._afdian.arequest(
            "GET",
            url,
        )

    def post_order_update_express(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/order/update-express"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostOrderUpdateExpressRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._afdian.request(
            "POST",
            url,
            json=exclude_unset(json),
        )

    async def async_post_order_update_express(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/order/update-express"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostOrderUpdateExpressRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._afdian.arequest(
            "POST",
            url,
            json=exclude_unset(json),
        )

    def post_order_update_address(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/order/update-address"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostOrderUpdateAddressRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._afdian.request(
            "POST",
            url,
            json=exclude_unset(json),
        )

    async def async_post_order_update_address(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/order/update-address"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostOrderUpdateAddressRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._afdian.arequest(
            "POST",
            url,
            json=exclude_unset(json),
        )

    def get_order_query_express_progress(
        self,
        number: str,
        mobile: str,
        out_trade_no: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/order/query-express-progress"

        params = {
            "number": number,
            "mobile": mobile,
            "out_trade_no": out_trade_no,
        }

        return self._afdian.request(
            "GET",
            url,
            params=exclude_unset(params),
        )

    async def async_get_order_query_express_progress(
        self,
        number: str,
        mobile: str,
        out_trade_no: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/order/query-express-progress"

        params = {
            "number": number,
            "mobile": mobile,
            "out_trade_no": out_trade_no,
        }

        return await self._afdian.arequest(
            "GET",
            url,
            params=exclude_unset(params),
        )

    def post_order_update_creator_remark(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/order/update-creator-remark"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostOrderUpdateCreatorRemarkRequestBody).validate_python(
            json
        )
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._afdian.request(
            "POST",
            url,
            json=exclude_unset(json),
        )

    async def async_post_order_update_creator_remark(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/order/update-creator-remark"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostOrderUpdateCreatorRemarkRequestBody).validate_python(
            json
        )
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._afdian.arequest(
            "POST",
            url,
            json=exclude_unset(json),
        )

    def get_order_tickets(
        self,
        out_trade_no: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/order/tickets"

        params = {
            "out_trade_no": out_trade_no,
        }

        return self._afdian.request(
            "GET",
            url,
            params=exclude_unset(params),
        )

    async def async_get_order_tickets(
        self,
        out_trade_no: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/order/tickets"

        params = {
            "out_trade_no": out_trade_no,
        }

        return await self._afdian.arequest(
            "GET",
            url,
            params=exclude_unset(params),
        )

    def get_order_ticket_checkin(
        self,
        out_trade_no: str,
        id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/order/ticket-checkin"

        params = {
            "out_trade_no": out_trade_no,
            "id": id,
        }

        return self._afdian.request(
            "GET",
            url,
            params=exclude_unset(params),
        )

    async def async_get_order_ticket_checkin(
        self,
        out_trade_no: str,
        id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/order/ticket-checkin"

        params = {
            "out_trade_no": out_trade_no,
            "id": id,
        }

        return await self._afdian.arequest(
            "GET",
            url,
            params=exclude_unset(params),
        )

    def get_order_transfer_pay_url(
        self,
        out_trade_no: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/order/transfer-pay-url"

        params = {
            "out_trade_no": out_trade_no,
        }

        return self._afdian.request(
            "GET",
            url,
            params=exclude_unset(params),
        )

    async def async_get_order_transfer_pay_url(
        self,
        out_trade_no: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/order/transfer-pay-url"

        params = {
            "out_trade_no": out_trade_no,
        }

        return await self._afdian.arequest(
            "GET",
            url,
            params=exclude_unset(params),
        )
