# IS601 - Final Project
## Project by Eric Brokerick and Ricardo Nunes

### This project is for a simple Contact Tracing Web-App. It will allow users to "check-in" to a location with their Name, Phone Number, and other optional information.

  - The user data provided along with check in time and a unique session ID will be stored in a SQL database. 

  - On the Check Out Page, the User's Cookie is used to successful log the time the user hit check out if the system and attach it to their check-in record in the database, while also deleting the cookie from the User's Device and allowing them to check in again. 
  
  - The Last page allow a user to set an arrival time and Departure time and query the database which will return a list of individuals that were checked in within that timeframe. This would be used in the case of someone testing positive COVID and a list of possible people who they may have come in contact with needs to be compiled. 