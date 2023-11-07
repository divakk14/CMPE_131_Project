## Functional Requirements
1. Registration
2. Authentication
3. Login Mauro
4. Password reset
5. Note Creation
6. Manage notes Mauro
7. Search notes Alan
8. Note categorization Visualizing note connections
9. User profile editing
10. Users are able to comment for additional info
11. User’s flexibility with the mode of the note
12. Recovery of deleted notes
13. Sorting Notes


## Non-functional Requirements
1. 


## Registration (Divak):
** Pre-condition: ** user doesn’t have any prior account on this website
** Trigger: ** User selects the “Sign up” button.
** Primary sequences:  **
Users access the registration page after clicking the register button
Users enter their first and last name, email address, password(alphanumeric), authentication questions
Account set up confirmation is received on the entered email address
** Primary Postcondition: ** Account is successfully created in the system
** Alternate Sequence: ** 
Cancel account creation

## Authentication (Alan):
**Pre-condition:** User must be in the process of registering for an account
**Primary Sequence:** 
User begins account registration.
  1. The browser prompts the user to choose 3 of the 10 security questions provided 
  2. User chooses 3 questions and provides an answer for them
  3. The system saves selected questions and their answers to the database 
  4. User proceeds to the steps mentioned in the registration use case.
**Primary Postcondition** User will be escorted to the home page
**Alternative sequence:**
  1. User answers the question incorrectly 
  2. Browser prompts the user to try again 
  3. After 3 incorrect answers browser prompts user to answer the other 2
  4. If all 3 tries are unsuccessful for the last 2, the user gets a temporary cooldown


 




## Login (Mauro)
  **Pre-condition:** The user has created an account and has access to the internet
  **Trigger:** User clicks “login” button
  **Primary Sequence:** 
  1. User access login page
  2. The user inputs their email, password, and security question
  3. The system verifies the provided credentials against the stored user data
  4. Successfully logged in (pop-up).  
  5. Redirect to the home (main) page
  **Primary Postconditions:** The user can access the notes list
  **Alternate Sequence:** The user has input invalid credentials

## Password Reset (Biruk)
** Pre-condition: **The user is registered with the system but is unable to access their account due to incorrect password assuming the user has entered the right email address and security questions.
** Trigger: ** User clicks “forgot password” button to initiate password reset. 
** Primary sequence: ** 
1. User navigates to the login page
2. The user inputs their email, password, and security question
3. The system notifies user that they have entered an incorrect password 
4. User clicks on the “forgot password” button
5. The system opens a form that prompts the user to enter their registered email address
6. User enters their email address and clicks submit 
7. The system generates a password reset link and sends it to the users email 
8. User receives the email and clicks on the password reset link
9. User sets a new password 
10. The system updates the password in the database 
11. User receives a password reset confirmation email.
** Primary postconditions: ** The user has successfully reset their password and can now login with the new password. 
** Alternate sequence: **
4. User enters an email address that is not found 
  a. The system informs the user that the email address is not registered via error message 
  b. The system prompts the user to enter a valid email address
7. User enters a new password that is not accepted 
  a. The system prompts the user to enter a valid password

## Note Creation (Biruk)
Pre-condition: The user is logged into the notes app  
Trigger: User chooses to create a new note by clicking the “+” icon  
Primary sequence: 
User navigates to the home page 
User opens the note creation interface in the application 
User enters the title and contents of the new note including any attachments e.g. image 
Auto saves when the note is closed. 
System stores the new note in the user’s account 
Primary postconditions: A new note is successfully created and stored in the user’s account, all notes will populate on home page  
Alternate sequence: 
4.1) User encounters an issue saving the note due to network error etc.
The system informs the user via error message 
The system offers the option to retry
4.2) User decides to discard note after starting the creation process 
User discards the note without saving 
The system asks if user is sure via pop up to avoid accidental deletion 


## Manage Notes (Mauro)
  **Pre-condition:** The user has created notes in the application
  **Trigger:** User clicks “done” when finishing modification
  **Primary Sequence:** 
  1. The user right-clicks the particular note they wish to modify.
  2. After the right click, an option list is dropped such as edit, delete, or move to the folder.
  3. If editing a note, the user modifies the content, update details, or adds information.
  4. If the user intends to delete a note, they select the option to delete the chosen note.
  5. The user reorganizes the selected note within the existing or new folder.
  6. Changes are saved by the system
  **Primary Postconditions:** Any changes made by the user during note management are reflected in the system
  **Alternate Sequence:** Note management cancellation

## Search Notes (Alan)
 **Pre-condition:** User is on the home page by default.
 **Trigger:** User clicks the search bar on the home page
 **Primary Sequence:** 
 User types in the search bar.
 User’s search parses in all of the notes list and it searches the content of each note. 
 It displays the information related to the user's search.
 Then the user selects the one they want to form the list.
 Primary postcondition: 
User continues with the note which is related to their search.
Alternative sequence: 
User is no longer interested in searching.

##Note Organization: Visualize note connections (Biruk)
Pre-condition: The user is logged into the notes website and is on the home page.
Trigger: User clicks the “select” button.   
Primary sequence: 
User will click the “select” button to move notes into a folder 
The system will prompt user to select at least one note from the preexisting list of saved notes 
User selects the notes they want to move and clicks “next”
The system will prompt user to select a folder from the preexisting list of folders or create a new folder 
If user selects new folder the system will prompt them to name the folder before continuing 
User will click “done” 
The system will save notes to a specified folder
Primary postconditions: The selected notes are successfully moved into the chosen folder.   
Alternate sequence: The user opts to “cancel” the organization process before reaching step 7


## Comment on Notes (Mauro)
  **Pre-condition:**
  **Trigger:**
  **Primary Sequence:**
  **Primary Postconditions:**
  **Alternate Sequence:**

## User Profile Editing (Mauro)
  **Pre-condition:** 
  **Trigger:**
  **Primary Sequence:**
  **Primary Postconditions:**
  **Alternate Sequence:**
