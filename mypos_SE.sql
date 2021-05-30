-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 11, 2021 at 08:34 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 7.3.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mypos2`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add bill', 7, 'add_bill'),
(26, 'Can change bill', 7, 'change_bill'),
(27, 'Can delete bill', 7, 'delete_bill'),
(28, 'Can view bill', 7, 'view_bill'),
(29, 'Can add employee', 8, 'add_employee'),
(30, 'Can change employee', 8, 'change_employee'),
(31, 'Can delete employee', 8, 'delete_employee'),
(32, 'Can view employee', 8, 'view_employee'),
(33, 'Can add history_promotion', 9, 'add_history_promotion'),
(34, 'Can change history_promotion', 9, 'change_history_promotion'),
(35, 'Can delete history_promotion', 9, 'delete_history_promotion'),
(36, 'Can view history_promotion', 9, 'view_history_promotion'),
(37, 'Can add item_in_promotion', 10, 'add_item_in_promotion'),
(38, 'Can change item_in_promotion', 10, 'change_item_in_promotion'),
(39, 'Can delete item_in_promotion', 10, 'delete_item_in_promotion'),
(40, 'Can view item_in_promotion', 10, 'view_item_in_promotion'),
(41, 'Can add list_product', 11, 'add_list_product'),
(42, 'Can change list_product', 11, 'change_list_product'),
(43, 'Can delete list_product', 11, 'delete_list_product'),
(44, 'Can view list_product', 11, 'view_list_product'),
(45, 'Can add member', 12, 'add_member'),
(46, 'Can change member', 12, 'change_member'),
(47, 'Can delete member', 12, 'delete_member'),
(48, 'Can view member', 12, 'view_member'),
(49, 'Can add member_point', 13, 'add_member_point'),
(50, 'Can change member_point', 13, 'change_member_point'),
(51, 'Can delete member_point', 13, 'delete_member_point'),
(52, 'Can view member_point', 13, 'view_member_point'),
(53, 'Can add product', 14, 'add_product'),
(54, 'Can change product', 14, 'change_product'),
(55, 'Can delete product', 14, 'delete_product'),
(56, 'Can view product', 14, 'view_product'),
(57, 'Can add product_order', 15, 'add_product_order'),
(58, 'Can change product_order', 15, 'change_product_order'),
(59, 'Can delete product_order', 15, 'delete_product_order'),
(60, 'Can view product_order', 15, 'view_product_order'),
(61, 'Can add profit', 16, 'add_profit'),
(62, 'Can change profit', 16, 'change_profit'),
(63, 'Can delete profit', 16, 'delete_profit'),
(64, 'Can view profit', 16, 'view_profit'),
(65, 'Can add promotion', 17, 'add_promotion'),
(66, 'Can change promotion', 17, 'change_promotion'),
(67, 'Can delete promotion', 17, 'delete_promotion'),
(68, 'Can view promotion', 17, 'view_promotion'),
(69, 'Can add promotion_member', 18, 'add_promotion_member'),
(70, 'Can change promotion_member', 18, 'change_promotion_member'),
(71, 'Can delete promotion_member', 18, 'delete_promotion_member'),
(72, 'Can view promotion_member', 18, 'view_promotion_member'),
(73, 'Can add sale', 19, 'add_sale'),
(74, 'Can change sale', 19, 'change_sale'),
(75, 'Can delete sale', 19, 'delete_sale'),
(76, 'Can view sale', 19, 'view_sale'),
(77, 'Can add subscription_fee', 20, 'add_subscription_fee'),
(78, 'Can change subscription_fee', 20, 'change_subscription_fee'),
(79, 'Can delete subscription_fee', 20, 'delete_subscription_fee'),
(80, 'Can view subscription_fee', 20, 'view_subscription_fee');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$216000$eWWo8xHSt0hB$43Js1GjXN97mVlwwIdmzWbyohD1IfWhGJAqdQ0NxDrY=', '2021-04-11 01:13:47.004343', 1, 'admin', '', '', 'admin@admin.com', 1, 1, '2021-04-11 01:12:22.710273'),
(2, 'pbkdf2_sha256$216000$fOFlultDQFYr$6IoQBZRYDobA1AGZIKlrxR4REN36YPzysoPHZobTS5c=', '2021-04-11 05:31:20.345290', 0, 'pajaree', '', '', '', 0, 1, '2021-04-11 01:16:26.812538'),
(3, 'pbkdf2_sha256$216000$ssnz4Yzxk1VB$KL/A5lyK+ViD21+iSXMk68kB3V68gRrn9KlMOER/9yI=', NULL, 0, 'sujira', '', '', '', 0, 1, '2021-04-11 02:36:41.470912'),
(4, 'pbkdf2_sha256$216000$ocKsl5v3VxSU$cg+h5CgaeDpsLkrUaSQmz6x42q4FNtLGx4CAyVrI53c=', '2021-04-11 05:31:00.588966', 0, 'jay', '', '', '', 0, 1, '2021-04-11 02:44:53.891712'),
(5, 'pbkdf2_sha256$216000$w79OEJukSbPl$aHRTJBqO5izZiJKgec63VSOvBXB6275RE6Gc43NZeeU=', '2021-04-11 05:30:25.551321', 0, 'holidays', '', '', '', 0, 1, '2021-04-11 02:50:53.419626'),
(6, 'pbkdf2_sha256$216000$0ELbiTfhU024$pmllEVe+QfugIXYm4+Cs7yMTouMMLwswkbTyWDeD9iA=', '2021-04-11 03:24:53.469220', 0, 'bright', '', '', '', 0, 1, '2021-04-11 03:24:36.125020'),
(7, 'pbkdf2_sha256$216000$HcEoKBkHk2cm$BBJBUQ0WOVoBASRr4equKfM59hcamugCfLx/6yodBx8=', NULL, 0, 'Sirirakkkk', '', '', '', 0, 1, '2021-04-11 05:00:44.337177');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'Myposapp', 'bill'),
(8, 'Myposapp', 'employee'),
(9, 'Myposapp', 'history_promotion'),
(10, 'Myposapp', 'item_in_promotion'),
(11, 'Myposapp', 'list_product'),
(12, 'Myposapp', 'member'),
(13, 'Myposapp', 'member_point'),
(14, 'Myposapp', 'product'),
(15, 'Myposapp', 'product_order'),
(16, 'Myposapp', 'profit'),
(17, 'Myposapp', 'promotion'),
(18, 'Myposapp', 'promotion_member'),
(19, 'Myposapp', 'sale'),
(20, 'Myposapp', 'subscription_fee'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'Myposapp', '0001_initial', '2021-04-11 02:07:45.598579'),
(2, 'contenttypes', '0001_initial', '2021-04-11 02:07:45.631979'),
(3, 'auth', '0001_initial', '2021-04-11 02:07:45.754331'),
(4, 'admin', '0001_initial', '2021-04-11 02:07:45.937671'),
(5, 'admin', '0002_logentry_remove_auto_add', '2021-04-11 02:07:46.019219'),
(6, 'admin', '0003_logentry_add_action_flag_choices', '2021-04-11 02:07:46.027467'),
(7, 'contenttypes', '0002_remove_content_type_name', '2021-04-11 02:07:46.082361'),
(8, 'auth', '0002_alter_permission_name_max_length', '2021-04-11 02:07:46.110313'),
(9, 'auth', '0003_alter_user_email_max_length', '2021-04-11 02:07:46.126251'),
(10, 'auth', '0004_alter_user_username_opts', '2021-04-11 02:07:46.134222'),
(11, 'auth', '0005_alter_user_last_login_null', '2021-04-11 02:07:46.173402'),
(12, 'auth', '0006_require_contenttypes_0002', '2021-04-11 02:07:46.176441'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2021-04-11 02:07:46.185403'),
(14, 'auth', '0008_alter_user_username_max_length', '2021-04-11 02:07:46.200329'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2021-04-11 02:07:46.215291'),
(16, 'auth', '0010_alter_group_name_max_length', '2021-04-11 02:07:46.230290'),
(17, 'auth', '0011_update_proxy_permissions', '2021-04-11 02:07:46.244481'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2021-04-11 02:07:46.258479'),
(19, 'sessions', '0001_initial', '2021-04-11 02:07:46.281415');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('luka78ef0vad8x1k6ajepiiytydvhbtg', 'e30:1lVQcx:BL3b4DFAZ2Ld_SAw3liBliJFetnqplmqi8N4bU0ONUI', '2021-04-25 03:19:11.937410'),
('m588o0o7yzrhhg06z3czpxwm32ize9ex', '.eJxVjMEOwiAQRP-FsyGASMGj934DWXa3UjWQlPZk_HdL0oMmc5r3Zt4iwrbmuDVe4kziKow4_XYJ8MmlA3pAuVeJtazLnGRX5EGbHCvx63a4fwcZWu5rCoptSKCnszHBOae8Z7Z7PCNZtIoGDPYCjBYGBICJkt4Rea9Ai88XAmE5Ug:1lVSgq:yE3p1JkZJ1avGYeculzj-GmwDrtED6c2ccqRsnNcKEM', '2021-04-25 05:31:20.349309');

-- --------------------------------------------------------

--
-- Table structure for table `myposapp_bill`
--

CREATE TABLE `myposapp_bill` (
  `id` int(11) NOT NULL,
  `Date` date NOT NULL,
  `Time` time(6) NOT NULL,
  `Member_id` int(11) DEFAULT NULL,
  `Total` int(11) DEFAULT NULL,
  `Quantity` int(11) DEFAULT NULL,
  `Employee_name` varchar(100) NOT NULL,
  `Employee_role` varchar(100) NOT NULL,
  `Discount` int(11) DEFAULT NULL,
  `Receive` int(11) DEFAULT NULL,
  `Tax` int(11) DEFAULT NULL,
  `Profit` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myposapp_bill`
