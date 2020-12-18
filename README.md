# IS601 - Final Project
## Project by Eric Broderick and Ricardo Nunes

### This project is for a simple Contact Tracing Web-App. It will allow users to "check-in" to a location with their Name, Phone Number, and other optional information.

  - On the Check In Page,the user data provided along with check-in time as well as a unique session(CookieID) ID will be stored in an SQL database. If a user has already check-in (has a cookie on the device) then they will be show a message saying they have already checked-in and can not check in again without checking out first. They will also be show the record of their last check-in which is pulled from the database using their CookieID. 

  - On the Check Out Page, the User's Cookie (SessionID) is used to successful log the time a user hits check out and 
    uses the ID it to attach it to their check-in record in the database. If a user has not checked-in (does not have a cookie local saved) then they would not be shown the check out button on the checkout page. This also deletes the cookie from the User's Device and allows them to check in again. 
  
  - The Last page, allows a user to set an Arrival and Departure date and times which queries the database and will return a list
    of individuals that were checked in within that timeframe. This would be used in the case of someone testing 
    positive COVID-19 as a list of possible people who they may have come in contact with needs to be compiled. 
    
## [Install and Run Instructions](./install.md)

## [Runtime Feature Examples](./examples.md)
