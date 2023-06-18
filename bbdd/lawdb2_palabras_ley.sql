-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: lawdb2
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `palabras_ley`
--

DROP TABLE IF EXISTS `palabras_ley`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `palabras_ley` (
  `Palabras_idPalabras` int NOT NULL AUTO_INCREMENT,
  `Ley_Nro. Registro` int NOT NULL,
  PRIMARY KEY (`Palabras_idPalabras`,`Ley_Nro. Registro`),
  KEY `fk_Palabras_has_Ley_Ley1_idx` (`Ley_Nro. Registro`),
  KEY `fk_Palabras_has_Ley_Palabras_idx` (`Palabras_idPalabras`),
  CONSTRAINT `fk_Palabras_has_Ley_Ley1` FOREIGN KEY (`Ley_Nro. Registro`) REFERENCES `ley` (`Nro. Registro`),
  CONSTRAINT `fk_Palabras_has_Ley_Palabras` FOREIGN KEY (`Palabras_idPalabras`) REFERENCES `palabras` (`idPalabras`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `palabras_ley`
--

LOCK TABLES `palabras_ley` WRITE;
/*!40000 ALTER TABLE `palabras_ley` DISABLE KEYS */;
/*!40000 ALTER TABLE `palabras_ley` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-17 20:20:05