--

INSERT INTO `myposapp_bill` (`id`, `Date`, `Time`, `Member_id`, `Total`, `Quantity`, `Employee_name`, `Employee_role`, `Discount`, `Receive`, `Tax`, `Profit`) VALUES
(1, '2021-04-11', '08:45:29.753629', 1, 2499, 1, 'Pajaree', 'Admin', 0, 3000, 175, 499),
(2, '2021-04-11', '09:15:43.167106', 1, 4998, 1, 'Pajaree', 'Admin', 0, 4998, 350, 998),
(3, '2021-04-11', '09:22:00.976197', 0, 3489, 2, 'Pajaree', 'Admin', 0, 3489, 244, 1589),
(4, '2021-04-11', '09:22:14.759596', 0, 4590, 1, 'Pajaree', 'Admin', 0, 6000, 321, 1590),
(5, '2021-04-11', '09:22:38.105721', 0, 597, 1, 'Pajaree', 'Admin', 0, 600, 42, 297),
(6, '2021-04-11', '11:18:35.773207', 0, 2499, 1, 'Pajaree', 'Admin', 0, 2499, 175, 499),
(7, '2021-04-11', '12:28:05.724821', 0, 7188, 2, 'Pajaree', 'Admin', 0, 8000, 503, 2188),
(8, '2021-04-11', '12:28:56.110521', 0, 4589, 2, 'Pajaree', 'Admin', 0, 4589, 321, 1589),
(9, '2021-04-11', '12:29:36.749515', 1, 4589, 2, 'Pajaree', 'Admin', 0, 4589, 321, 1589);

