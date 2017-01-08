-- MySQL dump 10.13  Distrib 5.7.16, for Linux (x86_64)
--
-- Host: us-cdbr-azure-central-a.cloudapp.net    Database: corelogic
-- ------------------------------------------------------
-- Server version	5.5.45-log

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
-- Table structure for table `houses`
--

DROP TABLE IF EXISTS `houses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `houses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fips_code` text,
  `formatted_apn` text,
  `p_id_iris_frmtd` text,
  `census_tract` text,
  `block_number` text,
  `lot_number` text,
  `house_range` text,
  `township` text,
  `section` text,
  `quarter_section` text,
  `land_use` text,
  `municipality_name` text,
  `subdivision_tract_number` text,
  `subdivision_plat_book` text,
  `subdivision_plat_page` text,
  `parcel_level_latitude` text,
  `parcel_level_longitude` text,
  `situs_house_number_prefix` text,
  `sit_house_number` text,
  `sit_house_number_2` text,
  `situs_house_number_suffix` text,
  `situs_direction` text,
  `situs_street_name` text,
  `situs_quadrant` text,
  `situs_mode` text,
  `sit_unit_number` text,
  `situs_city` text,
  `sit_state` text,
  `situs_zip_code` text,
  `situs_carrier_code` text,
  `front_footage` text,
  `depth_footage` text,
  `acres` text,
  `land_square_footage` text,
  `universal_building_square_feet` text,
  `building_square_feet_ind` text,
  `building_square_feet` text,
  `living_square_feet` text,
  `ground_floor_square_feet` text,
  `gross_square_feet` text,
  `adjusted_gross_square_feet` text,
  `basement_square_feet` text,
  `garage_parking_squarefeet` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `houses_id_uindex` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `houses`
--

LOCK TABLES `houses` WRITE;
/*!40000 ALTER TABLE `houses` DISABLE KEYS */;
/*!40000 ALTER TABLE `houses` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-01-07 17:00:05
