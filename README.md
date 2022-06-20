# Bug_management_system_(TrackingApp)
 Very simple app to track bugs, made with python

# Project notes
Bug management system

Login 

- Users must register with an email and username if they wish to submit bug reports or feature requests.

Two types of user

- Admin
- User

Class Admin is child to User class
Theres only one bug class. 

Tracking System 

- Users can create bug reports. Tickets contain a title, project, description or type of, priority, status, author, date submitted. The date the ticket was made and who made it are automatically added when submitted.

Search 

- It covers the title, description or type of, priority and status. eg. You can show all bugs with the word Unicorn in them in order of date submitted by searching "bug unicorn".

________________________________________________________________________________________________________________________

Admins or Users can edit the ticket or remove it completely, there could be a sort function (Not applied yet).
Working on applying a sql server to save user data and bug data.  