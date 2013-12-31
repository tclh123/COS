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
drop table if exists permission;

--
-- Table structure for table "open_id"
--
CREATE TABLE `open_id_kind` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `kind_name` varchar(100) NOT NULL,
  `created_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_name` (`kind_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table "user"
--
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `open_id_kind` int(11) NOT NULL,
  `open_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(64) NOT NULL,
  `type` varchar(16) NOT NULL,
  `target_id` int(11),
  `created_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_open_id` (`open_id_kind`, `open_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table "staff"
--
CREATE TABLE `staff` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `permissions` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table "permission"
--
CREATE TABLE `permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` int(11) NOT NULL,
  `desc` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_value` (`value`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
