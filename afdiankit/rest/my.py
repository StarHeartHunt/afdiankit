"""DO NOT EDIT THIS FILE!

This file is automatically @generated by afdiankit using the follow command:

    python -m codegen && isort . && black .
"""


from typing import TYPE_CHECKING, Dict, Literal, Optional

from pydantic import BaseModel, TypeAdapter
from afdiankit.utils import UNSET, exclude_unset

from .types import (
    PostMyEditBasicRequestBody,
    PostSetShowBadgeRequestBody,
    PostMySendMsgBatchRequestBody,
    PostMyUpdateNotifyRequestBody,
    PostMyWhoSponsoredMeRequestBody,
    PostMyCheckSendMsgBatchRequestBody,
    PostDeleteSponsorRelationRequestBody,
)

if TYPE_CHECKING:
    from afdiankit import AfdianCore


class MyClient:
    def __init__(self, afdian: "AfdianCore"):
        self._afdian = afdian

    def get_session_user(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/profile"

        return self._afdian.request(
            "GET",
            url,
        )

    async def async_get_session_user(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/profile"

        return await self._afdian.arequest(
            "GET",
            url,
        )

    def get_my_bill_history(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/bill-history"

        return self._afdian.request(
            "GET",
            url,
        )

    async def async_get_my_bill_history(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/bill-history"

        return await self._afdian.arequest(
            "GET",
            url,
        )

    def get_my_dashboard(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/dashboard"

        return self._afdian.request(
            "GET",
            url,
        )

    async def async_get_my_dashboard(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/dashboard"

        return await self._afdian.arequest(
            "GET",
            url,
        )

    def get_my_withdraw_history(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/withdraw-history"

        return self._afdian.request(
            "GET",
            url,
        )

    async def async_get_my_withdraw_history(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/withdraw-history"

        return await self._afdian.arequest(
            "GET",
            url,
        )

    def get_my_apply_withdraw(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/apply-withdraw"

        return self._afdian.request(
            "POST",
            url,
        )

    async def async_get_my_apply_withdraw(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/apply-withdraw"

        return await self._afdian.arequest(
            "POST",
            url,
        )

    def post_my_edit_basic(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/my/edit-basic"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostMyEditBasicRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._afdian.request(
            "POST",
            url,
            json=exclude_unset(json),
        )

    async def async_post_my_edit_basic(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/my/edit-basic"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostMyEditBasicRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._afdian.arequest(
            "POST",
            url,
            json=exclude_unset(json),
        )

    def get_my_check(
        self,
        local_new_msg_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/check"

        params = {
            "local_new_msg_id": local_new_msg_id,
        }

        return self._afdian.request(
            "GET",
            url,
            params=exclude_unset(params),
        )

    async def async_get_my_check(
        self,
        local_new_msg_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/check"

        params = {
            "local_new_msg_id": local_new_msg_id,
        }

        return await self._afdian.arequest(
            "GET",
            url,
            params=exclude_unset(params),
        )

    def get_my_notice_bar(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/notice-bar"

        return self._afdian.request(
            "GET",
            url,
        )

    async def async_get_my_notice_bar(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/notice-bar"

        return await self._afdian.arequest(
            "GET",
            url,
        )

    def get_my_sponsored_bill(
        self,
        pay_success_sn: str,
        type: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/sponsored-bill"

        params = {
            "pay_success_sn": pay_success_sn,
            "type": type,
        }

        return self._afdian.request(
            "GET",
            url,
            params=exclude_unset(params),
        )

    async def async_get_my_sponsored_bill(
        self,
        pay_success_sn: str,
        type: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/sponsored-bill"

        params = {
            "pay_success_sn": pay_success_sn,
            "type": type,
        }

        return await self._afdian.arequest(
            "GET",
            url,
            params=exclude_unset(params),
        )

    def get_my_sponsored_bill_filter(
        self,
        page: int,
        sort_field: str,
        sort_value: str,
        is_redeem: int,
        plan_id: str,
        sign_status: int,
        has_remark: int,
        status: str,
        order_id: str,
        nick_name: str,
        remark: str,
        express_no: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/sponsored-bill-filter"

        params = {
            "page": page,
            "sort_field": sort_field,
            "sort_value": sort_value,
            "is_redeem": is_redeem,
            "plan_id": plan_id,
            "sign_status": sign_status,
            "has_remark": has_remark,
            "status": status,
            "order_id": order_id,
            "nick_name": nick_name,
            "remark": remark,
            "express_no": express_no,
        }

        return self._afdian.request(
            "GET",
            url,
            params=exclude_unset(params),
        )

    async def async_get_my_sponsored_bill_filter(
        self,
        page: int,
        sort_field: str,
        sort_value: str,
        is_redeem: int,
        plan_id: str,
        sign_status: int,
        has_remark: int,
        status: str,
        order_id: str,
        nick_name: str,
        remark: str,
        express_no: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/sponsored-bill-filter"

        params = {
            "page": page,
            "sort_field": sort_field,
            "sort_value": sort_value,
            "is_redeem": is_redeem,
            "plan_id": plan_id,
            "sign_status": sign_status,
            "has_remark": has_remark,
            "status": status,
            "order_id": order_id,
            "nick_name": nick_name,
            "remark": remark,
            "express_no": express_no,
        }

        return await self._afdian.arequest(
            "GET",
            url,
            params=exclude_unset(params),
        )

    def get_my_sponsoring(
        self,
        need_sponsor_info: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/sponsoring"

        params = {
            "need_sponsor_info": need_sponsor_info,
        }

        return self._afdian.request(
            "GET",
            url,
            params=exclude_unset(params),
        )

    async def async_get_my_sponsoring(
        self,
        need_sponsor_info: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/sponsoring"

        params = {
            "need_sponsor_info": need_sponsor_info,
        }

        return await self._afdian.arequest(
            "GET",
            url,
            params=exclude_unset(params),
        )

    def get_my_account(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/account"

        return self._afdian.request(
            "GET",
            url,
        )

    async def async_get_my_account(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/account"

        return await self._afdian.arequest(
            "GET",
            url,
        )

    def get_my_creator_accomplishment(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/creator-accomplishment"

        return self._afdian.request(
            "GET",
            url,
        )

    async def async_get_my_creator_accomplishment(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/creator-accomplishment"

        return await self._afdian.arequest(
            "GET",
            url,
        )

    def post_my_creator_share_page(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/creator-share-page"

        return self._afdian.request(
            "POST",
            url,
        )

    async def async_post_my_creator_share_page(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/creator-share-page"

        return await self._afdian.arequest(
            "POST",
            url,
        )

    def post_my_notice(
        self,
        publish_sn: str,
        type: str,
        action: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/notice"

        params = {
            "publish_sn": publish_sn,
            "type": type,
            "action": action,
        }

        return self._afdian.request(
            "GET",
            url,
            params=exclude_unset(params),
        )

    async def async_post_my_notice(
        self,
        publish_sn: str,
        type: str,
        action: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/notice"

        params = {
            "publish_sn": publish_sn,
            "type": type,
            "action": action,
        }

        return await self._afdian.arequest(
            "GET",
            url,
            params=exclude_unset(params),
        )

    def get_my_income(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/income"

        return self._afdian.request(
            "GET",
            url,
        )

    async def async_get_my_income(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/income"

        return await self._afdian.arequest(
            "GET",
            url,
        )

    def get_my_joined_group(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/joined-group"

        return self._afdian.request(
            "GET",
            url,
        )

    async def async_get_my_joined_group(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/joined-group"

        return await self._afdian.arequest(
            "GET",
            url,
        )

    def get_my_marked(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/marked"

        return self._afdian.request(
            "GET",
            url,
        )

    async def async_get_my_marked(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/marked"

        return await self._afdian.arequest(
            "GET",
            url,
        )

    def get_my_marked_post(
        self,
        page: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/marked-post"

        params = {
            "page": page,
        }

        return self._afdian.request(
            "GET",
            url,
            params=exclude_unset(params),
        )

    async def async_get_my_marked_post(
        self,
        page: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/marked-post"

        params = {
            "page": page,
        }

        return await self._afdian.arequest(
            "GET",
            url,
            params=exclude_unset(params),
        )

    def get_my_product_order(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/product-order"

        return self._afdian.request(
            "GET",
            url,
        )

    async def async_get_my_product_order(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/product-order"

        return await self._afdian.arequest(
            "GET",
            url,
        )

    def get_my_sponsored_bill_out_filter(
        self,
        page: int,
        sort_field: str,
        sort_value: str,
        is_redeem: int,
        plan_id: str,
        sign_status: str,
        status: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/sponsored-bill-out-filter"

        params = {
            "page": page,
            "sort_field": sort_field,
            "sort_value": sort_value,
            "is_redeem": is_redeem,
            "plan_id": plan_id,
            "sign_status": sign_status,
            "status": status,
        }

        return self._afdian.request(
            "GET",
            url,
            params=exclude_unset(params),
        )

    async def async_get_my_sponsored_bill_out_filter(
        self,
        page: int,
        sort_field: str,
        sort_value: str,
        is_redeem: int,
        plan_id: str,
        sign_status: str,
        status: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/sponsored-bill-out-filter"

        params = {
            "page": page,
            "sort_field": sort_field,
            "sort_value": sort_value,
            "is_redeem": is_redeem,
            "plan_id": plan_id,
            "sign_status": sign_status,
            "status": status,
        }

        return await self._afdian.arequest(
            "GET",
            url,
            params=exclude_unset(params),
        )

    def get_api_my_blacked(
        self,
        page: int,
        type: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/blacked"

        params = {
            "page": page,
            "type": type,
        }

        return self._afdian.request(
            "GET",
            url,
            params=exclude_unset(params),
        )

    async def async_get_api_my_blacked(
        self,
        page: int,
        type: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/blacked"

        params = {
            "page": page,
            "type": type,
        }

        return await self._afdian.arequest(
            "GET",
            url,
            params=exclude_unset(params),
        )

    def get_my_stat(
        self,
        page: int,
        type: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/stat"

        params = {
            "page": page,
            "type": type,
        }

        return self._afdian.request(
            "GET",
            url,
            params=exclude_unset(params),
        )

    async def async_get_my_stat(
        self,
        page: int,
        type: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/stat"

        params = {
            "page": page,
            "type": type,
        }

        return await self._afdian.arequest(
            "GET",
            url,
            params=exclude_unset(params),
        )

    def post_my_who_sponsored_me(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/my/who-sponsored-me"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostMyWhoSponsoredMeRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._afdian.request(
            "POST",
            url,
            json=exclude_unset(json),
        )

    async def async_post_my_who_sponsored_me(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/my/who-sponsored-me"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostMyWhoSponsoredMeRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._afdian.arequest(
            "POST",
            url,
            json=exclude_unset(json),
        )

    def post_my_check_send_msg_batch(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/my/check-send-msg-batch"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostMyCheckSendMsgBatchRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._afdian.request(
            "POST",
            url,
            json=exclude_unset(json),
        )

    async def async_post_my_check_send_msg_batch(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/my/check-send-msg-batch"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostMyCheckSendMsgBatchRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._afdian.arequest(
            "POST",
            url,
            json=exclude_unset(json),
        )

    def post_my_send_msg_batch(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/my/send-msg-batch"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostMySendMsgBatchRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._afdian.request(
            "POST",
            url,
            json=exclude_unset(json),
        )

    async def async_post_my_send_msg_batch(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/my/send-msg-batch"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostMySendMsgBatchRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._afdian.arequest(
            "POST",
            url,
            json=exclude_unset(json),
        )

    def post_my_send_msg_batch_progress(
        self,
        task_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/send-msg-batch-progress"

        params = {
            "task_id": task_id,
        }

        return self._afdian.request(
            "GET",
            url,
            params=exclude_unset(params),
        )

    async def async_post_my_send_msg_batch_progress(
        self,
        task_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/send-msg-batch-progress"

        params = {
            "task_id": task_id,
        }

        return await self._afdian.arequest(
            "GET",
            url,
            params=exclude_unset(params),
        )

    def get_my_notify_config(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/notify-config"

        return self._afdian.request(
            "GET",
            url,
        )

    async def async_get_my_notify_config(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/notify-config"

        return await self._afdian.arequest(
            "GET",
            url,
        )

    def post_my_update_notify(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/my/update-notify"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostMyUpdateNotifyRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._afdian.request(
            "POST",
            url,
            json=exclude_unset(json),
        )

    async def async_post_my_update_notify(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/my/update-notify"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostMyUpdateNotifyRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._afdian.arequest(
            "POST",
            url,
            json=exclude_unset(json),
        )

    def get_sponsored_bill_out_count(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/sponsored-bill-out-count"

        return self._afdian.request(
            "GET",
            url,
        )

    async def async_get_sponsored_bill_out_count(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = "/api/my/sponsored-bill-out-count"

        return await self._afdian.arequest(
            "GET",
            url,
        )

    def post_set_show_badge(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/my/set-show-badge"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostSetShowBadgeRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._afdian.request(
            "POST",
            url,
            json=exclude_unset(json),
        )

    async def async_post_set_show_badge(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/my/set-show-badge"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostSetShowBadgeRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._afdian.arequest(
            "POST",
            url,
            json=exclude_unset(json),
        )

    def post_delete_sponsor_relation(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/my/delete-sponsor-relation"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostDeleteSponsorRelationRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._afdian.request(
            "POST",
            url,
            json=exclude_unset(json),
        )

    async def async_post_delete_sponsor_relation(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Literal[UNSET] = UNSET,
        **kwargs,
    ):
        url = "/api/my/delete-sponsor-relation"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(PostDeleteSponsorRelationRequestBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._afdian.arequest(
            "POST",
            url,
            json=exclude_unset(json),
        )
