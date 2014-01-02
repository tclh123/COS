/* user module

table open_id_kind
table user
table staff
table permission

 */

insert into open_id_kind values (NULL, 'company_staff_id', now());

insert into permission values (NULL, 1, '餐厅员工基本权限(basic)');
insert into permission values (NULL, 2, '管理员权限(admin)');
insert into permission values (NULL, 4, '送餐员权限(delivery)');

insert into staff values (NULL, 7);
insert into staff values (NULL, 3);
insert into staff values (NULL, 1);

insert into user values (NULL, 1, 13101249, 'Harry Lee', 'tclh123@gmail.com', 'user', NULL, now());
insert into user values (NULL, 1, 10000001, 'Ace', 'ace@tclh123.com', 'staff', 1, now());
insert into user values (NULL, 1, 10000002, 'KING', 'king@tclh123.com', 'staff', 2, now());
insert into user values (NULL, 1, 10000003, 'QUEEN', 'queen@tclh123.com', 'staff', 3, now());
