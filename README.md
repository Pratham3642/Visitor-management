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
 - CREATE TABLE visitor(name text,phone integer,in_time text,out_time text,office text);

**_Run the application:_**
 - python vms.py or the file name you gave.

**Adding Visitor Details:**
- Enter the visitor's name, phone number, in-time, out-time, and select the office.
- Click 'Submit' to save the details.

**Admin Login:**
- Username: admin
- Password: abc123

## Input Validations:

1. Name Field:

Cannot be empty.
Must contain only alphabetical characters.
Must be between 2 to 50 characters long.

2. Phone Number Field:

Cannot be empty.
Must contain only digits.
Must not be negative.
Must be exactly 10 digits long.

3. In-Time and Out-Time Fields:

Cannot be empty.
Must be in the format HH:MM:SS
Must be a valid time format.

4. Office Selection:

Must select an office (cannot be 0).

## Output:

**Main Visitor Entry Page (root):**

![Screenshot 2024-06-01 113718](https://github.com/Pratham3642/Visitor-management/assets/162919475/dc6aa9d7-c6bd-417b-a4cd-1cdfeb8181fb)

**Admin Login Page (admin):**

![Screenshot 2024-06-01 113746](https://github.com/Pratham3642/Visitor-management/assets/162919475/8d2e7822-5858-44b4-b090-e2727644947b)

**Visitor Information View Page (view):**

![Screenshot 2024-06-01 113853](https://github.com/Pratham3642/Visitor-management/assets/162919475/7109b91b-7ac1-445b-be55-75681081bd7f)


  

  
