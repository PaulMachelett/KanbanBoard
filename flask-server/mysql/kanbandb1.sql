-- -----------------------------------------------------
-- Schema KanbanDB
-- -----------------------------------------------------
DROP DATABASE IF EXISTS KanbanDB;
CREATE DATABASE IF NOT EXISTS KanbanDB;
CREATE SCHEMA IF NOT EXISTS `KanbanDB` DEFAULT CHARACTER SET utf8 ;
USE `KanbanDB` ;

CREATE DATABASE  IF NOT EXISTS `KanbanDB` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `KanbanDB`;

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


  
-- -----------------------------------------------------
-- Table `KanbanDB`.`Person`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Person` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nickname` VARCHAR(45) NULL,
  `firstname` VARCHAR(150) NULL,
  `lastname` VARCHAR(100) NULL,
  `googleid` VARCHAR(150) NULL,
  `email` VARCHAR(100) NULL,
  PRIMARY KEY (`id`));

-- -----------------------------------------------------
-- Table `KanbanDB`.`Project`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Project` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `start_date` DATETIME NULL,
  `end_date` DATETIME NULL,
  `name` VARCHAR(100) NULL,
  PRIMARY KEY (`id`));

  -- -----------------------------------------------------
-- Table `KanbanDB`.`Phase`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Phase` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `projectid` INT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`projectid`) REFERENCES Project(`id`) ON DELETE CASCADE );

-- -----------------------------------------------------
-- Table `KanbanDB`.`Kanbancard`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Kanbancard` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(100) NULL,
  `content` VARCHAR(45) NULL,
  `phaseid` INT NULL,
  `start_date` DATETIME NULL,
  `end_date` DATETIME NULL,
  `creator` INT NULL,
  `assigned_person` INT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`phaseid`) REFERENCES Phase(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`creator`) REFERENCES Person(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`assigned_person`) REFERENCES Person(`id`) ON DELETE CASCADE);

-- -----------------------------------------------------
-- Table `KanbanDB`.`Comment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Comment` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `creator` INT NULL,
  `content` VARCHAR(45) NULL,
  `cardid` INT NULL,
  `creation_date` DATETIME NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`creator`) REFERENCES Person (`id`),
  FOREIGN KEY (`cardid`) REFERENCES Kanbancard (`id`) ON DELETE CASCADE);


-- -----------------------------------------------------
-- Table `KanbanDB`.`Project Participation`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Project_Participation` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `projectid` INT NULL,
  `personid` INT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`projectid`) REFERENCES Project(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`personid`) REFERENCES Person(`id`) ON DELETE CASCADE);



-- -----------------------------------------------------
-- Auto Increment
-- -----------------------------------------------------
ALTER TABLE `Person` AUTO_INCREMENT = 1;
ALTER TABLE `Phase` AUTO_INCREMENT = 1;
ALTER TABLE `Kanbancard` AUTO_INCREMENT = 1;
ALTER TABLE `Project` AUTO_INCREMENT = 1;
ALTER TABLE `Comment` AUTO_INCREMENT = 1;
ALTER TABLE `Project_Participation` AUTO_INCREMENT = 1;


-- -----------------------------------------------------
-- Person
-- -----------------------------------------------------
INSERT INTO `Person` (nickname, firstname, lastname, googleid, email)
VALUES('S200', 'Sarah', 'Müller', '116340648124815495610', 'sarahmueller@yahoo.com');
INSERT INTO `Person` (nickname, firstname, lastname, googleid, email)
VALUES('Ro209', 'Robert', 'Senk', '23634061812457054952398', 'robertsenk@web.de');
INSERT INTO `Person` (nickname, firstname, lastname, googleid, email)
VALUES('Dani_S', 'Daniel', 'Fischer', '44325173482823', 'danielfischer@yahoo.com');

-- -----------------------------------------------------
-- Project
-- -----------------------------------------------------
INSERT INTO `Project` (start_date, end_date, name)
VALUES('2023-11-20 13:54:17', '2023-11-22 13:54:17', 'TestProject');

-- -----------------------------------------------------
-- Phase
-- -----------------------------------------------------
INSERT INTO `Phase` (name, projectid)
VALUES('ToDo', '1');

-- -----------------------------------------------------
-- Kanbancard
-- -----------------------------------------------------
INSERT INTO `Kanbancard` (title, content, phaseid, start_date, end_date, creator, assigned_person)
VALUES('Sopra bestehen', 'Dieses Jahr muss das Sopra bestanden werden', '1', '2023-11-20 13:54:17', '2023-11-22 13:54:17', '2', '1');

-- -----------------------------------------------------
-- Comment
-- -----------------------------------------------------
INSERT INTO `Comment` (creator, content, cardid, creation_date)
VALUES('3', 'Inhalt eines Kommentars', '1','2023-11-20 13:54:17');

-- -----------------------------------------------------
-- ProjectParticipation
-- -----------------------------------------------------
INSERT INTO `Project_Participation` (projectid, personid)
VALUES('1', '3');


