/* user module

table open_id_kind
table user
table staff
table permission

 */
use `cosdb`;

insert into staff values (NULL, 7, now());
insert into staff values (NULL, 3, now());
insert into staff values (NULL, 1, now());
insert into staff values (NULL, 4, now());

insert into user values (NULL, 1, 13101249, 'Harry Lee', 'tclh123@gmail.com', 'user', NULL, now(), now());
insert into user values (NULL, 1, 10000001, 'Ace', 'ace@tclh123.com', 'staff', 1, now(), now());
insert into user values (NULL, 1, 10000002, 'KING', 'king@tclh123.com', 'staff', 2, now(), now());
insert into user values (NULL, 1, 10000003, 'QUEEN', 'queen@tclh123.com', 'staff', 3, now(), now());
insert into user values (NULL, 1, 10000004, 'DELIVERMAN', 'd@tclh123.com', 'staff', 4, now(), now());
