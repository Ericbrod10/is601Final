# IS601 - Final Project
## Project by Eric Broderick and Ricardo Nunes

### This project is for a simple Contact Tracing Web-App. It will allow users to "check-in" to a location with their Name, Phone Number, and other optional information.

  - The user data provided along with check-in time as well as a unique session ID will be stored in an SQL database. 

  - On the Check Out Page, the User's Cookie (SessionID) is used to successful log the time a user hits check out and 
    uses the ID it to attach it to their check-in record in the database. This also deletes the cookie from the User's 
    Device and allows them to check in again. 
  
  - The Last page, allows a user to set an Arrival and Departure times which queries the database and will return a list
    of individuals that were checked in within that timeframe. This would be used in the case of someone testing 
    positive COVID-19 as well as a list of possible people who they may have come in contact with needs to be compiled. 
    
## [Install and Run Instructions](./install.md)

## [Runtime Feature Examples](./examples.md)
