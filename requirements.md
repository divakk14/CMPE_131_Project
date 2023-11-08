# Functional Requirements
1. **Registration:** Allows the user to create an account on the notes web application
2. **Authentication:** 
3. **Login:** Allows the user to enter their credentials and sign into the notes web application 
4. **Password reset:** If the user has forgoten their password this is a way to reset it
5. **Note Creation:** Allows the user to create a new note in the notes web application
6. **Manage notes:**
7. **Search notes:** Allows the user to search for key words in their collection of notes 
8. **Note categorization (Visualizing note connections)**
9. **Home Button:** Allows the user to go back to the homepage once they have navigated elsewhere
10. **Comment on a particular note:**
11. **User’s flexibility with the mode of the note:**
12. **Recovery of deleted notes:** Allows the user to restore a previously deleted note 
13. **Sorting Notes:**
14. **User profile editing:** Allows the user to edit the information in their profile after registration 

# Non-functional requirements: 
1. When the particular note is opened there should be a label or tag of the folder if the note belongs to any of the folders.
2. The title of the notes should be bold.  

## Registration (Divak):
**Pre-condition:** The user doesn’t have any prior account on this website

**Trigger:** User selects the “Register” button.

**Primary sequences:**
1. Users access the registration page after clicking the register button
2. Users enter their first and last name, email address, password (alphanumeric)
3. Account set-up confirmation is received on the entered email address

**Primary Postcondition:** Account is successfully created in the system

**Alternate Sequence:** 

2. Cancel account creation

## Authentication (Alan):
**Pre-condition:** User must have Gmail connected 

**Trigger:** User enters email and password on the login page and clicks login

**Primary Sequence:** 
1. The user receives verification code on their email
2. The browser prompts user to a new page asking for the verification code
3. The user checks their email for the code
4. The user enters the code they are sent
5. The system verifies the code with the code sent to the Gmail account. 

**Primary Postcondition** User will be escorted to the home page

**Alternative sequence:**

4. User enters an incorrect code

   a) The system notifies the user that the code entered is invalid

   b) The system prompts the user to enter the right code


## Login (Mauro)
  **Pre-condition:** The user has created an account and has access to the internet
  
  **Trigger:** User clicks the “login” button
  
  **Primary Sequence:** 
  1. User access login page
  2. The user inputs their email, and password.
  3. once they enter the valid email they receive the authentication code on the same email. 
  4. The system verifies the provided credentials and code with the code sent to the email. 
  5. Successfully logged in (pop-up).  
  6. Redirect to the home (main) page
  
  **Primary Postconditions:** The user can access the notes list
  
  **Alternate Sequence:**
The user has input invalid credentials


## Password Reset (Biruk)
**Pre-condition:** The user is registered with the system but is unable to access their account due to an incorrect password assuming the user has entered the right email address

**Trigger:** User clicks “forgot password” button to initiate password reset. 

**Primary sequence:** 
1. The system opens a form that prompts the user to enter their registered email address.
2. User enters their email address and clicks submit.
3. The system generates a password reset link and sends it to the users email.
4. User receives the email and clicks on the password reset link.
5. User sets a new password.
6. The system updates the password in the database.
7. User receives a password reset confirmation email.

**Primary postconditions:** The user has successfully reset their password and can now login with the new password. 

**Alternate sequence:**

4. User enters an email address that is not found 

   a. The system informs the user that the email address is not registered via error message 

   b. The system prompts the user to enter a valid email address

7. The user enters a new password that is not accepted

   a. The system prompts the user to enter a valid password (alphanumeric)


## Note Creation (Biruk)
**Pre-condition:** The user is logged into the notes web application

**Trigger:** User chooses to create a new note by clicking the “+” icon  

**Primary sequence:**
1. User navigates to the home page
2. User opens the note creation interface in the application
3. User enters the title and contents of the new note including any attachments e.g. image
4. Auto saves when the note is closed.
5. System stores the new note in the user’s account

** Primary postconditions:** A new note is successfully created and stored in the user’s account, all notes will populate on home page  

**Alternate sequence:**

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
  6. The system saves changes
 
  **Primary Postconditions:** Any changes made by the user during note management are reflected in the system
  
  **Alternate Sequence:**
Note management cancellation


## Search Notes (Alan)
 **Pre-condition:** User is on the home page by default.
 
 **Trigger:** User clicks the search bar on the home page
 
 **Primary Sequence:** 
 1. User types in the search bar.
 2. User’s search parses in all of the notes list and it searches the content of each note.
 3. It displays the information related to the user's search.
 4. Then the user selects the one they want to form the list.

