/*
    init const data
 */

insert into open_id_kind values (NULL, 'company_staff_id', now());

insert into permission values (NULL, 1, '餐厅员工基本权限(basic)');
insert into permission values (NULL, 2, '管理员权限(admin)');
insert into permission values (NULL, 4, '送餐员权限(delivery)');


insert into order_status values (NULL, '待买家完善订单后提交', now(), now());
insert into order_status values (NULL, '待买家付款', now(), now());
insert into order_status values (NULL, '待餐厅处理', now(), now());
insert into order_status values (NULL, '待送餐员送餐', now(), now());
insert into order_status values (NULL, '订单结束', now(), now());

insert into payment_kind values (NULL, '货到付款', now(), now());
insert into payment_kind values (NULL, '工资支付', now(), now());
insert into payment_kind values (NULL, '网上支付', now(), now());
