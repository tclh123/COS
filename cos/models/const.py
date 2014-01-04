# coding=utf-8


PERM_BASIC = 0b001
PERM_ADMIN = 0b010
PERM_DELIVERY = 0b100

ORDER_STATUS_SUBMIT = 1
ORDER_STATUS_PAY = 2
ORDER_STATUS_WAIT = 3
ORDER_STATUS_DELIVERY = 4
ORDER_STATUS_OVER = 5
# '待买家完善订单后提交'
# '待买家付款'
# '待餐厅处理'
# '待送餐员送餐'
# '订单结束'

PAYMENT = {
    u'货到付款': 1,
    u'工资支付': 2,
    u'网上支付': 3,
}
