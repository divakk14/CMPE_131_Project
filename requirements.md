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


 




## Login
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

## Manage Notes
**Pre-condition:** The user has created notes in the application
**Trigger:** User clicks “done” when finishing modification
**Primary Sequence:**
**Primary Postconditions:**
**Alternate Sequence:**

## Comment on Notes
**Pre-condition:**
**Trigger:**
**Primary Sequence:**
**Primary Postconditions:**
**Alternate Sequence:**

## User Profile Editing
**Pre-condition:** 
**Trigger:**
**Primary Sequence:**
**Primary Postconditions:**
**Alternate Sequence:**
