CREATE DATABASE LocalAid;

USE LocalAid;

CREATE TABLE tasks
(
	TaskID INT PRIMARY KEY AUTO_INCREMENT,
    Title VARCHAR(255) NOT NULL,
    Description TEXT,
    Category VARCHAR(100),
    Location VARCHAR(255)
    
);