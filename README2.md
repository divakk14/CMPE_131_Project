Welcome to the Note App, a collaborative project developed by the team comprising Divak, Biruk, Alan, and Mauro. This README provides instructions to run the project and offers insights into its functionality.

How to Run the Project

Clone the Repository:
git clone https://github.com/divakk14/CMPE_131_Project.git

Navigate to the Project Directory:
cd CMPE_131_Project

Install Dependencies:
pip3 install flask-wtf flask-sqlalchemy flask-login

Run the Application: python app.py
Access the App: Open your web browser and visit: 

General Instructions:
The app provides a user-friendly interface to create, edit, and manage notes and folders.
To register, click on the "Register" button and follow the prompts. After registration, use the "Login" button to access your account.
Upon login, you'll be directed to the home page, where you can view existing notes and folders or create new ones.
Use the "Create New Note" button to add a new note. Select a folder and enter the note details.
The "Trash Folder" contains deleted notes, offering a chance to recover or permanently delete them.
The "Edit Profile" button allows users to update their profile information, including changing the password.
To log out, click the "Logout" button.


Implemented Functional Requirements

User Registration (Divak):
Users can register for an account with their first and last name, email address, and alphanumeric password.

User Authentication (Alan):
Secure login with a verification code sent to the user's Gmail account.

Login (Mauro):
Users can log in with their email and password, receiving an authentication code on their email.

Password Reset (Biruk):
Users can initiate a password reset by clicking the "Forgot Password" button.

Note Creation (Biruk):
Users can create new notes, including attachments like images, with an auto-save feature.

Manage Notes (Mauro):
Users can modify notes by right-clicking to access options like edit, delete, or move to a folder.

Search Notes (Alan):
Users can search for notes using the search bar on the home page.

Note Organization (Biruk):
Users can visualize connections between notes and perform actions like moving or deleting selected notes.

Home Button (Biruk):
A home button is accessible from various pages, redirecting users to the home page.