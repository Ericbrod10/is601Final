CREATE DATABASE CheckInData;
use CheckInData;


CREATE TABLE IF NOT EXISTS LogTable (
    id int AUTO_INCREMENT,
    FirstName varchar(255),
    LastName varchar(255),
    PhoneNumber varchar(255),
    ReasonForVisit varchar(255),
    LoginCookieID varchar(255),
    CheckInTime DATETIME,
    CheckOutTime DATETIME,
    PRIMARY KEY (id)
);

INSERT INTO LogTable VALUES
    (1 ,'Eric', 'Lroderick', '732-555-5555','Shopping','gfhjdsghjfdbhjdsf', NULL, NULL),
    (2 ,'Eric', 'Broderick', '732-555-5555','Shopping','gfhjdsghjfdbhjdsf', NULL, NULL),
    (3 ,'Eric', 'Mooderick', '732-555-5555','Shopping','gfhjdsghjfdbhjdsf', NULL, NULL);