CREATE DATABASE  IF NOT EXISTS `ispc_lawdb` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `ispc_lawdb`;
-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: ispc_lawdb
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
-- Table structure for table `jurisdiccion`
--

DROP TABLE IF EXISTS `jurisdiccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jurisdiccion` (
  `idJurisdiccion` int NOT NULL AUTO_INCREMENT,
  `Jurisdiccion` varchar(100) NOT NULL,
  `Organo Legislativo` varchar(100) NOT NULL,
  PRIMARY KEY (`idJurisdiccion`),
  UNIQUE KEY `Organo Legislativo_UNIQUE` (`Organo Legislativo`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jurisdiccion`
--

LOCK TABLES `jurisdiccion` WRITE;
/*!40000 ALTER TABLE `jurisdiccion` DISABLE KEYS */;
INSERT INTO `jurisdiccion` VALUES (1,'Nacional','Congreso de la Nación'),(2,'Provincial','Legislatura de Córdoba');
/*!40000 ALTER TABLE `jurisdiccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ley`
--

DROP TABLE IF EXISTS `ley`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ley` (
  `Nro. Registro` int NOT NULL AUTO_INCREMENT,
  `Tipo de normativa` varchar(45) NOT NULL,
  `Nro. Normativa` int NOT NULL,
  `Fecha` date NOT NULL,
  `Descripción` varchar(450) NOT NULL,
  `Categoria` varchar(45) NOT NULL,
  `Jurisdiccion_idJurisdiccion` int NOT NULL,
  PRIMARY KEY (`Nro. Registro`,`Jurisdiccion_idJurisdiccion`),
  KEY `fk_Ley_Jurisdiccion1_idx` (`Jurisdiccion_idJurisdiccion`),
  CONSTRAINT `fk_Ley_Jurisdiccion1` FOREIGN KEY (`Jurisdiccion_idJurisdiccion`) REFERENCES `jurisdiccion` (`idJurisdiccion`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ley`
--

LOCK TABLES `ley` WRITE;
/*!40000 ALTER TABLE `ley` DISABLE KEYS */;
INSERT INTO `ley` VALUES (1,'Ley',20744,'1976-05-13','La Ley de Contratos de Trabajo Es la norma legal \n	que regula las relaciones laborales de los \n	trabajadores que se encuentran bajo relación de \n	dependencia, excluyendo a los empleados de la \n	Administración Pública.','Laboral',1),(2,'Ley',14250,'1953-09-29','Convenciones colectivas de trabajo La ley de \n	convenciones colectivas de trabajo tiene el fin de \n	regular la actividad de las asociaciones \n	profesionales de empleadores, empleador o \n	grupo de empleadores, asociaciones \n	profesionales de trabajadores con personalidad \n	gremial y asociaciones profesionales de \n	trabajadores del Estado.','Laboral',1),(3,'Ley',23551,'1988-03-23','Asociaciones sindicales Esta ley dispone que \n	todos trabajadores tienen derecho a constituir \n	libremente y sin necesidad de autorización previa \n	asociaciones sindicales, a afiliarse, no afiliarse o \n	desafiliarse, a reunirse y desarrollar actividades \n	sindicales, elegir libremente a sus representantes, \n	ser elegidos y postular candidatos.','Laboral',1),(4,'Ley',23592,'1988-08-03','La Ley de Actos Discriminatorios, tipifica como \n	delitos un conjunto de conductas que tienen por \n	finalidad, en primer lugar, la discriminación racial \n	o religiosa y, en segundo, la persecución o el odio \n	fundado en motivos de raza, religión, nacionalidad \n	o ideas políticas.','Laboral',1),(5,'Ley',27555,'2020-08-14','Régimen del teletrabajo - La persona que trabaja \n	bajo la modalidad de teletrabajo tendrá derecho a \n	no ser contactada y a desconectarse de los \n	dispositivos digitales y/o tecnologías de la \n	información y comunicación, fuera de su jornada \n	laboral y durante los períodos de licencias. No \n	podrá ser sancionada por hacer uso de este \n	derecho.','Laboral',1),(6,'Ley',24241,'1993-09-23','Sistema integrado de jubilaciones y pensiones - \nestablece los índices de movilidad de las \nprestaciones jubilatorias y de las Prestaciones del \nRégimen Previsional Público.','Laboral',1),(7,'Ley',24557,'1995-10-04','Ley de riesgos del trabajo - propone en su marco \nteórico, la prevención de los accidentes de trabajo \ny enfermedades profesionales, además de \nasegurar al trabajador adecuada atención médica \nen forma oportuna, procurando su \nrestablecimiento','Laboral',1),(8,'Ley',19550,'2015-08-01','Ley Sociedades Comerciales - establece los \ndistintos tipos societarios admitidos en el nuevo \nCódigo Civil y Comercial de la Nación. establece \nque habrá sociedad si una o más personas en \nforma organizada conforme a uno de los tipos \nprevistos en esta ley, se obligan a realizar aportes \npara aplicarlos a la producción o intercambio de \nbienes o servicios, participando de los beneficios \ny soportando las pérdidas.','Civil',1),(9,'Ley',7642,'1987-11-25','Establece la denominación y domicilio del \nConsejo Profesional de Ciencias Informáticas de \nla Provincia de Córdoba.\nEnumera los objetivos de la asociación, que \nincluyen agrupar a los profesionales de Ciencias \nInformáticas, promover su desarrollo, brindar \napoyo y asesoramiento, establecer vínculos con \notras entidades y contribuir a la formación y \nactualización profesional.','Laboral',2);
/*!40000 ALTER TABLE `ley` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `palabras`
--

DROP TABLE IF EXISTS `palabras`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `palabras` (
  `idPalabras` int NOT NULL AUTO_INCREMENT,
  `Palabras clave` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`idPalabras`),
  UNIQUE KEY `Palabras clave_UNIQUE` (`Palabras clave`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `palabras`
--

LOCK TABLES `palabras` WRITE;
/*!40000 ALTER TABLE `palabras` DISABLE KEYS */;
INSERT INTO `palabras` VALUES (30,'acciones'),(34,'accionista'),(19,'administradoras de Fondos de jubilaciones y pensiones'),(21,'afiliado'),(9,'asociación'),(23,'beneficiario'),(31,'capital'),(7,'colectiva'),(2,'contrato'),(8,'convencion'),(36,'daño permanente'),(5,'derecho'),(33,'director'),(12,'discriminatorio'),(4,'empleador'),(39,'entidad'),(11,'gremial'),(26,'incapacidad'),(38,'informatica'),(24,'invalidez'),(18,'jornada'),(22,'jubilaciones'),(35,'laboral'),(37,'matriculado'),(16,'modalidad'),(15,'nacionalidad'),(6,'obligación'),(20,'prestacion'),(25,'prestaciones'),(40,'profesional'),(13,'raza'),(14,'religion'),(32,'resposabilidad'),(27,'riesgo'),(10,'sindicales'),(28,'sociedad'),(29,'socio'),(17,'teletrabajo'),(3,'trabajador'),(1,'trabajo');
/*!40000 ALTER TABLE `palabras` ENABLE KEYS */;
UNLOCK TABLES;

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
  CONSTRAINT `fk_Palabras_has_Ley_Ley1` FOREIGN KEY (`Ley_Nro. Registro`) REFERENCES `ley` (`Nro. Registro`) ON DELETE CASCADE,
  CONSTRAINT `fk_Palabras_has_Ley_Palabras` FOREIGN KEY (`Palabras_idPalabras`) REFERENCES `palabras` (`idPalabras`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `palabras_ley`
--

LOCK TABLES `palabras_ley` WRITE;
/*!40000 ALTER TABLE `palabras_ley` DISABLE KEYS */;
INSERT INTO `palabras_ley` VALUES (1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(1,2),(3,2),(4,2),(7,2),(8,2),(1,3),(3,3),(4,3),(7,3),(8,3),(9,3),(10,3),(11,3),(12,4),(13,4),(14,4),(15,4),(3,5),(4,5),(5,5),(16,5),(17,5),(18,5),(19,6),(20,6),(21,6),(22,6),(23,6),(24,6),(3,7),(4,7),(25,7),(26,7),(27,7),(36,7),(2,8),(28,8),(29,8),(30,8),(31,8),(32,8),(33,8),(34,8),(37,9),(38,9),(39,9),(40,9);
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

-- Dump completed on 2023-06-22 16:26:52
