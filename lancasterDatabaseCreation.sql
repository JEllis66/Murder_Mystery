-- This file essentially drops the database and created it again from scratch. decent for a fresh start and to be able to see the tables without having to edit them;

DROP DATABASE IF EXISTS lancaster_theater;

CREATE DATABASE lancaster_theater;

USE lancaster_theater;

-- dropping the table if i forgot to drop it
DROP TABLE IF EXISTS named_Character;

/*

named_Character represents ANY person involved in the story in any way, 
whether or not they are played by a player, they are an NPC, 
or even if they are just a person who is mentioned in passing but never is present in the house

*/

CREATE TABLE named_Character (
	characterID SMALLINT NOT NULL AUTO_INCREMENT,
    firstName VARCHAR(20) NOT NULL,
    lastName VARCHAR(20) NOT NULL,
    userName VARCHAR(20), -- can be null if the character is not a player
    passCode VARCHAR(20), -- also can be null if the character is not a player
    isPlayerCharacter BOOL NOT NULL, -- 1 if the player is a PC, if 1 they will have a username and passcode
    isNPC BOOL NOT NULL, -- 1 if they are an NPC, examples are Dan, Jamie, Tyler (jerry) and Ashley (cop). some will have a user name and passcode
    isInHouse BOOL NOT NULL, -- if this is 0, it is a character mentioned but not present, eg Baron Lancaster (Jerry's Dad)
    PRIMARY KEY (characterID)
    );
    
DROP TABLE IF EXISTS story_Item; -- same as previous table
/*
story_Item represents anything that can be looked up in the app. 
Some of them are public (meaning everyone can see it), 
others will require some kind of code or search to find.
All of that should be indicated in this table
*/

CREATE TABLE story_Item (
	itemID SMALLINT NOT NULL AUTO_INCREMENT,
    itemName VARCHAR(20), -- should be a short name
    itemDescription VARCHAR(1000), -- backend only descriptor for the item.
    category VARCHAR(20), -- eg general person descriptor, hidden item, character briefing
    howToFind VARCHAR(200), -- backend description for how to find the item itself
    appTab VARCHAR(20), -- page on the app on which to search to find this item eg party attendees, item info, interview transcript. some items should be searchable on multiple tabs (how to configure?)
    findTerm VARCHAR(20), -- phrase that needs to be typed in order to bring up the item (how should we configure this if we want there to be multiple possible search terms?)
    PRIMARY KEY (itemID)
    );


SELECT * FROM named_character;