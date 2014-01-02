/* meal module

table meal
table menu

 */
use `cosdb`;

insert into meal values (NULL, '超好吃的菜菜', 2000, '超好吃超好吃哦', now(), now());
insert into meal values (NULL, '超超好吃的菜菜', 2500, '超超好吃超好吃哦', now(), now());

insert into menu values (NULL, 1, 2000, 50, 0, now(), now());
insert into menu values (NULL, 2, 2350, 10, 0, now(), now());
