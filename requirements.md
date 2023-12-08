# Functional Requirements
1. **Registration:** Allows the user to create an account on the Notes web application
2. **Authentication** 
3. **Login:** Allows the user to enter their credentials and sign into the notes web application 
4. **Password reset:** If the user has forgotten their password this is a way to reset it
5. **Note Creation:** Allows the user to create a new note in the notes web application
6. **Manage notes**
7. **Search notes:** Allows the user to search for keywords in their collection of notes 
8. **Note categorization (Visualizing note connections)**
9. **Home Button:** Allows the user to go back to the homepage once they have navigated elsewhere.
10. **Comment on a particular note**
11. **User’s flexibility with the mode of the note**
12. **Recovery of deleted notes:** Allows the user to restore a previously deleted note 
13. **Sorting Notes**
14. **User profile editing:** Allows the user to edit the information in their profile after registration 

# Non-functional requirements: (Divak) 
1. Automatic labeling: When a particular note is opened there should be a label or tag automatically associating the note to a folder if it belongs to any of the folders. It's an automatic function where the user doesn't interact. 
2. User interface consistency: The user interface is consistent throughout all pages meaning all the pages will have a uniform layout structure, color schemes, and font styles. Example: Titles of all the notes will have font bigger than the body.  

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
**Summary:** The user authentication use case primarily focuses on ensuring secure access to the application for existing users. It involves the validation of login credentials and the establishment of a secure session. This process is crucial for maintaining the confidentiality and integrity of user data, as only authenticated users should be granted access to their personalized content and features within the application.
**Pre-condition:** User must have Gmail connected.


**Trigger:** User enters email and password on the login page and clicks login

**Primary Sequence:** 
1. The user receives a verification code on their email
2. The browser prompts the user to a new page asking for the verification code
3. The user checks their email for the code
4. The user enters the code they are sent
5. The system verifies the code with the code sent to the Gmail account. 

**Primary Postcondition** User will be escorted to the home page

**Alternative sequence:**

4. The user enters an incorrect code

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
  
  **Primary Postconditions:** The user can access the notes list.
  
  **Alternate Sequence:**

2. The user has inputted invalid credentials.


## Password Reset (Biruk)
**Pre-condition:** The user is registered with the system but is unable to access their account due to an incorrect password assuming the user has entered the right email address

**Trigger:** User clicks the “forgot password” button to initiate a password reset. 

**Primary sequence:** 
1. The system opens a form that prompts the user to enter their registered email address.
2. The user enters their email address and clicks submit.
3. The system generates a password reset link and sends it to the user's email.
4. The user receives the email and clicks on the password reset link.
5. The user sets a new password.
6. The system updates the password in the database.
7. User receives a password reset confirmation email.

**Primary postconditions:** The user has successfully reset their password and can now log in with the new password. 

**Alternate sequence:**

4. User enters an email address that is not found 

   a. The system informs the user that the email address is not registered via error message 

   b. The system prompts the user to enter a valid email address

7. The user enters a new password that is not accepted

   a. The system prompts the user to enter a valid password (alphanumeric)


## Note Creation (Biruk)
**Pre-condition:** The user is logged into the Notes web application

**Trigger:** User chooses to create a new note by clicking the “Create a note” button.  

**Primary sequence:**
1. User navigates to the home page
2. The user opens the note creation interface in the application
3. The user enters the title and contents of the new note including any attachments e.g. image
4. Auto saves when the note is closed.
5. System stores the new note in the user’s account

**Primary postconditions:** A new note is successfully created and stored in the user’s account, all notes will populate on home page  

**Alternate sequence:**

4. The user decides to discard the note after starting the creation process 

   a. The user discards the note without saving it.
   
   b. The system asks if a user is sure via pop-up to avoid accidental deletion 


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
  
3. Note management cancellation


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

1. The user is no longer interested in searching



**Alternate sequence:**
   
   1. The user deselects all notes except one and can edit, move, or delete 


## Home Button (Divak)
**Summary:** The home button will be accessible from wherever they are in the application. It is used when the user is creating a note and wants to exit back to the home page, it will redirect them to home. When the user is navigating different interlinked pages and they directly want to access their home page they can hit the Home button instead of pressing back numerous times. 

**Precondition:** User has one of the notes opened. 

**Trigger:** User clicks the home button

**Primary Sequence:**
1. The user has a note open
2. The user is done editing/viewing the note
3. The user wants to exit the note
4. The user clicks the home button

**Primary postcondition:** User gets redirected to the home page 

**Alternative sequence:**

4. The user doesn’t click the home button and ends up staying on the opened notes


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

5. Deleting Comment: Users might have the option to delete their comments, removing them from public view


## User’s flexibility with the note mode (dark mode, grid view, list view, etc) (Divak)
**Pre-condition:** The user already logged in and some default mode is already there. 

**Trigger:** By clicking the action button “More” the user will see an option listed as “ View by” 

**Primary sequences:** 
1. The user is logged in.
2. The user wants to change the mode so they click the view by for their preferences.
3. They choose the mode either light or dark.
4. The user selects the view to have their list by grid or by list.

**Postcondition:** The user can see the preference they chose.

**Alternate sequence:**

2. The user will have the default website version.


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

3. The user permanently loses their note. 

## Sorting Notes: (Alan)
**Pre-condition:** There already exists a note. 

**Trigger:** When more than one note is in the system the notes list is sorted according to the time stamp meaning oldest on top and newest on bottom of the list. 

**Primary sequence:**
1. There is a pre-existing note in the user's account.
2. The user starts writing a second note.
3. The system successfully saves the latest note.
4. Now the sorting algorithm will sort both of the notes according to the time stamps.

**Primary postcondition:** The user sees the latest note on top of the list.

**Alternative sequence:**

2. The user decides to cancel the new note creation.

   a. The previous note(s) are sorted by default (Timestamp)

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

3. The user decides to cancel the editing process with the original information intact


## Logout: (Alan)
**Pre-condition:** The user is already logged into the website.

**Trigger:** The user clicks the logout button. 

**Primary sequence:**
1. The user is done using the website and wants to exit the website.
2. The user will click the action button (more) to successfully log out.
3. The user is now navigated to the login page. 

**Primary postcondition:** User is successfully logged out.

**Alternate sequence:**

1. The user is interested in doing some activity with the already existing notes. 
