-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema lancasters_schema
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `lancasters_schema` ;

-- -----------------------------------------------------
-- Schema lancasters_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `lancasters_schema` DEFAULT CHARACTER SET utf8 ;
USE `lancasters_schema` ;

-- -----------------------------------------------------
-- Table `lancasters_schema`.`characters`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `lancasters_schema`.`characters` ;

CREATE TABLE IF NOT EXISTS `lancasters_schema`.`characters` (
  `idcharacters` INT NOT NULL AUTO_INCREMENT,
  `login_password` VARCHAR(255) NOT NULL,
  `login_username` VARCHAR(45) NOT NULL,
  `role` VARCHAR(255) NOT NULL,
  `relationship` TEXT(1000) NULL,
  `potential_motive` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`idcharacters`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lancasters_schema`.`storyitems`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `lancasters_schema`.`storyitems` ;

CREATE TABLE IF NOT EXISTS `lancasters_schema`.`storyitems` (
  `idstoryitems` INT NOT NULL,
  `story_title` VARCHAR(255) NULL,
  `description` VARCHAR(255) NULL,
  `lookup_key` VARCHAR(255) NULL,
  `storyitemscol` VARCHAR(45) NULL,
  `item_content` TEXT(1000) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`idstoryitems`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lancasters_schema`.`characters_has_storyitems`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `lancasters_schema`.`characters_has_storyitems` ;

CREATE TABLE IF NOT EXISTS `lancasters_schema`.`characters_has_storyitems` (
  `characters_idcharacters` INT NOT NULL,
  `storyitems_idstoryitems` INT NOT NULL,
  PRIMARY KEY (`characters_idcharacters`, `storyitems_idstoryitems`),
  INDEX `fk_characters_has_storyitems_storyitems1_idx` (`storyitems_idstoryitems` ASC) VISIBLE,
  INDEX `fk_characters_has_storyitems_characters_idx` (`characters_idcharacters` ASC) VISIBLE,
  CONSTRAINT `fk_characters_has_storyitems_characters`
    FOREIGN KEY (`characters_idcharacters`)
    REFERENCES `lancasters_schema`.`characters` (`idcharacters`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_characters_has_storyitems_storyitems1`
    FOREIGN KEY (`storyitems_idstoryitems`)
    REFERENCES `lancasters_schema`.`storyitems` (`idstoryitems`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
