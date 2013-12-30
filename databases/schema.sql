-- COS - Cafeteria Ordering System

drop schema if exists `cosdb`;
CREATE SCHEMA `cosdb`;
use `cosdb`;

/* clean up old tables;
   must drop tables with foreign keys first
   due to referential integrity constraints
 */
drop table if exists user;

--
-- Table structure for table "open_id"
--
CREATE TABLE `open_id_kind` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `kind_name` varchar(20) NOT NULL,
  `created_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table "user"
--
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `open_id_kind` int(11) NOT NULL,
  `open_id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `type` varchar(16) NOT NULL,
  `target_id` int(11) NOT NULL,
  `created_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
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
  `desc` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
