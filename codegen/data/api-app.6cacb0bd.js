[
  {
    name: "GET_INIT_CONFIG",
    url: "/api/init/config",
    method: "get",
    data: {},
  },
  {
    name: "POST_LOG_COLLECT",
    url: "/api/log/collect",
    method: "post",
    data: {
      stat_id: "",
      uri: "",
      refer: "",
    },
  },
  {
    name: "POST_VERIFY_CODE",
    url: "/api/passport/send-verify-code",
    method: "post",
    data: {
      account: "",
      password: "",
      name: "",
    },
  },
  {
    name: "POST_REG",
    url: "/api/passport/register",
    method: "post",
    data: {
      account: "",
      password: "",
      name: "",
      code: "",
      mp_token: "",
    },
  },
  {
    name: "POST_LOGIN",
    url: "/api/passport/login",
    method: "post",
    data: {
      account: "",
      password: "",
      mp_token: "",
    },
  },
  {
    name: "POST_QUICK_LOGIN",
    url: "/api/passport/quick-login",
    method: "post",
    data: {
      account: "",
      code: "",
      mp_token: "",
    },
  },
  {
    name: "POST_SEND_QL_CODE",
    url: "/api/passport/send-ql-code",
    method: "post",
    data: {
      account: "",
    },
  },
  {
    name: "POST_QUICK_LOGIN_CODE",
    url: "/api/passport/send-quick-login-code",
    method: "post",
    data: {
      account: "",
    },
  },
  {
    name: "POST_SEND_FORGET_CODE",
    url: "/api/passport/send-forget-code",
    method: "post",
    data: {
      account: "",
    },
  },
  {
    name: "POST_CHECK_FORGET_CODE",
    url: "/api/passport/check-forget-code",
    method: "post",
    data: {
      account: "",
      code: "",
    },
  },
  {
    name: "POST_RESET_PASSWORD",
    url: "/api/passport/reset-password",
    method: "post",
    data: {
      token: "",
      password: "",
    },
  },
  {
    name: "GET_SESSION_USER",
    url: "/api/my/profile",
    method: "get",
    data: {},
  },
  {
    name: "GET_CATEGORY_LIST",
    url: "/api/category/list",
    method: "get",
    data: {},
  },
  {
    name: "GET_CATEGORY_EDIT_LIST",
    url: "/api/category/edit-list",
    method: "get",
    data: {},
  },
  {
    name: "POST_EDIT_BASIC",
    url: "/api/creator/edit-basic",
    method: "post",
    data: {
      name: "",
      avatar: "",
      url_slug: "",
      category_id: "",
      type: "",
      doing: "",
      detail: "",
      pic: "",
      cover: "",
      watermark: "",
    },
  },
  {
    name: "POST_EDIT_PLAN",
    url: "/api/creator/edit-plan",
    method: "post",
    data: {
      plan_id: "",
      name: "",
      price: "",
      desc: "",
      pic: "",
      status: "",
      reply_switch: "",
      reply_content: "",
      reply_random_switch: "",
      reply_random_content: "",
      independent: "",
      permanent: "",
      sku: [],
      need_address: "",
      pay_month: "",
      favorable_price: "",
      product_discount_price: "",
      product_vip_price: "",
      vip_price_related_plan_ids: "",
      has_time_limit_price: 0,
      time_limit_begin: "",
      time_limit_end: "",
      time_limit_price: "",
      time_limit_discount: "",
      product_type: "",
      bundle_stock: "",
      bundle_sku_select_count: "",
      product_vip_price_include_history: 0,
      has_plan_config: 0,
      remark_name: "",
      remark_placeholder: "",
      remark_required: "",
      can_ali_agreement: "",
    },
  },
  {
    name: "POST_DEL_PLAN",
    url: "/api/creator/delete-plan",
    method: "post",
    data: {
      plan_id: "",
    },
  },
  {
    name: "POST_EDIT_WITHDRAW",
    url: "/api/creator/edit-withdraw",
    method: "post",
    data: {
      realname: "",
      account: "",
      type: "",
    },
  },
  {
    name: "GET_ALL_PLANS",
    url: "/api/creator/all-plans",
    method: "get",
    data: {
      post_only: "",
      sale_only: "",
      status: "",
    },
  },
  {
    name: "GET_WITHDRAW_METHOD",
    url: "/api/creator/withdraw-method",
    method: "get",
    data: {},
  },
  {
    name: "GET_USER_PROFILE",
    url: "/api/user/get-profile",
    method: "get",
    data: {
      user_id: "",
    },
  },
  {
    name: "GET_USER_PROFILE_BY_SLUG",
    url: "/api/user/get-profile-by-slug",
    method: "get",
    data: {
      url_slug: "",
    },
  },
  ($ = {
    name: "GET_CREATOR_PLANS",
    url: "/api/creator/get-plans",
    method: "get",
    data: {
      user_id: "",
      album_id: "",
      unlock_plan_ids: "",
    },
  }),
  {
    name: "GET_ORDER_PREPARE",
    url: "/api/order/prepare",
    method: "post",
    data: {
      plan_id: "",
      user_id: "",
      sku_detail: "",
      product_type: "",
    },
  },
  {
    name: "POST_CREATE_ORDER",
    url: "/api/order/create-order",
    method: "post",
    data: {
      plan_id: "",
      month: "",
      total_amount: "",
      out_trade_no: "",
      pay_type: "alipay",
      code: "",
      user_id: "",
      per_month: "",
      remark: "",
      mp_token: "",
      show_amount: "",
      addr_name: "",
      addr_phone: "",
      addr_address: "",
      sku_detail: [],
      plan_invite_code: "",
      custom_order_id: "",
      cmid: "",
      card_id_list: [],
      ticket_round_id: "",
      agreement: "",
    },
  },
  {
    name: "POST_ORDER_CHECK",
    url: "/api/order/check",
    method: "get",
    data: {
      out_trade_no: "",
    },
  },
  {
    name: "POST_PAYPAL_CAPTURE",
    url: "/api/paypal/capture",
    method: "get",
    data: {
      out_trade_no: "",
      token: "",
      PayerID: "",
    },
  },
  {
    name: "GET_ORDER_SIGN",
    url: "/api/order/sign",
    method: "get",
    data: {
      out_trade_no: "",
    },
  },
  {
    name: "GET_MY_BILL_HISTORY",
    url: "/api/my/bill-history",
    method: "get",
    data: {},
  },
  {
    name: "GET_ORDER_CANCEL",
    url: "/api/order/cancel-order",
    method: "post",
    data: {
      out_trade_no: "",
    },
  },
  {
    name: "GET_CREATOR_LIST",
    url: "/api/creator/list",
    method: "get",
    data: {
      page: 1,
      type: "",
      category_id: "",
      q: "",
    },
  },
  {
    name: "GET_MY_DASHBOARD",
    url: "/api/my/dashboard",
    method: "get",
    data: {},
  },
  {
    name: "GET_MY_WITHDRAW_HISTORY",
    url: "/api/my/withdraw-history",
    method: "get",
    data: {},
  },
  {
    name: "GET_MY_APPLY_WITHDRAW",
    url: "/api/my/apply-withdraw",
    method: "post",
    data: {},
  },
  {
    name: "POST_MY_EDIT_BASIC",
    url: "/api/my/edit-basic",
    method: "post",
    data: {
      avatar: "",
      name: "",
      addr_name: "",
      addr_phone: "",
      addr_address: "",
      gender: "",
      birthday: "",
    },
  },
  {
    name: "GET_USER_SPONSORING",
    url: "/api/user/get-sponsoring",
    method: "get",
    data: {
      user_id: "",
    },
  },
  {
    name: "GET_MESSAGE_DIALOGS",
    url: "/api/message/dialogs",
    method: "get",
    data: {
      page: 1,
      unread: "",
    },
  },
  {
    name: "GET_MESSAGE_MESSAGES",
    url: "/api/message/messages",
    method: "get",
    data: {
      user_id: "",
      type: "old",
      message_id: "",
    },
  },
  {
    name: "POST_MESSAGE_SEND",
    url: "/api/message/send",
    method: "post",
    data: {
      user_id: "",
      type: "",
      content: "",
    },
  },
  {
    name: "GET_MESSAGE_CAN_SEND",
    url: "/api/message/can-send",
    method: "get",
    data: {
      user_id: "",
    },
  },
  {
    name: "GET_MY_CHECK",
    url: "/api/my/check",
    method: "get",
    data: {
      local_new_msg_id: "",
    },
  },
  {
    name: "GET_MY_NOTICE_BAR",
    url: "/api/my/notice-bar",
    method: "get",
    data: {},
  },
  {
    name: "GET_USER_SPONSOR_INFO",
    url: "/api/user/sponsor-info",
    method: "get",
    data: {
      user_id: "",
    },
  },
  {
    name: "GET_MY_SPONSORED_BILL",
    url: "/api/my/sponsored-bill",
    method: "get",
    data: {
      pay_success_sn: "",
      type: "old",
    },
  },
  {
    name: "GET_MY_SPONSORED_BILL_FILTER",
    url: "/api/my/sponsored-bill-filter",
    method: "get",
    data: {
      page: 1,
      sort_field: "update_time",
      sort_value: "desc",
      is_redeem: 0,
      plan_id: "",
      sign_status: 0,
      has_remark: 0,
      status: "",
      order_id: "",
      nick_name: "",
      remark: "",
      express_no: "",
    },
  },
  {
    name: "GET_ORDER_WXJSURL",
    url: "/api/order/wxjsurl",
    method: "get",
    data: {
      url: "",
    },
  },
  {
    name: "POST_POST_PUBLISH",
    url: "/api/post/publish",
    method: "post",
    data: {
      post_id: "",
      vote_id: "",
      cate: "",
      title: "",
      content: "",
      pics: "",
      is_public: "",
      min_price: "",
      audio: "",
      video: "",
      audio_thumb: "",
      video_thumb: "",
      type: 0,
      cover: "",
      group_id: "",
      is_feed: 0,
      plan_ids: "",
      album_ids: "",
      attachment: [],
      timing: "",
      optype: "publish",
      preview_text: "",
      cover: "",
    },
  },
  {
    name: "POST_POST_DELETE",
    url: "/api/post/delete",
    method: "post",
    data: {
      post_id: "",
    },
  },
  {
    name: "POST_CREATOR_REM_ALBUM_POST",
    url: "/api/creator/rem-album-post",
    method: "post",
    data: {
      post_id: "",
      album_id: "",
    },
  },
  {
    name: "GET_POST_LIST",
    url: "/api/post/get-list",
    method: "get",
    data: {
      user_id: "",
      type: "old",
      publish_sn: "",
      per_page: 10,
      group_id: "",
      all: "",
      is_public: "",
      plan_id: "",
      title: "",
      name: "",
    },
  },
  {
    name: "POST_POST_LIKE",
    url: "/api/post/like",
    method: "post",
    data: {
      post_id: "",
    },
  },
  {
    name: "POST_POST_UNLIKE",
    url: "/api/post/unlike",
    method: "post",
    data: {
      post_id: "",
    },
  },
  {
    name: "POST_COMMENT_LIKE",
    url: "/api/comment/like",
    method: "post",
    data: {
      comment_id: "",
    },
  },
  {
    name: "POST_COMMENT_UNLIKE",
    url: "/api/comment/unlike",
    method: "post",
    data: {
      comment_id: "",
    },
  },
  {
    name: "POST_CREATOR_CUSTOM_PLAN_SWITCH",
    url: "/api/creator/custom-plan-switch",
    method: "post",
    data: {
      status: "",
      desc: "",
    },
  },
  {
    name: "POST_CREATOR_HIDE_PLAN",
    url: "/api/creator/hide-plan",
    method: "post",
    data: {
      plan_id: "",
    },
  },
  {
    name: "POST_CREATOR_SHOW_PLAN",
    url: "/api/creator/show-plan",
    method: "post",
    data: {
      plan_id: "",
    },
  },
  {
    name: "GET_POST_GET_DETAIL",
    url: "/api/post/get-detail",
    method: "get",
    data: {
      post_id: "",
      album_id: "",
    },
  },
  {
    name: "GET_COMMENT_GET_LIST",
    url: "/api/comment/get-list",
    method: "get",
    data: {
      post_id: "",
      publish_sn: "",
      type: "old",
      hot: "",
    },
  },
  {
    name: "POST_COMMENT_PUBLISH",
    url: "/api/comment/publish",
    method: "post",
    data: {
      post_id: "",
      content: "",
      reply_comment_id: "",
    },
  },
  {
    name: "GET_CREATOR_GET_TOP_SPONSORS",
    url: "/api/creator/get-top-sponsors",
    method: "get",
    data: {
      user_id: "",
    },
  },
  {
    name: "GET_CREATOR_GET_SPONSORS",
    url: "/api/creator/get-sponsors",
    method: "get",
    data: {
      user_id: "",
      type: "",
      page: "",
    },
  },
  {
    name: "GET_CREATOR_GET_THANK_SPONSORS",
    url: "/api/creator/get-thank-sponsors",
    method: "get",
    data: {
      user_id: "",
      month: "",
      year: "",
      page: 1,
    },
  },
  {
    name: "GET_CREATOR_GET_THANK_WORD",
    url: "/api/creator/get-thank-word",
    method: "get",
    data: {
      user_id: "",
      month: "",
      year: "",
    },
  },
  {
    name: "POST_CREATOR_EDIT_THANK_WORD",
    url: "/api/creator/edit-thank-word",
    method: "post",
    data: {
      content: "",
      month: "",
      year: "",
      pic: "",
    },
  },
  {
    name: "GET_ALL_GOALS",
    url: "/api/creator/all-goals",
    method: "get",
    data: {},
  },
  {
    name: "GET_CREATOR_GOALS",
    url: "/api/creator/get-goals",
    method: "get",
    data: {
      user_id: "",
    },
  },
  {
    name: "POST_EDIT_GOAL",
    url: "/api/creator/edit-goal",
    method: "post",
    data: {
      goal_id: "",
      monthly_fans: "",
      monthly_income: "",
      desc: "",
      type: 1,
      status: 1,
      begin_time: "",
      end_time: "",
    },
  },
  {
    name: "POST_DEL_GOAL",
    url: "/api/creator/delete-goal",
    method: "post",
    data: {
      goal_id: "",
    },
  },
  {
    name: "POST_CREATOR_HIDE_GOAL",
    url: "/api/creator/hide-goal",
    method: "post",
    data: {
      goal_id: "",
    },
  },
  {
    name: "POST_CREATOR_SHOW_GOAL",
    url: "/api/creator/show-goal",
    method: "post",
    data: {
      goal_id: "",
    },
  },
  {
    name: "GET_REC_LIST",
    url: "/api/post/get-rec-list",
    method: "get",
    data: {
      publish_sn: "",
      type: "old",
      all: "",
    },
  },
  {
    name: "GET_MY_REC_LIST",
    url: "/api/post/get-my-rec-list",
    method: "get",
    data: {
      publish_sn: "",
      type: "old",
      all: "",
    },
  },
  {
    name: "GET_MY_SPONSORING",
    url: "/api/my/sponsoring",
    method: "get",
    data: {
      need_sponsor_info: "",
    },
  },
  {
    name: "POST_ACCOUNT_SEND_VERIFY_CODE",
    url: "/api/account/send-verify-code",
    method: "post",
    data: {
      account: "",
    },
  },
  {
    name: "POST_ACCOUNT_CHANGE_PASSWORD",
    url: "/api/account/change-password",
    method: "post",
    data: {
      old_password: "",
      new_password: "",
    },
  },
  {
    name: "POST_ACCOUNT_BIND",
    url: "/api/account/bind",
    method: "post",
    data: {
      account: "",
      code: "",
    },
  },
  {
    name: "GET_MY_ACCOUNT",
    url: "/api/my/account",
    method: "get",
    data: {},
  },
  {
    name: "GET_MY_CREATOR_ACCOMPLISHMENT",
    url: "/api/my/creator-accomplishment",
    method: "get",
    data: {},
  },
  {
    name: "POST_MY_CREATOR_SHARE_PAGE",
    url: "/api/my/creator-share-page",
    method: "post",
    data: {},
  },
  {
    name: "POST_OAUTH_MP_REDIRECT_URI",
    url: "/api/oauth/mp-redirect-uri",
    method: "post",
    data: {
      redirect_uri: "",
    },
  },
  {
    name: "POST_OAUTH_MP_CODE",
    url: "/api/oauth/mp-code",
    method: "post",
    data: {
      code: "",
    },
  },
  {
    name: "POST_OAUTH_MX_REDIRECT_URI",
    url: "/api/oauth/wx-redirect-uri",
    method: "post",
    data: {
      redirect_uri: "",
    },
  },
  {
    name: "POST_OAUTH_MX_CODE",
    url: "/api/oauth/wx-code",
    method: "post",
    data: {
      code: "",
    },
  },
  {
    name: "POST_CREATOR_DISCOUNT_OPTION",
    url: "/api/creator/discount-option",
    method: "post",
    data: {
      status: "",
    },
  },
  {
    name: "GET_UPLOAD_SNAPSHOT ",
    url: "/api/upload/snapshot",
    method: "get",
    data: {
      snapshot_id: "",
    },
  },
  {
    name: "POST_COMMENT_DELETE ",
    url: "/api/comment/delete",
    method: "post",
    data: {
      comment_id: "",
    },
  },
  {
    name: "POST_CREATOR_SHOW_GUIDE ",
    url: "/api/creator/show-guide",
    method: "post",
    data: {
      status: "",
    },
  },
  {
    name: "POST_CREATOR_PRIVACY_PUBLIC_INCOME ",
    url: "/api/creator/privacy-public-income",
    method: "post",
    data: {
      status: "",
    },
  },
  {
    name: "POST_CREATOR_PRIVACY_PUBLIC_SPONSOR ",
    url: "/api/creator/privacy-public-sponsor",
    method: "post",
    data: {
      status: "",
    },
  },
  {
    name: "POST_MY_NOTICE",
    url: "/api/my/notice",
    method: "get",
    data: {
      publish_sn: "",
      type: "old",
      action: "",
    },
  },
  {
    name: "GET_MY_INCOME",
    url: "/api/my/income",
    method: "get",
    data: {},
  },
  {
    name: "POST_TOP",
    url: "/api/post/top",
    method: "post",
    data: {
      post_id: "",
    },
  },
  {
    name: "POST_UNTOP",
    url: "/api/post/untop",
    method: "post",
    data: {
      post_id: "",
    },
  },
  {
    name: "POST_CREATOR_EDIT_ALBUM",
    url: "/api/creator/edit-album",
    method: "post",
    data: {
      album_id: "",
      title: "",
      content: "",
      cover: "",
    },
  },
  {
    name: "GET_CREATOR_GET_ALBUM_INFO",
    url: "/api/user/get-album-info",
    method: "get",
    data: {
      album_id: "",
    },
  },
  {
    name: "POST_CREATOR_EDIT_ALBUM_POST",
    url: "/api/creator/edit-album-post",
    method: "post",
    data: {
      album_id: "",
      post_ids: "",
    },
  },
  {
    name: "GET_CREATOR_GET_ALBUM_LIST",
    url: "/api/user/get-album-list",
    method: "get",
    data: {
      user_id: "",
      page: "",
      per_page: "",
    },
  },
  {
    name: "GET_CREATOR_GET_ALBUM_POST",
    url: "/api/user/get-album-post",
    method: "get",
    data: {
      album_id: "",
      lastRank: "",
      rankOrder: "",
      rankField: "",
    },
  },
  {
    name: "POST_CREATOR_UPDATE_ALBUM_POST_ORDER_BY",
    url: " /api/creator/update-album-post-order-by",
    method: "post",
    data: {
      album_id: "",
      order_by: "",
    },
  },
  {
    name: "GET_CREATOR_GET_ALBUM_POST_IDS",
    url: " /api/creator/get-album-post-ids",
    method: "get",
    data: {
      album_id: "",
    },
  },
  {
    name: "GET_CREATOR_DEL_ALBUM",
    url: "/api/creator/del-album",
    method: "post",
    data: {
      album_id: "",
    },
  },
  {
    name: "GET_CREATOR_GET_ALBUM_CATALOG",
    url: "/api/user/get-album-catalog",
    method: "get",
    data: {
      album_id: "",
      page: 1,
      per_page: 10,
    },
  },
  {
    name: "POST_CREATOR_SHOW_ALBUM",
    url: "/api/creator/show-album",
    method: "post",
    data: {
      status: "",
    },
  },
  {
    name: "POST_CREATOR_SHOW_SHOP",
    url: "/api/creator/show-shop",
    method: "post",
    data: {
      status: "",
    },
  },
  {
    name: "POST_CREATOR_SET_SHOW_SPONSOR",
    url: "/api/creator/set-show-sponsor",
    method: "post",
    data: {
      status: "",
    },
  },
  {
    name: "GET_CREATOR_EDIT_GROUP",
    url: "/api/creator/edit-group",
    method: "post",
    data: {
      group_id: "",
      title: "",
      content: "",
      cover: "",
      type: "",
      price: "",
      join_group_type: "",
      selected_plan: "",
    },
  },
  {
    name: "GET_USER_GET_GROUP",
    url: "/api/user/get-group",
    method: "get",
    data: {
      group_id: "",
    },
  },
  {
    name: "GET_GROUP_SELECTED_PLANS",
    url: "/api/creator/get-group-selected-plans",
    method: "get",
    data: {},
  },
  {
    name: "GET_USER_GET_GROUP_FEED",
    url: "/api/user/get-group-feed",
    method: "get",
    data: {
      group_id: "",
      filter: "all",
      publish_sn: "",
      publish_sn_key: "reply_time",
    },
  },
  {
    name: "GET_CREATOR_GET_GROUP_STATUS",
    url: "/api/creator/get-group-status",
    method: "get",
    data: {},
  },
  {
    name: "GET_USER_GET_GROUP_LIST",
    url: "/api/user/get-group-list",
    method: "get",
    data: {
      user_id: "",
    },
  },
  {
    name: "GET_USER_JOIN_GROUP",
    url: "/api/user/join-group",
    method: "post",
    data: {
      group_id: "",
    },
  },
  {
    name: "GET_MY_JOINED_GROUP",
    url: "/api/my/joined-group",
    method: "get",
    data: {},
  },
  {
    name: "POST_CREATOR_OPEN_GROUP_SWITCH",
    url: "/api/creator/open-group-switch",
    method: "post",
    data: {
      group_id: "",
      status: "",
    },
  },
  {
    name: "POST_POST_TOP_GROUP",
    url: "/api/post/top-group",
    method: "post",
    data: {
      post_id: "",
    },
  },
  {
    name: "POST_POST_UNTOP_GROUP",
    url: "/api/post/untop-group",
    method: "post",
    data: {
      post_id: "",
    },
  },
  {
    name: "POST_UPLOAD_GET_SIGN",
    url: "/api/upload/get-sign",
    method: "post",
    data: {
      type: "",
    },
  },
  {
    name: "POST_UPLOAD_GET_URL",
    url: "/api/upload/get-url",
    method: "post",
    data: {
      url: "",
      type: "",
    },
  },
  {
    name: "POST_CREATOR_MAKE_REDEEM",
    url: "/api/creator/make-redeem",
    method: "post",
    data: {
      plan_id: "",
      num: "",
      sku_id: "",
    },
  },
  {
    name: "GET_CREATOR_REDEEM_HISTORY",
    url: "/api/creator/redeem-history",
    method: "get",
    data: {
      plan_id: "",
      sku_id: "",
    },
  },
  {
    name: "GET_USER_REDEEM_INFO",
    url: "/api/user/redeem-info",
    method: "get",
    data: {
      redeem_id: "",
    },
  },
  {
    name: "POST_USER_USE_REDEEM",
    url: "/api/user/use-redeem",
    method: "post",
    data: {
      redeem_id: "",
      addr_name: "",
      addr_phone: "",
      addr_address: "",
    },
  },
  {
    name: "GET_UPLOAD_GET_OBJ_SIGN",
    url: "/api/upload/get-obj-sign",
    method: "get",
    data: {},
  },
  {
    name: "GET_UPLOAD_GET_MESSAGE_SIGN",
    url: "/api/upload/get-message-sign",
    method: "get",
    data: {},
  },
  {
    name: "POST_SET_CAN_BUY_HIDE",
    url: "/api/creator/set-can-buy-hide",
    method: "post",
    data: {
      plan_id: "",
      status: "",
    },
  },
  {
    name: "GET_MY_MARKED",
    url: "/api/my/marked",
    method: "get",
    data: {},
  },
  {
    name: "GET_MY_MARKED_POST",
    url: "/api/my/marked-post",
    method: "get",
    data: {
      page: "",
    },
  },
  {
    name: "POST_USER_MARK",
    url: "/api/user/mark",
    method: "post",
    data: {
      user_id: "",
    },
  },
  {
    name: "POST_USER_UNMARK",
    url: "/api/user/unmark",
    method: "post",
    data: {
      user_id: "",
    },
  },
  {
    name: "POST_GET_PLAN_SKUS",
    url: "/api/creator/get-plan-skus",
    method: "get",
    data: {
      plan_id: "",
      is_ext: "",
    },
  },
  {
    name: "GET_MY_PRODUCT_ORDER",
    url: "/api/my/product-order",
    method: "get",
    data: {},
  },
  {
    name: "GET_MY_SPONSORED_BILL_OUT_FILTER",
    url: "/api/my/sponsored-bill-out-filter",
    method: "get",
    data: {
      page: 1,
      sort_field: "",
      sort_value: "",
      is_redeem: 0,
      plan_id: "",
      sign_status: "",
      status: "",
    },
  },
  {
    name: "POST_USER_QUIT_GROUP",
    url: "/api/user/quit-group",
    method: "post",
    data: {
      group_id: "",
    },
  },
  {
    name: "GET_CREATOR_CHECK_CERTIFICATION",
    url: "/api/creator/check-certification",
    method: "get",
    data: {},
  },
  {
    name: "POST_CREATOR_SUBMIT_CERTIFICATION",
    url: "/api/creator/submit-certification",
    method: "post",
    data: {
      url: "",
    },
  },
  {
    name: "POST_CREATOR_COPY_TEXT",
    url: "/api/creator/copy-text",
    method: "post",
    data: {
      status: "",
    },
  },
  {
    name: "POST_CREATOR_COPY_PIC",
    url: "/api/creator/copy-pic",
    method: "post",
    data: {
      status: "",
    },
  },
  {
    name: "GET_WELCOME_CATEGORY_LIST",
    url: "/api/welcome/category-list",
    method: "get",
    data: {},
  },
  {
    name: "GET_WELCOME_CATEGORY_CREATOR",
    url: "/api/welcome/category-creator",
    method: "get",
    data: {
      category_id: "",
    },
  },
  {
    name: "POST_API_USER_BLACK",
    url: "/api/user/black",
    method: "post",
    data: {
      user_id: "",
      type: "",
    },
  },
  {
    name: "POST_API_USER_UNBLACK",
    url: "/api/user/unblack",
    method: "post",
    data: {
      user_id: "",
      type: "",
    },
  },
  {
    name: "GET_API_MY_BLACKED",
    url: "/api/my/blacked",
    method: "get",
    data: {
      page: 1,
      type: "",
    },
  },
  {
    name: "POST_USER_SHOW_SPONSORING",
    url: "/api/user/show-sponsoring",
    method: "post",
    data: {
      status: "",
    },
  },
  {
    name: "GET_API_FAQ_LIST_FAQ",
    url: "/api/faq/list-faq",
    method: "get",
    data: {
      user_id: "",
    },
  },
  {
    name: "POST_API_FAQ_ASK",
    url: "/api/faq/ask",
    method: "post",
    data: {
      id: "",
      user_id: "",
    },
  },
  {
    name: "POST_API_FAQ_ANSWER",
    url: "/api/faq/answer",
    method: "post",
    data: {
      id: "",
      user_id: "",
    },
  },
  {
    name: "GET_ORDER_EXPRESS_COMPANY_LIST",
    url: "/api/order/express-company-list",
    method: "get",
    data: {},
  },
  {
    name: "POST_ORDER_UPDATE_EXPRESS",
    url: "/api/order/update-express",
    method: "post",
    data: {
      out_trade_no: "",
      company_id: "",
      express_no: "",
    },
  },
  {
    name: "POST_ORDER_UPDATE_ADDRESS",
    url: "/api/order/update-address",
    method: "post",
    data: {
      out_trade_no: "",
      addr_name: "",
      addr_phone: "",
      addr_address: "",
    },
  },
  {
    name: "GET_MY_STAT",
    url: "/api/my/stat",
    method: "get",
    data: {
      page: 1,
      type: "day",
    },
  },
  {
    name: "POST_MY_WHO_SPONSORED_ME",
    url: "/api/my/who-sponsored-me",
    method: "post",
    data: {
      page: 1,
      sort_field: "",
      sort_value: "",
      filter: [],
      per_page: 10,
    },
  },
  {
    name: "POST_MY_CHECK_SEND_MSG_BATCH",
    url: "/api/my/check-send-msg-batch",
    method: "post",
    data: {
      filter: [],
      is_all: 0,
      include_user_ids: [],
      exclude_user_ids: [],
      type: "text",
      content: "",
    },
  },
  {
    name: "POST_MY_SEND_MSG_BATCH",
    url: "/api/my/send-msg-batch",
    method: "post",
    data: {
      filter: [],
      is_all: 0,
      include_user_ids: [],
      exclude_user_ids: [],
      type: "text",
      content: "",
    },
  },
  {
    name: "POST_MY_SEND_MSG_BATCH_PROGRESS",
    url: "/api/my/send-msg-batch-progress",
    method: "get",
    data: {
      task_id: "",
    },
  },
  {
    name: "POST_CREATOR_LIST_OPEN_TOKENS",
    url: "/api/creator/list-open-tokens",
    method: "get",
    data: {},
  },
  {
    name: "POST_CREATOR_CREATE_OPEN_TOKEN",
    url: "/api/creator/create-open-token",
    method: "post",
    data: {},
  },
  {
    name: "GET_CREATOR_LIST_OPEN_WEBHOOK",
    url: "/api/creator/list-open-webhook",
    method: "get",
    data: {},
  },
  {
    name: "POST_CREATOR_UPDATE_OPEN_WEBHOOK",
    url: "/api/creator/update-open-webhook",
    method: "post",
    data: {
      url: "",
    },
  },
  {
    name: "POST_CREATOR_TEST_OPEN_WEBHOOK",
    url: "/api/creator/test-open-webhook",
    method: "post",
    data: {
      url: "",
    },
  },
  {
    name: "POST_EDIT_VOTE",
    url: "/api/post/edit-vote",
    method: "post",
    data: {
      vote_id: "",
      chosen_type: "",
      chosen_max: "",
      title: "",
      deadline: 0,
      options: [],
      deadline_type: "",
    },
  },
  {
    name: "GET_GET_VOTE",
    url: "/api/post/get-vote",
    method: "get",
    data: {
      vote_id: "",
    },
  },
  {
    name: "POST_CAST_VOTE",
    url: "/api/post/cast-vote",
    method: "post",
    data: {
      vote_id: "",
      vote: [],
    },
  },
  {
    name: "GET_MESSAGE_WORK_ORDER_OPTIONS",
    url: "/api/message/work-order-options",
    method: "get",
    data: {},
  },
  {
    name: "POST_MESSAGE_CREATE_WORK_ORDER",
    url: "/api/message/create-work-order",
    method: "post",
    data: {
      msg_id: "",
      type: "",
    },
  },
  {
    name: "GET_ORDER_QUERY_EXPRESS_PROGRESS",
    url: "/api/order/query-express-progress",
    method: "get",
    data: {
      number: "",
      mobile: "",
      out_trade_no: "",
    },
  },
  {
    name: "GET_OAUTH_JSSDK_SIGN",
    url: "/api/oauth/jssdk-sign",
    method: "post",
    data: {
      url: "",
    },
  },
  {
    name: "GET_ACCOUNT_UNBIND_WECHAT",
    url: "/api/account/unbind-wechat",
    method: "get",
    data: {},
  },
  {
    name: "GET_PRODUCTS",
    url: "/api/creator/get-products",
    method: "get",
    data: {
      user_id: "",
      page: "",
    },
  },
  {
    name: "GET_SKU",
    url: "/api/creator/get-sku",
    method: "get",
    data: {
      sku_id: "",
    },
  },
  {
    name: "POST_USER_MARK_POST",
    url: "/api/user/mark-post",
    method: "post",
    data: {
      post_id: "",
    },
  },
  {
    name: "POST_USER_UNMARK_POST",
    url: "/api/user/unmark-post",
    method: "post",
    data: {
      post_id: "",
    },
  },
  {
    name: "POST_UPDATE_USER_FEED_SETTING",
    url: "/api/post/update-user-feed-setting",
    method: "post",
    data: {
      sponsoring: "",
      unlock: "",
      in_blacklist: "",
      user_id: "",
    },
  },
  {
    name: "GET_BLOCKED_CREATORS",
    url: "/api/post/get-blocked-creators",
    method: "get",
    data: {},
  },
  {
    name: "POST_GOAL_SETTING_SPONSOR",
    url: "/api/creator/goal-setting-sponsor",
    method: "post",
    data: {
      status: "",
    },
  },
  {
    name: "POST_GOAL_SETTING_PRODUCT",
    url: "/api/creator/goal-setting-product",
    method: "post",
    data: {
      status: "",
    },
  },
  {
    name: "GET_MY_NOTIFY_CONFIG",
    url: "/api/my/notify-config",
    method: "get",
    data: {},
  },
  {
    name: "POST_MY_UPDATE_NOTIFY",
    url: "/api/my/update-notify",
    method: "post",
    data: {
      status: "",
      field: "",
    },
  },
  {
    name: "POST_SHOW_PRODUCT_COUNT_SET",
    url: "/api/creator/show-product-count-set",
    method: "post",
    data: {
      count: "",
    },
  },
  {
    name: "GET_SPONSORED_BILL_OUT_COUNT",
    url: "/api/my/sponsored-bill-out-count",
    method: "get",
    data: {},
  },
  {
    name: "GET_BANG_SEARCH_BANK",
    url: "/api/bang/search-bank",
    method: "get",
    data: {
      name: "",
    },
  },
  {
    name: "POST_API_CREATOR_SEARCH",
    url: "/api/creator/search",
    method: "post",
    data: {
      user_id: "",
      keyword: "",
      type: "",
      page: 1,
    },
  },
  {
    name: "POST_BANG_CUS_APPLICATION",
    url: "/api/bang/cus-application",
    method: "post",
    data: {
      copy: "",
      national: "",
      number: "",
      name: "",
      valid_time: "",
      mobile_number: "",
      bank_acct_no: "",
      bank_code: "",
      bank_branch_code: "",
      sms_code: "",
    },
  },
  {
    name: "POST_BANG_CUS_APPLICATION_RENEW",
    url: "/api/bang/cus-application-renew",
    method: "post",
    data: {
      copy: "",
      national: "",
      number: "",
      name: "",
      valid_time: "",
      mobile_number: "",
      bank_acct_no: "",
      bank_code: "",
      bank_branch_code: "",
      sms_code: "",
    },
  },
  {
    name: "POST_SUIYINZI_SET_PERSON_MEMBER",
    url: "/api/suiyinzi/set-person-member",
    method: "post",
    data: {
      mobile: "",
      identity_no: "",
      identity_front_img_no: "",
      identity_back_img_no: "",
      identity_no_valid_date: "",
      account_name: "",
      account_no: "",
      bank_code: "",
    },
  },
  {
    name: "POST_CHANGE_DEFAULT_WITHDRAW_METHOD",
    url: "/api/creator/change-default-withdraw-method",
    method: "post",
    data: {
      withdraw_type: "",
    },
  },
  {
    name: "POST_EDIT_CREATOR_BADGE",
    url: "/api/badge/edit-creator-badge",
    method: "post",
    data: {
      images: "",
      badge_id: "",
      selected_plan: "",
    },
  },
  {
    name: "GET_CREATOR_BADGE_LIST",
    url: "/api/badge/get-creator-badge-list",
    method: "get",
    data: {},
  },
  {
    name: "POST_BADGE_GET_USER_BADGE_DETAIL",
    url: "/api/badge/get-user-badge-detail",
    method: "post",
    data: {
      badge_set_id: "",
      user_id: "",
    },
  },
  {
    name: "GET_BADGE_GET_USER_BADGE_LIST",
    url: "/api/badge/get-user-badge-list",
    method: "get",
    data: {
      user_id: "",
    },
  },
  {
    name: "POST_SET_SHOW_BADGE",
    url: "/api/my/set-show-badge",
    method: "post",
    data: {
      display_status: "",
      badge_set_id: "",
    },
  },
  {
    name: "GET_BADGE_FIRST_SHOW",
    url: "/api/badge/first_show",
    method: "get",
    data: {
      creator_id: "",
    },
  },
  {
    name: "POST_ORDER_UPDATE_CREATOR_REMARK",
    url: "/api/order/update-creator-remark",
    method: "post",
    data: {
      out_trade_no: "",
      creator_remark: "",
    },
  },
  {
    name: "POST_OAUTH2_CLIENT_INFO",
    url: "/api/oauth2/client_info",
    method: "post",
    data: {
      client_id: "",
    },
  },
  {
    name: "POST_OAUTH2_AUTHORIZE",
    url: "/api/oauth2/authorize",
    method: "post",
    data: {
      response_type: "",
      client_id: "",
      redirect_uri: "",
      state: "",
      scope: "",
    },
  },
  {
    name: "POST_EDIT_PLAN_RANK",
    url: "/api/creator/edit-plan-rank",
    method: "post",
    data: {
      plan_ids: "",
    },
  },
  {
    name: "GET_USER_IDCARD",
    url: "/api/user/idcard",
    method: "get",
    data: {},
  },
  {
    name: "POST_USER_IDCARD_VALIDATE",
    url: "/api/user/idcard-validate",
    method: "post",
    data: {
      id_card: "",
      name: "",
      phone: "",
      license_type: "",
      is_self: "",
    },
  },
  {
    name: "POST_USER_EDIT_IDCARD",
    url: "/api/user/edit-idcard",
    method: "post",
    data: {
      id_card: "",
      name: "",
      phone: "",
      license_type: "",
      id: "",
    },
  },
  {
    name: "GET_USER_DELETE_IDCARD",
    url: "/api/user/delete-idcard",
    method: "get",
    data: {
      id: "",
    },
  },
  {
    name: "GET_ALL_IDCARDS",
    url: "/api/user/all-idcards",
    method: "get",
    data: {},
  },
  {
    name: "GET_ORDER_TICKETS",
    url: "/api/order/tickets",
    method: "get",
    data: {
      out_trade_no: "",
    },
  },
  {
    name: "GET_ORDER_TICKET_CHECKIN",
    url: "/api/order/ticket-checkin",
    method: "get",
    data: {
      out_trade_no: "",
      id: "",
    },
  },
  {
    name: "GET_MESSAGE_DELETE_DIALOG",
    url: "/api/message/delete-dialog",
    method: "get",
    data: {
      user_id: "",
    },
  },
  {
    name: "GET_REPORT_PREPARE",
    url: "/api/user/report-prepare",
    method: "get",
    data: {
      object_type: "",
    },
  },
  {
    name: "POST_REPORT",
    url: "/api/user/report",
    method: "post",
    data: {
      object_type: "",
      object_id: "",
      report_type: "",
      report_reason: "",
    },
  },
  {
    name: "GET_ORDER_TRANSFER_PAY_URL",
    url: "/api/order/transfer-pay-url",
    method: "get",
    data: {
      out_trade_no: "",
    },
  },
  {
    name: "POST_ACCOUNT_SUBMIT_CANCELLATION",
    url: "/api/account/submit-cancellation",
    method: "post",
    data: {
      account: "",
      password: "",
      reason: "",
      content: "",
    },
  },
  {
    name: "GET_ACCOUNT_CHECK_CANCELLATION",
    url: "/api/account/check-cancellation",
    method: "get",
    data: {},
  },
  {
    name: "POST_ACCOUNT_CANCEL_CANCELLATION",
    url: "/api/account/cancel-cancellation",
    method: "post",
    data: {},
  },
  {
    name: "POST_DELETE_SPONSOR_RELATION",
    url: "/api/my/delete-sponsor-relation",
    method: "post",
    data: {
      remote_id: "",
    },
  },
  {
    name: "POST_ADD_TEAM_MEMBER",
    url: "/api/creator/add-team-member",
    method: "post",
    data: {
      account: "",
      member_name: "",
    },
  },
  {
    name: "POST_DELETE_TEAM_MEMBER",
    url: "/api/creator/delete-team-member",
    method: "post",
    data: {
      user_id: "",
    },
  },
  {
    name: "POST_EDIT_TEAM_MEMBER",
    url: "/api/creator/edit-team-member",
    method: "post",
    data: {
      user_id: "",
      member_name: "",
    },
  },
  {
    name: "GET_TEAM_MEMBERS",
    url: "/api/creator/get-team-members",
    method: "get",
    data: {},
  },
  {
    name: "GET_TEAM_MEMBER_INFO",
    url: "/api/creator/get-team-member-info",
    method: "get",
    data: {
      user_id: "",
    },
  },
];