-- --------------------------------------------------------

--
-- Table structure for table `myposapp_employee`
--

CREATE TABLE `myposapp_employee` (
  `id` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `IDcard` varchar(13) NOT NULL,
  `Title_Name` varchar(10) NOT NULL,
  `Firstname` varchar(100) NOT NULL,
  `Lastname` varchar(100) NOT NULL,
  `Age` int(11) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Phonenumber` varchar(10) NOT NULL,
  `Blood_Type` varchar(5) NOT NULL,
  `Birthday` date NOT NULL,
  `Ethnicity` varchar(45) NOT NULL,
  `Nationality` varchar(45) NOT NULL,
  `Religion` varchar(45) NOT NULL,
  `Address` varchar(200) NOT NULL,
  `Maritial_Status` varchar(45) NOT NULL,
  `Education_Level` varchar(100) NOT NULL,
  `Emergency_Tel` varchar(10) NOT NULL,
  `Relationship` varchar(45) NOT NULL,
  `Father_Name` varchar(45) NOT NULL,
  `Father_Lastname` varchar(45) NOT NULL,
  `Father_Career` varchar(45) DEFAULT NULL,
  `Father_Tel` varchar(45) DEFAULT NULL,
  `Father_Ethnicty` varchar(45) DEFAULT NULL,
  `Father_Nationallity` varchar(45) DEFAULT NULL,
  `Father_Religion` varchar(45) DEFAULT NULL,
  `Father_Address` varchar(45) DEFAULT NULL,
  `Mother_Title` varchar(45) NOT NULL,
  `Mother_Name` varchar(45) NOT NULL,
  `Mother_Lastname` varchar(45) NOT NULL,
  `Mother_Career` varchar(45) DEFAULT NULL,
  `Mother_Tel` varchar(45) DEFAULT NULL,
  `Mother_Ethnicty` varchar(45) DEFAULT NULL,
  `Mother_Religion` varchar(45) DEFAULT NULL,
  `Mother_Address` varchar(45) DEFAULT NULL,
  `Mother_Nationallity` varchar(45) DEFAULT NULL,
  `Role` varchar(45) NOT NULL,
  `status` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myposapp_employee`
--

INSERT INTO `myposapp_employee` (`id`, `id_user`, `IDcard`, `Title_Name`, `Firstname`, `Lastname`, `Age`, `Gender`, `Email`, `Phonenumber`, `Blood_Type`, `Birthday`, `Ethnicity`, `Nationality`, `Religion`, `Address`, `Maritial_Status`, `Education_Level`, `Emergency_Tel`, `Relationship`, `Father_Name`, `Father_Lastname`, `Father_Career`, `Father_Tel`, `Father_Ethnicty`, `Father_Nationallity`, `Father_Religion`, `Father_Address`, `Mother_Title`, `Mother_Name`, `Mother_Lastname`, `Mother_Career`, `Mother_Tel`, `Mother_Ethnicty`, `Mother_Religion`, `Mother_Address`, `Mother_Nationallity`, `Role`, `status`) VALUES
(1, 2, '1200101873570', 'Ms.', 'Pajaree', 'Wiyasing', 20, 'Female', 'tara_both@outlook.co.th', '0628019565', 'A', '2000-07-07', 'thai', 'thai', 'thai', '835/33 ข. ซ.กุลศิริศาสน์ ต.มะขามหย่ง อ.เมือง จ.ชลบุรี 20000', 'Single', 'ปี 3', '0628019565', 'friend', 'm', 'm', '', '', '', '', '', '', 'Mrs.', 'n', 'n', NULL, '', '', '', '', '', 'Admin', 1),
(2, 3, '1250100437024', 'Ms.', 'Sujira', 'Petcharat', 21, 'Female', 'sujira.pe@ku.th', '0897487492', 'B', '1999-09-18', 'Thai', 'Thai', 'Buddhist', 'Chonburi,Thailand 20230', 'Single', 'University', '0912140912', 'Friend', 'Peter', 'Parker', '', '', '', '', '', '', 'Mrs.', 'Marry', 'Jane', NULL, '', '', '', '', '', 'Admin', 0),
(3, 4, '2200601044198', 'Mr.', 'Wakkadet', 'Panyakamonkit', 20, 'Male', 'james_young@hotmail.co.th', '0639311427', 'A', '1999-10-27', 'Thai', 'Thai', 'พุทธ', '151 ม.10 ต.หมอนนาง อ.พนัสนิคม', 'Single', '้ปี3', '0639311427', 'เพื่อน', 'อยธยา', 'คาวาอิ', '', '', '', '', '', '', 'Mrs.', 'สมมณี', 'หอมศรี', NULL, '', '', '', '', '', 'Finance', 1),
(4, 5, '1104200108434', 'Mr.', 'Tanakorn', 'Pattoom', 21, 'Male', 'tana-hon1@hotmail.com', '0912140912', 'O', '1999-08-04', 'Thai', 'Thai', 'พุทธ', '59/122 ', 'Single', 'University', '0897487492', 'GF', 'Jim', 'Suriya', '', '', '', '', '', '', 'Mrs.', 'May', 'Sorayut', NULL, '', '', '', '', '', 'Cashier', 1),
(5, 6, '1111111111111', 'Mr.', 'asdasdasdasdasda', 'asdasdasdasd', 12, 'Female', 'tara_both@outlook.co.th', '0851549568', 'A', '2021-04-11', 'asd', 'asd', 'asd', 'asd', 'Single', 'asd', 'asd', 'asd', 'asd', 'asd', '', '', '', '', '', '', 'Mrs.', 'asd', 'asd', NULL, '', '', '', '', '', 'Admin', 1),
(6, 7, '1250100437024', 'Ms.', 'Sirirak', 'Ajcha', 15, 'Female', 'pajaree.wi@outlook.co.th', '0628019565', 'AB', '2020-02-11', 'Thai', 'THai', 'Buddhist', '835/33 ข. ซ.กุลศิริศาสน์ ต.มะขามหย่ง อ.เมือง จ.ชลบุรี 20000', 'Single', 'University', '0912140912', 'Friend', '-', '-', '', '', '', '', '', '', 'Ms.', 'Pajaree', 'Wiya', NULL, '', '', '', '', '', 'Cashier', 0);

-- --------------------------------------------------------

--
-- Table structure for table `myposapp_history_promotion`
--

CREATE TABLE `myposapp_history_promotion` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `types` varchar(100) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `apply` varchar(45) NOT NULL,
  `value` int(11) DEFAULT NULL,
  `atlest` int(11) DEFAULT NULL,
  `by` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myposapp_history_promotion`
--

INSERT INTO `myposapp_history_promotion` (`id`, `name`, `types`, `start_date`, `end_date`, `apply`, `value`, `atlest`, `by`) VALUES
(1, 'summer', 'Amount off', '2021-03-28', '2021-04-21', 'Some', 200, NULL, 'pajaree');

-- --------------------------------------------------------

--
-- Table structure for table `myposapp_item_in_promotion`
--

CREATE TABLE `myposapp_item_in_promotion` (
  `id` int(11) NOT NULL,
  `id_history` int(11) NOT NULL,
  `Barcode_ID` varchar(13) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Size` varchar(45) NOT NULL,
  `Color` varchar(45) NOT NULL,
  `Type` varchar(45) NOT NULL,
  `Model` varchar(45) NOT NULL,
  `Cost` varchar(45) NOT NULL,
  `Price` varchar(45) NOT NULL,
  `VAT` varchar(45) NOT NULL,
  `Excluding_VAT` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myposapp_item_in_promotion`
--

INSERT INTO `myposapp_item_in_promotion` (`id`, `id_history`, `Barcode_ID`, `Name`, `Size`, `Color`, `Type`, `Model`, `Cost`, `Price`, `VAT`, `Excluding_VAT`) VALUES
(1, 1, '1111111111111', 'Adidas', 'L', 'pink', 'all start', 'specail', '2000', '2599', '182', '2417');

-- --------------------------------------------------------

--
-- Table structure for table `myposapp_list_product`
--

CREATE TABLE `myposapp_list_product` (
  `id` int(11) NOT NULL,
  `id_promotion` int(11) NOT NULL,
  `id_product` int(11) NOT NULL,
  `Xory` varchar(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myposapp_list_product`
--

INSERT INTO `myposapp_list_product` (`id`, `id_promotion`, `id_product`, `Xory`) VALUES
(3, 2, 1, 'x'),
(4, 2, 2, 'y'),
(5, 3, 2, 'a');

-- --------------------------------------------------------

--
-- Table structure for table `myposapp_member`
--

CREATE TABLE `myposapp_member` (
  `Member_ID` int(11) NOT NULL,
  `IDcard` varchar(13) NOT NULL,
  `Title_Name` varchar(10) NOT NULL,
  `Firstname` varchar(100) NOT NULL,
  `Lastname` varchar(100) NOT NULL,
  `Age` varchar(100) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Phonenumber` varchar(10) NOT NULL,
  `Birthday` date NOT NULL,
  `Address` varchar(200) DEFAULT NULL,
  `Point` int(11) NOT NULL,
  `status` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myposapp_member`
--

INSERT INTO `myposapp_member` (`Member_ID`, `IDcard`, `Title_Name`, `Firstname`, `Lastname`, `Age`, `Gender`, `Email`, `Phonenumber`, `Birthday`, `Address`, `Point`, `status`) VALUES
(1, '1200101873570', 'Mr.', 'ปาจรีย์ ', 'วิยาสิงห์', '20', 'Female', 'pajaree.wi@live.ku.th', '0628019565', '2000-07-11', '835/33 ข. ซ.กุลศิริศาสน์ ต.มะขามหย่ง อ.เมือง จ.ชลบุรี 20000', 0, 1),
(2, '1250100437024', 'Mr.', 'Pattarapon', 'Budeee', '25', 'Male', 'pajaree.wi@ku.th', '0956485123', '2018-06-11', '835/33 ข. ซ.กุลศิริศาสน์ ต.มะขามหย่ง อ.เมือง จ.ชลบุรี 20000', 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `myposapp_member_point`
--

CREATE TABLE `myposapp_member_point` (
  `id` int(11) NOT NULL,
  `Pay_new` int(11) DEFAULT NULL,
  `Is_new` int(11) DEFAULT NULL,
  `Use_new` int(11) DEFAULT NULL,
  `discout_new` int(11) DEFAULT NULL,
  `Pay_old` int(11) DEFAULT NULL,
  `Is_old` int(11) DEFAULT NULL,
  `Use_old` int(11) DEFAULT NULL,
  `discout_old` int(11) DEFAULT NULL,
  `by` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myposapp_member_point`
--

INSERT INTO `myposapp_member_point` (`id`, `Pay_new`, `Is_new`, `Use_new`, `discout_new`, `Pay_old`, `Is_old`, `Use_old`, `discout_old`, `by`, `status`) VALUES
(1, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 'Pajaree', 'expire'),
(2, 100, 7777, 100, 1, 9999, 9999, 9999, 9999, 'Pajaree', 'expire'),
(3, 100, 1, 100, 1, 100, 7777, 100, 1, 'Pajaree', 'online');

-- --------------------------------------------------------

--
-- Table structure for table `myposapp_product`
--

CREATE TABLE `myposapp_product` (
  `id` int(11) NOT NULL,
  `Barcode_ID` varchar(13) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Size` varchar(45) NOT NULL,
  `Color` varchar(45) NOT NULL,
  `Type` varchar(45) NOT NULL,
  `Model` varchar(45) NOT NULL,
  `Cost` int(11) NOT NULL,
  `Price` int(11) NOT NULL,
  `VAT` int(11) NOT NULL,
  `Excluding_VAT` int(11) NOT NULL,
  `id_Promotion` int(11) NOT NULL,
  `status` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myposapp_product`
--

INSERT INTO `myposapp_product` (`id`, `Barcode_ID`, `Name`, `Size`, `Color`, `Type`, `Model`, `Cost`, `Price`, `VAT`, `Excluding_VAT`, `id_Promotion`, `status`) VALUES
(1, '1111111111111', 'Adidas', 'L', 'pink', 'all start', 'specail', 2000, 2599, 182, 2417, 2, 1),
(2, '2222222222222', 'Nike', 'L', 'black', 'all start', 'specail', 1000, 1990, 139, 1851, 3, 0),
(3, '3333333333333', 'VAN', 'Free size', 'white', 'all start', 'specail', 900, 1499, 105, 1394, 0, 1),
(4, '4444444444444', 'Nike X VAN', 'M', 'yellow', 'all start', 'specail', 3000, 4590, 321, 4269, 0, 1),
(5, '5555555555555', 'T-shirt', 'XS', 'black', 'all start', 'specail', 100, 199, 14, 185, 0, 1),
(6, '8888888888888', 'Converse', 'XL', 'pink', 'all start', 'specail', 2000, 3000, 210, 2790, 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `myposapp_product_order`
--

CREATE TABLE `myposapp_product_order` (
  `id` int(11) NOT NULL,
  `Date` date NOT NULL,
  `Product_id` int(11) DEFAULT NULL,
  `Bill_id` int(11) DEFAULT NULL,
  `Employee_id` int(11) DEFAULT NULL,
  `Quantity` int(11) DEFAULT NULL,
  `Unit_price` int(11) DEFAULT NULL,
  `Unit_Cost` int(11) DEFAULT NULL,
  `Unit_Tax` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myposapp_product_order`
--

INSERT INTO `myposapp_product_order` (`id`, `Date`, `Product_id`, `Bill_id`, `Employee_id`, `Quantity`, `Unit_price`, `Unit_Cost`, `Unit_Tax`) VALUES
(1, '2021-04-11', 1, 1, 2, 1, 2499, 2000, 175),
(2, '2021-04-11', 1, 2, 2, 2, 2499, 2000, 175),
(3, '2021-04-11', 2, 3, 2, 1, 1990, 1000, 139),
(4, '2021-04-11', 3, 3, 2, 1, 1499, 900, 105),
(5, '2021-04-11', 4, 4, 2, 1, 4590, 3000, 321),
(6, '2021-04-11', 5, 5, 2, 3, 199, 100, 14),
(9, '2021-04-11', 1, 6, 2, 1, 2499, 2000, 175),
(10, '2021-04-11', 1, 7, 2, 2, 2599, 2000, 182),
(11, '2021-04-11', 2, 7, 2, 1, 1990, 1000, 139),
(12, '2021-04-11', 1, 8, 2, 1, 2599, 2000, 182),
(13, '2021-04-11', 2, 8, 2, 1, 1990, 1000, 139),
(14, '2021-04-11', 1, 9, 2, 1, 2599, 2000, 182),
(15, '2021-04-11', 2, 9, 2, 1, 1990, 1000, 139);

-- --------------------------------------------------------

--
-- Table structure for table `myposapp_profit`
--

CREATE TABLE `myposapp_profit` (
  `id` int(11) NOT NULL,
  `January` int(11) DEFAULT NULL,
  `February` int(11) DEFAULT NULL,
  `March` int(11) DEFAULT NULL,
  `April` int(11) DEFAULT NULL,
  `May` int(11) DEFAULT NULL,
  `June` int(11) DEFAULT NULL,
  `July` int(11) DEFAULT NULL,
  `August` int(11) DEFAULT NULL,
  `September` int(11) DEFAULT NULL,
  `October` int(11) DEFAULT NULL,
  `November` int(11) DEFAULT NULL,
  `December` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myposapp_profit`
--

INSERT INTO `myposapp_profit` (`id`, `January`, `February`, `March`, `April`, `May`, `June`, `July`, `August`, `September`, `October`, `November`, `December`) VALUES
(1, 0, 0, 0, 499, 0, 0, 0, 0, 0, 0, 0, 0),
(2, 0, 0, 0, 998, 0, 0, 0, 0, 0, 0, 0, 0),
(3, 0, 0, 0, 1589, 0, 0, 0, 0, 0, 0, 0, 0),
(4, 0, 0, 0, 1590, 0, 0, 0, 0, 0, 0, 0, 0),
(5, 0, 0, 0, 297, 0, 0, 0, 0, 0, 0, 0, 0),
(6, 0, 0, 0, 499, 0, 0, 0, 0, 0, 0, 0, 0),
(7, 0, 0, 0, 2188, 0, 0, 0, 0, 0, 0, 0, 0),
(8, 0, 0, 0, 1589, 0, 0, 0, 0, 0, 0, 0, 0),
(9, 0, 0, 0, 1589, 0, 0, 0, 0, 0, 0, 0, 0),
(10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `myposapp_promotion`
--

CREATE TABLE `myposapp_promotion` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `types` varchar(100) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `apply` varchar(45) NOT NULL,
  `value` int(11) NOT NULL,
  `atlest` int(11) DEFAULT NULL,
  `by` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myposapp_promotion`
--

INSERT INTO `myposapp_promotion` (`id`, `name`, `types`, `start_date`, `end_date`, `apply`, `value`, `atlest`, `by`) VALUES
(2, 'winter', 'Buy X Get Y', '2021-03-28', '2021-04-19', '', 0, NULL, 'pajaree'),
(3, 'autumn', 'Combo Set', '2021-03-28', '2021-04-21', '', 500, NULL, 'pajaree'),
(4, 'fox', 'At least', '2021-03-28', '2021-04-20', '', 5, 1000, 'pajaree');

-- --------------------------------------------------------

--
-- Table structure for table `myposapp_promotion_member`
--

CREATE TABLE `myposapp_promotion_member` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `types` varchar(100) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `form` time(6) NOT NULL,
  `to` time(6) NOT NULL,
  `value` int(11) DEFAULT NULL,
  `atlest` int(11) DEFAULT NULL,
  `by` varchar(100) NOT NULL,
  `condition` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myposapp_promotion_member`
--

INSERT INTO `myposapp_promotion_member` (`id`, `name`, `types`, `start_date`, `end_date`, `form`, `to`, `value`, `atlest`, `by`, `condition`, `status`) VALUES
(1, 'member_promotion', 'Discount for member Persent  Off', '2021-04-13', '2021-04-21', '00:55:00.000000', '02:55:00.000000', 55555, 0, 'Pajaree', '[\'-\']', 'online'),
(2, 'ccdfdf', 'Discount for member Persent  Off', '2021-04-12', '2021-04-15', '11:55:00.000000', '00:55:00.000000', 999999, 0, 'Pajaree', '[\'-\']', 'online'),
(3, 'gggg', 'Discount for member Persent  Off', '2021-04-12', '2021-04-15', '00:57:00.000000', '01:57:00.000000', 8989898, 0, 'Pajaree', '[\'-\']', 'online'),
(4, 'ccdfdf', 'Discount for member Persent  Off', '2021-04-14', '2021-04-21', '01:58:00.000000', '01:58:00.000000', 55555, 0, 'Pajaree', '[\'-\']', 'online'),
(5, 'ggggggg', 'Discount for member Persent  Off', '2021-04-20', '2021-04-14', '11:59:00.000000', '01:59:00.000000', 55555, 0, 'Pajaree', '[\'-\']', 'online'),
(6, 'member_promotionsdsdh', 'Brithday Special Amount  Off', '2021-04-06', '2021-04-13', '00:59:00.000000', '01:59:00.000000', 55555, 56565656, 'Pajaree', 'On birthmonth', 'online'),
(7, 'mospromotion', 'Discount for member Persent  Off', '2021-04-13', '2021-04-21', '14:06:00.000000', '14:06:00.000000', 500, 0, 'Pajaree', '[\'-\']', 'online'),
(8, 'mospromotion2', 'Brithday Special Persent  Off', '2021-04-01', '2021-04-06', '14:08:00.000000', '14:08:00.000000', 10, 5000, 'Pajaree', 'On birthmonth', 'expire'),
(9, 'member_promotion3', 'Brithday Special Amount  Off', '2021-04-15', '2021-04-22', '14:09:00.000000', '15:09:00.000000', 55555, 80000, 'Pajaree', 'On birthmonth', 'online');

-- --------------------------------------------------------

--
-- Table structure for table `myposapp_sale`
--

CREATE TABLE `myposapp_sale` (
  `id` int(11) NOT NULL,
  `January` int(11) DEFAULT NULL,
  `February` int(11) DEFAULT NULL,
  `March` int(11) DEFAULT NULL,
  `April` int(11) DEFAULT NULL,
  `May` int(11) DEFAULT NULL,
  `June` int(11) DEFAULT NULL,
  `July` int(11) DEFAULT NULL,
  `August` int(11) DEFAULT NULL,
  `September` int(11) DEFAULT NULL,
  `October` int(11) DEFAULT NULL,
  `November` int(11) DEFAULT NULL,
  `December` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myposapp_sale`
--

INSERT INTO `myposapp_sale` (`id`, `January`, `February`, `March`, `April`, `May`, `June`, `July`, `August`, `September`, `October`, `November`, `December`) VALUES
(1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0),
(2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0),
(3, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0),
(4, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0),
(5, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0),
(6, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0),
(7, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0),
(8, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0),
(9, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0),
(10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `myposapp_subscription_fee`
--

CREATE TABLE `myposapp_subscription_fee` (
  `id` int(11) NOT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `old_rate` int(11) DEFAULT NULL,
  `new_rate` int(11) DEFAULT NULL,
  `start_point` int(11) DEFAULT NULL,
  `by` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myposapp_subscription_fee`
--

INSERT INTO `myposapp_subscription_fee` (`id`, `start_date`, `end_date`, `old_rate`, `new_rate`, `start_point`, `by`, `status`) VALUES
(1, '2021-04-11', '2021-04-11', 9999, 9999, 9999, 'Pajaree', 'expire'),
(2, NULL, NULL, 100, 100, 1000, 'Pajaree', 'expire'),
(3, NULL, NULL, 100, 100, 7777, 'Pajaree', 'expire'),
(4, NULL, NULL, 100, 50, 300, 'Pajaree', 'expire'),
(5, '2021-04-11', '2021-04-29', 100, 9999, 7777, 'Pajaree', 'expire'),
(6, NULL, NULL, 100, 800, 20, 'Pajaree', 'online');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `myposapp_bill`
--
ALTER TABLE `myposapp_bill`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myposapp_employee`
--
ALTER TABLE `myposapp_employee`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myposapp_history_promotion`
--
ALTER TABLE `myposapp_history_promotion`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myposapp_item_in_promotion`
--
ALTER TABLE `myposapp_item_in_promotion`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myposapp_list_product`
--
ALTER TABLE `myposapp_list_product`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myposapp_member`
--
ALTER TABLE `myposapp_member`
  ADD PRIMARY KEY (`Member_ID`);

--
-- Indexes for table `myposapp_member_point`
--
ALTER TABLE `myposapp_member_point`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myposapp_product`
--
ALTER TABLE `myposapp_product`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myposapp_product_order`
--
ALTER TABLE `myposapp_product_order`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myposapp_profit`
--
ALTER TABLE `myposapp_profit`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myposapp_promotion`
--
ALTER TABLE `myposapp_promotion`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myposapp_promotion_member`
--
ALTER TABLE `myposapp_promotion_member`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myposapp_sale`
--
ALTER TABLE `myposapp_sale`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myposapp_subscription_fee`
--
ALTER TABLE `myposapp_subscription_fee`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=81;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `myposapp_bill`
--
ALTER TABLE `myposapp_bill`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `myposapp_employee`
--
ALTER TABLE `myposapp_employee`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `myposapp_history_promotion`
--
ALTER TABLE `myposapp_history_promotion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `myposapp_item_in_promotion`
--
ALTER TABLE `myposapp_item_in_promotion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `myposapp_list_product`
--
ALTER TABLE `myposapp_list_product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `myposapp_member_point`
--
ALTER TABLE `myposapp_member_point`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `myposapp_product`
--
ALTER TABLE `myposapp_product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `myposapp_product_order`
--
ALTER TABLE `myposapp_product_order`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `myposapp_profit`
--
ALTER TABLE `myposapp_profit`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `myposapp_promotion`
--
ALTER TABLE `myposapp_promotion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `myposapp_promotion_member`
--
ALTER TABLE `myposapp_promotion_member`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `myposapp_sale`
--
ALTER TABLE `myposapp_sale`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `myposapp_subscription_fee`
--
ALTER TABLE `myposapp_subscription_fee`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
