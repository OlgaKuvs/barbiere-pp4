# Barbiere Maestro

### [Live site](https://barbiere-e0b7941f6ea4.herokuapp.com/)

## Contents:

- <a href="#ux">UX</a>
- <a href="#testing">Testing</a>

## <div id="ux">UX</div>
### Overview
Barbiere Maestro is a website for a modern barbershop salon. The main goal is to create a simple and intuitive website based on a deep understanding of the target users. Users of the site can obtain detailed information about the services provided, about the experience of each barber, and also look at examples of barber's haircuts in photos to decide whether they want to use the services of this salon.

#### First Time User
- As a person who lives near a barbershop and looking for good barber service.
- As a person who is looking for clear information about the barbershop and services provided.
- As a person who prefer to make bookings digitally rather than speaking with others.

#### Returning User
- As a returning user, I would like to review all my previous barbershop appointments.
- As a returning user, who already has an account I would like quickly and easily make an appointment with a barber.
- As a returning user, I would like to see updates to the information on the site so that I can find something new and interesting for myself (for example, new modern haircuts).

### Strategy
Determining the best approach meant studying the needs of potential users. This included users logging in, quickly and easily booking appointments, reading, updating and deleting their appointments (CRUD). 
One of the main features of this website is the ability for the registered user to fill out and submit the booking form without refreshing the page. The form contains 3 dependent dropdown lists where the user can select the service he needs, the barber and the date and time of appointment.

#### Agile
The Agile methodology was used to plan the project. Github was used as the tool to demonstrate this. 

Projects were used to divide the project into three iterations with a simple [Kanban board](https://github.com/users/OlgaKuvs/projects/3/views/1).
To prioritize tasks [MoSCoW method](https://github.com/users/OlgaKuvs/projects/3/views/4) was used.

##### User Stories 
Issues were used to create User Stories with a custom templates for admin and user. I added the acceptance criteria and the tasks so I can track my work effectively. Once I completed a User Story I would move it from in progress to completed. 

- User Stories:
 
  - As a User I would like to examine the information on the home page about the services provided so that decide whether I want to use them.
  - As a User I would like to create an account so that I can book an appointment.
  - As a User, I would like to log in, so that I can access my profile.
  - As a Registered User I would like to see a list of available services, including relevant details such as barber name, appointment date and time so that I can choose the options that suit me.
  - As a Registered User I would like to view my appointments so that I can keep track of my booking (CRUD).
  - As a Registered User I would like to edit my booking so that I can change the details (CRUD).
  - As a Registered User I would like to delete my booking so that I can cancel my appointment (CRUD).
  - As a Registered User, I want to receive a confirmation text message or email, so that I know my appointment has been successfully booked.
  - As a Registered User I would like to be able to make an appointment with any barber to get the opportunity to choose a wider range of dates and times.
  - As an Admin I would like to view the bookings so that I can manage the barber's timetable.
  - As an admin I would like to have an access to database data so that I can make necessary changes (CRUD).


## <div id="testing">Testing</div>

### Manual testing

#### Testing User Stories 

| User story        | User story testing |           
| ------------------ | ------------- | 
| As a User I would like to examine the information on the home page about the services provided so that decide whether I want to use them. | On the home page user can view complete information about the barbershop, services with descriptions and prices, information about each barber including his name and work experience. Also user can view the pictures of various haircuts as work examples and choose the haircut that he likes.
| As a User I would like to create an account so that I can book an appointment. | On registering for the user account, the user populates their own information for log in in the future. User can add their username, first name, last name, e-mail address and password during the registration process (Create). | 
| As a User, I would like to log in, so that I can access my profile. | Once logged in, a registred user can view a list of their appointments on their profile page (Read). If the user does not have an appointment yet they can click the link to make an appointment. | 
| As a Registered User I would like to see a list of available services, including relevant details such as barber name, appointment date and time so that I can choose the options that suit me.| On the booking page, the user can see the booking form with 3 dependent dropdown lists: the list of services, the list of barbers providing the selected service and the list of available dates and times for the selected barber. And he can choose from the lists what suits him. |
|As a Registered User I would like to view my appointments so that I can keep track of my booking.| On the profile page user can view all details of their bookings including service name, barbers name and date and time of appointment. From this view they have acccess to every booking update (Edit button) or delete (Delete button).  |
| As a Registered User I would like to edit my booking so that I can change the details. | On the profile page, the user can click the "Edit" button for each of their appointments and will be redirected to the `edit` page. On the `edit` page they can see all the details of the current booking and below the form for making changes. After making the necessary changes, the user can click "Change" button and will be redirected to the profile page, where all changes made are reflected. Or the user can click the "Cancel" button to be redirected to the profile page without making any changes.| 
| As a Registered User I would like to delete my booking so that I can cancel my appointment. | On the profile page, the user can click the "Delete" button for each of their appointments and will be redirected to the `delete` page. On the `delete`  page they will be asked to confirm the deletion. If they click "Yes" button, the appointment will be deleted, and they will be redirected to the profile page. If they click "Cancel" button, they will be redirected to the profile page without making any changes. |
| As an admin I would like to have an access to database data so that I can make necessary changes. | Superuser has been created. All tables are visible and editable from the admin view. |
| As an Admin I would like to view the bookings so that I can manage the barber's timetable. | The Admin has access to booking's data and can determine the workload of each barber. Admin has access to the table with a list of barbers and checks or unchecks the  `is_available` button for each barber to manage the schedule (for example, if the barber is sick or on vacation and is not currently working). |

The following User stories were not completed (marked as `Could have` in MoSCoW method table) as they were deemed to be not necessary for this project at this time but are indications of possible future features:

 - As a Registered User, I want to receive a confirmation text message or email, so that I know my appointment has been successfully booked.
 - As a Registered User I would like to be able to make an appointment with any barber to get the opportunity to choose a wider range of dates and times.

