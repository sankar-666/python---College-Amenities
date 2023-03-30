/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.3.20-MariaDB : Database - college_amenities
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`college_amenities` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `college_amenities`;

/*Table structure for table `account` */

DROP TABLE IF EXISTS `account`;

CREATE TABLE `account` (
  `account_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `acc_no` varchar(100) DEFAULT NULL,
  `branch` varchar(100) DEFAULT NULL,
  `ifsc` varchar(100) DEFAULT NULL,
  `holder_name` varchar(100) DEFAULT NULL,
  `qr_code` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`account_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `account` */

/*Table structure for table `amenites` */

DROP TABLE IF EXISTS `amenites`;

CREATE TABLE `amenites` (
  `amenity_id` int(11) NOT NULL AUTO_INCREMENT,
  `amenity_type_id` int(11) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`amenity_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `amenites` */

/*Table structure for table `amenity_type` */

DROP TABLE IF EXISTS `amenity_type`;

CREATE TABLE `amenity_type` (
  `amenity_type_id` int(11) NOT NULL AUTO_INCREMENT,
  `type_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`amenity_type_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `amenity_type` */

/*Table structure for table `bookings` */

DROP TABLE IF EXISTS `bookings`;

CREATE TABLE `bookings` (
  `bookings_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `amenity_id` int(11) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  `for_date` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  `purpose` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`bookings_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `bookings` */

/*Table structure for table `class` */

DROP TABLE IF EXISTS `class`;

CREATE TABLE `class` (
  `class_id` int(11) NOT NULL AUTO_INCREMENT,
  `department_id` int(11) DEFAULT NULL,
  `class_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`class_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `class` */

/*Table structure for table `department` */

DROP TABLE IF EXISTS `department`;

CREATE TABLE `department` (
  `department_id` int(11) NOT NULL AUTO_INCREMENT,
  `principal_id` int(11) DEFAULT NULL,
  `dep_name` varchar(100) DEFAULT NULL,
  `hod_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`department_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `department` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `booking_id` int(11) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `reciept_file` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

/*Table structure for table `principal` */

DROP TABLE IF EXISTS `principal`;

CREATE TABLE `principal` (
  `principal_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`principal_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `principal` */

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `user` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
