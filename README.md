# Visitor-management
A desktop application built using Tkinter for the GUI and SQLite for the database. This system allows users to manage visitor details efficiently, including adding new visitors, viewing all records, and deleting specific entries through an admin interface.

## Features

- **Add Visitor Details**: Input fields for visitor name, phone number, in-time, out-time, and office selection.
- **Data Validation**: Ensures correct and complete information for names, phone numbers, and time entries.
- **Admin Login**: Secure admin access to view and delete visitor records.
- **View Records**: Displays all visitor entries in a scrollable text widget.
- **Delete Records**: Allows deletion of specific visitor records based on phone number.

## Prerequisites

- Python 3.x
- Tkinter (usually included with Python)
- SQLite3

## Follow the steps:

**Set up the SQLite database:**
- sqlite3 visitor.db

**Create the "visitor" table:**
 - CREATE TABLE visitor (
    name TEXT,
    phone TEXT,
    intime TEXT,
    outtime TEXT,
    office INTEGER
 );

**_Run the application:_**
 - python vms.py or the file name you gave.

**Adding Visitor Details:**
- Enter the visitor's name, phone number, in-time, out-time, and select the office.
- Click 'Submit' to save the details.

**Admin Login:**
- Username: admin
- Password: abc123

  

  
