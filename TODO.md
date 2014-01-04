- init\_\*.sql
- flask + SQLAlchemy
- ~~FE: Angluar~~ 已经用了plim了，先不搞前端吧。。
- page compeleting..

        anonymous = [
            ('Home', '/'),
            (u'今日菜单', '/menu'),
        ]
        user = [
            (u'查看购物车', '/order/user_cart'),
            (u'查看订单', '/'),
            (u'预约订餐', '/'),
        ]
        staff_basic = [
            (u'菜品库管理', '/'),
        ]
        staff_delivery = [
            (u'查看待送订单', '/'),
        ]
        staff_admin = [
            (u'菜单管理', '/'),
        ]

- 为了赶作业有很多偷懒的地方 ╮(╯▽╰)╭
- FIXME: 下架的情况下，读 meal\_id 而不是 menu\_id

- compelet order\_form  //就先这样吧...去写大作业文档了
