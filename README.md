# SAT Score Database using Python

A simple database used to view, insert, update and delete SAT records.


## Available Features
- Insert a Record
- View All Data
- Display SAT Score
- Update the SAT Score
- Delete a Record
- Save All Data to a File


### Feature 1 - Insert a Record

User is able to add a record using name as unique identifier. Address, City, Country, Pincode and SAT score is also recorded. The Exam Status is calcuated and if the SAT score > 30% then Exam Status is Pass or else Fail.


### **Feature 2 - View All Data**

User is able to view all avaialbe records in the database in json format.


### **Feature 3 - Display SAT Score**

User is able to enter a name, and if a record entry is found then the SAT score associcated with that name is displayed.


### **Feature 4 - Update SAT Score**

User is able to enter a name, and if a record entry is found then the SAT score associcated with that name is udpated with a new score.


### **Feature 5 - Delete a Record**

User is able to enter a name, and if a record entry is found, that record is deleted.

### **Feature 6 - Save All Data to a File**

All the available records in the database are saved to a file in json format.


## Scope for Improvement
- Add feature to display a single record
- Add feature to display a set of record matching a critera. For example, '\_Display records with Exam Status as Pass\_' or '\_Display records with Country that is not India\_'
- Add feature to update other values in a record
- Add 'Current Date and Time' value while creating/updating a record
- Add feature to delete multiple records at once
- Add feature to delete all records
- Make GUI for this application
