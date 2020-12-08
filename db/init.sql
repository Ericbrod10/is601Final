CREATE DATABASE zillowData;
use zillowData;


CREATE TABLE IF NOT EXISTS zillow (
    'id' int AUTO_INCREMENT,
    'FirstName' varchar(255),
    'LastName' varchar(255),
    'PhoneNumber' varchar(255),
    'ReasonForVisit' varchar(255),
    'LoginCookieID' varchar(255),
    'CheckInTime' TIMESTAMP,
    'CheckOutTime' TIMESTAMP,
    PRIMARY KEY (`id`)
);