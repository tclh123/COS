-- COS - Cafeteria Ordering System

drop schema if exists `cosdb`;
CREATE SCHEMA `cosdb`;
use `cosdb`;

/* clean up old tables;
   <del>must drop tables with foreign keys first
   due to referential integrity constraints</del>
 */
drop table if exists open_id_kind;
drop table if exists user;
drop table if exists staff;
drop table if exists deliveryman;
drop table if exists permission;

drop table if exists meal;
drop table if exists menu;

drop table if exists user_cart;
drop table if exists `order`;
drop table if exists order_status;
drop table if exists order_meal;
drop table if exists payment_kind;

drop table if exists inbox;

--
-- Table structure for table "open_id"
--
CREATE TABLE `open_id_kind` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `kind_name` varchar(100) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_name` (`kind_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table "user"
--
CREATE TABLE `user` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `open_id_kind` int(11) unsigned NOT NULL,
  `open_id` int(11) unsigned NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(64) NOT NULL,
  `type` varchar(16) NOT NULL,
  `target_id` int(11) unsigned DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_open_id` (`open_id_kind`, `open_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table "staff"
--
CREATE TABLE `staff` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `permissions` bigint(20) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table "deliveryman"
--
CREATE TABLE `deliveryman` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) unsigned NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table "permission"
--
create table `permission` (
  `id` int(11) unsigned not null auto_increment,
  `value` bigint(20) unsigned not null,
  `desc` varchar(200) not null,
  `created_at` timestamp not null default '0000-00-00 00:00:00',
  `updated_at` timestamp not null default current_timestamp on update current_timestamp,
  primary key (`id`),
  unique key `uk_value` (`value`)
) engine=innodb default charset=utf8;


--
-- Table structure for table "meal"
--
CREATE TABLE `meal` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `price` int(11) unsigned NOT NULL DEFAULT '0',
  `desc` varchar(1024) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table "menu"
--
CREATE TABLE `menu` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `meal_id` int(11) unsigned NOT NULL,
  `sale_price` int(11) unsigned NOT NULL,
  `amount` int(11) unsigned NOT NULL DEFAULT '0',
  `buying_amount` int(11) unsigned NOT NULL DEFAULT '0',
  `created_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_meal_id` (`meal_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table "user_cart"
--
CREATE TABLE `user_cart` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) unsigned NOT NULL,
  `meal_id` int(11) unsigned NOT NULL,
  `amount` int(11) unsigned NOT NULL DEFAULT '1',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table "order"
--
CREATE TABLE `order` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) unsigned NOT NULL,
  `status_id` smallint(5) unsigned NOT NULL,
  `delivery_time` datetime DEFAULT NULL,
  `delivery_spot` varchar(1024) DEFAULT NULL,
  `payment_kind` int(11) unsigned DEFAULT NULL,
  `is_paid` tinyint(1) NOT NULL DEFAULT '0',
  `deliveryman_id` int(11) unsigned DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table "order_status"
--
CREATE TABLE `order_status` (
  `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `desc` varchar(200) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table "order_meal"
--
CREATE TABLE `order_meal` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `order_id` int(11) unsigned NOT NULL,
  `meal_id` int(11) unsigned NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_order_id_meal_id` (`order_id`, `meal_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table "payment_kind"
--
CREATE TABLE `payment_kind` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `desc` varchar(200) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table "inbox"
--
CREATE TABLE `inbox` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) unsigned NOT NULL,
  `is_read` tinyint(1) DEFAULT '0',
  `content` varchar(1024) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
