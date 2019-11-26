-- MySQL dump 10.13  Distrib 5.7.28, for Linux (x86_64)
--
-- Host: localhost    Database: public
-- ------------------------------------------------------
-- Server version	5.7.28-0ubuntu0.18.04.4

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `business`
--

DROP TABLE IF EXISTS `business`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `business` (
  `businessid` int(11) NOT NULL AUTO_INCREMENT,
  `businessname` varchar(32) NOT NULL,
  `busdescription` varchar(200) NOT NULL,
  PRIMARY KEY (`businessid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `business`
--

LOCK TABLES `business` WRITE;
/*!40000 ALTER TABLE `business` DISABLE KEYS */;
/*!40000 ALTER TABLE `business` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `car_insurance`
--

DROP TABLE IF EXISTS `car_insurance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `car_insurance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `coverage` varchar(20) NOT NULL,
  `duration` varchar(20) NOT NULL,
  `price` varchar(200) NOT NULL,
  `price_range` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car_insurance`
--

LOCK TABLES `car_insurance` WRITE;
/*!40000 ALTER TABLE `car_insurance` DISABLE KEYS */;
INSERT INTO `car_insurance` VALUES (5,'glass insurance','full','3 years','13000','cheap'),(6,'glass insurance','full','5 years','23000','cheap'),(7,'glass insurance','full','10 years','23000','cheap'),(8,'glass insurance','partial','3 years','10000','cheap'),(9,'glass insurance','partial','5 years','18000','cheap'),(10,'glass insurance','partial','10 years','28000','cheap'),(11,'theft insurance','partial','3 years','5000','cheap'),(12,'theft insurance','partial','5 years','8000','cheap'),(13,'theft insurance','partial','10 years','10000','cheap'),(14,'theft insurance','full','3 years','10500','cheap'),(15,'theft insurance','full','5 years','14500','cheap'),(16,'theft insurance','full','10 years','19500','cheap'),(17,'engine insurance','full','3 years','20000','medium'),(18,'engine insurance','full','5 years','24000','medium'),(19,'engine insurance','full','10 years','34000','medium'),(20,'engine insurance','partial','3 years','18000','medium'),(21,'engine insurance','partial','5 years','23000','medium'),(22,'engine insurance','partial','10 years','30000','medium'),(23,'traffic insurance','full','3 years','32000','expensive'),(24,'traffic insurance','full','5 years','42000','expensive'),(25,'traffic insurance','full','10 years','62000','expensive'),(26,'traffic insurance','partial','10 years','60000','expensive'),(27,'traffic insurance','partial','5 years','50000','expensive'),(28,'traffic insurance','partial','3 years','30000','expensive');
/*!40000 ALTER TABLE `car_insurance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `claim`
--

DROP TABLE IF EXISTS `claim`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `claim` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `insuranceid` int(11) NOT NULL,
  `userid` int(11) NOT NULL,
  `description` varchar(120) NOT NULL,
  `date` varchar(40) NOT NULL,
  `state` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `claim`
--

LOCK TABLES `claim` WRITE;
/*!40000 ALTER TABLE `claim` DISABLE KEYS */;
INSERT INTO `claim` VALUES (1,2,1,'my car is broken','Sun Nov 24 14:46:04 2019','Processing'),(2,4,1,'my car is damaged','Sun Nov 24 15:47:14 2019','Processing'),(3,6,1,'my car broken','Sun Nov 24 23:12:16 2019','Processing'),(4,5,8,'my car is damaged','Sun Nov 24 23:32:31 2019','Processing');
/*!40000 ALTER TABLE `claim` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company` (
  `companyid` int(11) NOT NULL AUTO_INCREMENT,
  `companyname` varchar(32) NOT NULL,
  `tototalvalue` tinytext NOT NULL,
  PRIMARY KEY (`companyid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company`
--

LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_business`
--

DROP TABLE IF EXISTS `company_business`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company_business` (
  `company_businessid` int(11) NOT NULL AUTO_INCREMENT,
  `companyid` int(11) DEFAULT NULL,
  `businessid` int(11) DEFAULT NULL,
  PRIMARY KEY (`company_businessid`),
  KEY `companyid` (`companyid`),
  KEY `businessid` (`businessid`),
  CONSTRAINT `company_business_ibfk_1` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`),
  CONSTRAINT `company_business_ibfk_2` FOREIGN KEY (`businessid`) REFERENCES `business` (`businessid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_business`
--

LOCK TABLES `company_business` WRITE;
/*!40000 ALTER TABLE `company_business` DISABLE KEYS */;
/*!40000 ALTER TABLE `company_business` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_insurance`
--

DROP TABLE IF EXISTS `company_insurance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company_insurance` (
  `company_insuranceid` int(11) NOT NULL AUTO_INCREMENT,
  `companyid` int(11) DEFAULT NULL,
  `insuranceid` int(11) DEFAULT NULL,
  PRIMARY KEY (`company_insuranceid`),
  KEY `companyid` (`companyid`),
  KEY `insuranceid` (`insuranceid`),
  CONSTRAINT `company_insurance_ibfk_1` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`),
  CONSTRAINT `company_insurance_ibfk_2` FOREIGN KEY (`insuranceid`) REFERENCES `insurance` (`insuranceid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_insurance`
--

LOCK TABLES `company_insurance` WRITE;
/*!40000 ALTER TABLE `company_insurance` DISABLE KEYS */;
/*!40000 ALTER TABLE `company_insurance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_user`
--

DROP TABLE IF EXISTS `company_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company_user` (
  `company_userid` int(11) NOT NULL AUTO_INCREMENT,
  `companyid` int(11) DEFAULT NULL,
  `userid` int(11) DEFAULT NULL,
  PRIMARY KEY (`company_userid`),
  KEY `companyid` (`companyid`),
  KEY `userid` (`userid`),
  CONSTRAINT `company_user_ibfk_1` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`),
  CONSTRAINT `company_user_ibfk_2` FOREIGN KEY (`userid`) REFERENCES `user` (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_user`
--

LOCK TABLES `company_user` WRITE;
/*!40000 ALTER TABLE `company_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `company_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `description`
--

DROP TABLE IF EXISTS `description`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `description` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `description` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `description`
--

LOCK TABLES `description` WRITE;
/*!40000 ALTER TABLE `description` DISABLE KEYS */;
INSERT INTO `description` VALUES (1,'glass insurance','This is a popular insurance. Covers all the glass on your car'),(2,'theft insurance','Just feel free to park your car everywhere. If your car is stolen or damaged by the thief, you are able to claim and get your money back'),(3,'engine insurance','This insurance is popular for sports cars which has an advanced engine.'),(4,'traffic insurance','This insurance covers all kinds of traffic accidents whenever you are at fault or not.');
/*!40000 ALTER TABLE `description` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detail_insurance`
--

DROP TABLE IF EXISTS `detail_insurance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `detail_insurance` (
  `insuranceid` int(11) NOT NULL AUTO_INCREMENT,
  `insurance` int(11) NOT NULL,
  `userid` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `coverage` varchar(20) NOT NULL,
  `duration` varchar(20) NOT NULL,
  `price` varchar(200) NOT NULL,
  `price_range` varchar(200) NOT NULL,
  `date` varchar(40) NOT NULL,
  PRIMARY KEY (`insuranceid`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detail_insurance`
--

LOCK TABLES `detail_insurance` WRITE;
/*!40000 ALTER TABLE `detail_insurance` DISABLE KEYS */;
INSERT INTO `detail_insurance` VALUES (1,2,1,'theft insurance','full','5 years','12000 dollars','cheap','Sun Nov 24 09:18:44 2019'),(2,20,1,'engine insurance','partial','3 years','18000','medium','Sun Nov 24 13:20:33 2019'),(3,6,2,'glass insurance','full','5 years','23000','cheap','Sun Nov 24 13:50:56 2019'),(4,23,1,'traffic insurance','full','3 years','32000','expensive','Sun Nov 24 15:46:55 2019'),(5,9,1,'glass insurance','partial','5 years','18000','cheap','Sun Nov 24 15:47:41 2019'),(6,5,1,'glass insurance','full','3 years','13000','cheap','Sun Nov 24 23:11:58 2019'),(7,5,8,'glass insurance','full','3 years','13000','cheap','Sun Nov 24 23:30:59 2019');
/*!40000 ALTER TABLE `detail_insurance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `insurance`
--

DROP TABLE IF EXISTS `insurance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `insurance` (
  `insuranceid` int(11) NOT NULL AUTO_INCREMENT,
  `insurancename` varchar(32) NOT NULL,
  `insdescription` varchar(200) NOT NULL,
  PRIMARY KEY (`insuranceid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `insurance`
--

LOCK TABLES `insurance` WRITE;
/*!40000 ALTER TABLE `insurance` DISABLE KEYS */;
/*!40000 ALTER TABLE `insurance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role` (
  `roleid` int(11) NOT NULL AUTO_INCREMENT,
  `rolename` varchar(32) NOT NULL,
  PRIMARY KEY (`roleid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `userid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `email` varchar(32) NOT NULL,
  `birthday` varchar(32) NOT NULL,
  `gender` varchar(32) NOT NULL,
  `telephone` varchar(32) NOT NULL,
  `pwd` varchar(32) NOT NULL,
  `image` varchar(120) NOT NULL,
  `occupation` varchar(120) NOT NULL,
  `age` varchar(120) NOT NULL,
  `car_model` varchar(120) NOT NULL,
  `prev_accidents` varchar(120) NOT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'A','745514009@qq.com','1987-12-30','1','0452641297','1','None','commercial_driver','','corvette_c','1'),(2,'B','745514009@qq.com','2000-01-01','2','0452641297','1','None','student','','mecedes_benz_e','0'),(3,'C','745514009@qq.com','1980-01-01','1','0452641297','1','None','engineer','','bmw_e','10'),(4,'D','745514009@qq.com','1995-09-07','2','0452641297','1','None','cashier','','bmw_e','3'),(5,'E','745514009@qq.com','2010-01-01','2','0452641297','1','None','engineer','','ford_f','0'),(6,'HFR','rhf0410@gmail.com','1995-04-10','1','0452641297','12345','None','Student','25','Toyota Corolla','1'),(7,'Clin','1217597039@qq.com','2019-11-05','1','0416499999','1','None','Commercial Driver','1','BMW E','1'),(8,'Ou','909088543kirby@gmail.com','1995-01-01','2','0416499999','1234','None','Commercial Driver','25','Mercedes Benz E','1');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-11-26  1:05:46
