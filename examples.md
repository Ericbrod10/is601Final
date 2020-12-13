## Home Page
Below is the homepage for the app when it is accessed. There is a button that directs you to the check-in and check-out pages.
There is also a navbar across the top to aid with navigation.   
![webAppHome](./screenshots/homePage.png)
## New Check-in Page and function
Below is the check-in page. Users must enter their Name, Phone Number, and reason for the visit.
![checkInPage](./screenshots/newCheckInEntry.png)
Below you can see the successful POST command from the Docker runtime window.
![checkInPost](./screenshots/newCheckInPost.png)
SQL database view before the check-in in the example is executed.
![checkInBefore](./screenshots/newCheckInBefore.png)
SQL database view after the check-in above is executed and posted.
![checkInAfter](./screenshots/newCheckInAfter.png)
If a user attempts to navigate to the check-in page again before checking out (i.e. has an active cookie) they will be met with the following notice:
![checkInValidation](./screenshots/newCheckInValidation.png)
## Check-out Page and function
Below is the simple check-out page. 
![checkOutPage](./screenshots/newCheckOut.png)
Below you can see the successful POST command from the Docker runtime window.
![checkOutPost](./screenshots/newCheckOutPost.PNG)
SQL database view before the check-out in the example is executed.
![checkOutBefore](./screenshots/newCheckOutBefore.png)
SQL database view after the check-out above is executed and posted.
![checkOutAfter](./screenshots/newCheckOutAfter.png)
## Search Page and function
Below is the search page. Users must enter a date as well as time range. There is a calendar available to the user to aid with proper selection. 
![searchPage](./screenshots/searchEntry.png)
Below you can see the successful GET and POST command from the Docker runtime window.
![searchPost](./screenshots/searchPost.PNG)
Below is the search result page for the user entered date and time range. 
![searchResults](./screenshots/searchResults.png)
