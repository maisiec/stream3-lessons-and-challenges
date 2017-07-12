# Summary

In this lesson, we’ve learned that:

- Django supports ORM through models

- All model classes inherit from the 
models.Model class

- Model attributes map to database table fields

-Python comes with the SQLite DBMS

-Django projects are pre-configured to use SQLite, but can also use other DBMSs

-To  populate our database, we must first run the migrate command

- We run the makemigrations command followed by the migrate command after adding a new model or modifying an existing one

- SQLite has a free GUI-based administration application called SQLite Database Browser available, which you can use to view your project database and its tables

- You can populate your models with data through the Python shell


# Challenge 

Create a new project and associated app that will contain a database table with a list of quotes.