**Primary postcondition:** User continues with the note which is related to their search.

**Alternative sequence:**
User is no longer interested in searching


## Note Organization: Visualize note connections (Biruk)
**Pre-condition:** The user is logged into the notes website and is on the home page.

**Trigger:** User select the notes they want to perform an action on (move or delete)   

**Primary sequence:**
1. User will select the notes.
2. User will right click after the prefered notes are selected.
3. User will select to either move or delete the selected notes.
4. User's preferred action will be perfomred. 
7. The system will save notes to a specified folder or delete them

**Primary postconditions:** The selected notes are either moved to the particular folder or dleted.    

**Alternate sequence:**
   
   1. User deselcts all notes except one and has the ability to edit, move, or delete 


## Home Button (Biruk)
**Precondition:** User has one of the notes opened 

**Trigger:** User clicks the home button

**Primary Sequence:**
1. User has a note open
2. User is done editing/viewing the note
3. User wants to exit the note
4. User clicks the home button

**Primary postcondition:** User gets redirected to the home page 

**Alternative sequence:**

4. User doesn’t click the home button and ends up staying on the opened notes


## Comment on Notes (Mauro)
**Pre-condition:** The user has already created a note

**Trigger:** User clicks “done” after typing in the comment section

**Primary Sequence:** 
  1. The user navigates to the specific section or feature for comments or additional information.
  2. The system displays the content or subject for which the user wishes to comment or provide additional information.
  3. The user selects the option or interface to create a new comment or provide supplementary details.
  4. The user clicks the "Done" button to submit the comment.
  5. The system processes and saves the user's comments or additional information.

**Primary Postconditions:** The user's comment is successfully added and displayed within the respective section or associated content

**Alternate Sequence:**
Deleting Comment: Users might have the option to delete their own comments, removing them from public view


## User’s flexibility with the note mode (dark mode, grid view, list view etc) (Divak)
**Pre-condition:** user already logged in and some default mode is already there. 

**Trigger:** by clicking the action button “More” user will see option listed as “ View by” 

**Primary sequences:** 
1. The user is logged in.
2. There is a default mode but the user wants to change that so they click the system mode.
3. They choose the mode either light or dark.
4. The user selects the view to have their list by grid or by list.

**Postcondition:** The user can see the preference they chose.

**Alternate sequence:**
The user will have the default website version.


## Recovery of deleted notes (Divak)
**Pre-condition:** The user has already deleted the notes which are stored in the deleted folder.

**Trigger:** The user will open the trash folder where the deleted note will be stored so the user will have two options either to delete it permanently or recover it. 

**Primary sequences:**
1. The user will open the trash folder.
2. Users will select the note they want to recover.
3. Users will click the recover option once they select the note they want to recover from the trash folder.
4. Then the user will go back to the list of existing notes where they will see the deleted note successfully recovered from the trash folder. 

**Primary postcondition:** user can see their deleted notes in the default notes list.

**Alternate sequence:**
The user permanently loses their note. 


## Sorting Notes: (Alan)
**Pre-condition:** there should be more than one note.

**Trigger:** when more than one note is in the system the user account’s sorting algorithm at the backend acts as a trigger. 

**Primary sequence:**
1. Users have an existing note.
2. User starts writing a second note.
3. The backend sorting algorithm sorts according to the latest note added to the notes using the timestamp library. 

**Primary postcondition:** user sees the latest note on top of the list.

**Alternative sequence:**
unsorted notes list.


## User Profile Editing (Mauro)

**Pre-condition:** The user has an existing profile and has access to the internet

**Trigger:** User clicks on the “edit profile” button

**Primary Sequence:**
  1. The user navigates to the profile or account settings section.
  2. The system displays the user's current profile information, such as username, email, and other stored details.
  3. The user selects the information they wish to modify, such as password  and profile picture
  4. The system verifies the entered information for validity and consistency.
  5. Saving Changes: If the entered data is valid, the user confirms to save the changes.

**Primary Postconditions:** The user’s profile is updated with the changes made and is reflected in the system

**Alternate Sequence:**
The user decides to cancel the editing process with the original information intact


## Logout: (Alan)
**Pre-condition:** user is already logged into the website.

**Trigger:** user clicks the logout button. 

**Primary sequence:**
1. User is done using the website.
2. User wants to exit the website.
3. Then they still click the logout button to exit the website successfully and securely. 

**primary postcondition:** user is successfully logged out.

**Alternate sequence:**
user wants to view the list of already existing notes. 
