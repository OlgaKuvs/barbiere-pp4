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
| As a Registered User I would like to see a list of available services, including relevant details such as barber name, appointment date and time so that I can choose the options that suit me.| On the booking page, the user can see the booking form with 3 dependent dropdown lists: the list of services, the list of barbers providing the selected service and the list of available dates and times for the selected barber. And they can choose from the lists what suits them. |
|As a Registered User I would like to view my appointments so that I can keep track of my booking.| On the profile page user can view all details of their bookings including service name, barbers name and date and time of appointment. From this view they have acccess to every booking update (`Update` button) or delete (`Delete` button).  |
| As a Registered User I would like to edit my booking so that I can change the details. | On the profile page, the user can click the "Edit" button for each of their appointments and will be redirected to the update page. On the update page they can see all the details of the current booking and below the form for making changes. After making the necessary changes, the user can click "Change" button and will be redirected to the profile page, where all changes made are reflected. Or the user can click the "Cancel" button to be redirected to the profile page without making any changes.| 
| As a Registered User I would like to delete my booking so that I can cancel my appointment. | On the profile page, the user can click the "Delete" button for each of their appointments and will be redirected to the `delete` page. On the `delete`  page they will be asked to confirm the deletion. If they click "Yes" button, the appointment will be deleted, and they will be redirected to the profile page. If they click "Cancel" button, they will be redirected to the profile page without making any changes. |
| As an admin I would like to have an access to database data so that I can make necessary changes. | Superuser has been created. All tables are visible and editable from the admin view. |
| As an Admin I would like to view the bookings so that I can manage the barber's timetable. | The Admin has access to booking's data and can determine the workload of each barber. Admin has access to the table with a list of barbers and checks or unchecks the  `is_available` button for each barber to manage the schedule (for example, if the barber is sick or on vacation and is not currently working). |

The following User stories were not completed (marked as `Could have` in MoSCoW method table) as they were deemed to be not necessary for this project at this time but are indications of possible future features:

 - As a Registered User, I want to receive a confirmation text message or email, so that I know my appointment has been successfully booked.
 - As a Registered User I would like to be able to make an appointment with any barber to get the opportunity to choose a wider range of dates and times.

#### Testing Features
##### Navigation links

| Test |  Result |          
| ------------------ | ------------- |
| Non logged in user can access the links of landing page in the navbar.  | Non logged in user can access Home, Services, Our Staff, Gallery and Contact pages. All navigation links on landing page are working and bring the user to the correct part of the page. Active page link is highlighted in each case. Navbar remains in view when scrolling. 
| Non logged in user can go to the home page by clicking the title or logo in the page header. | Links from `Barbiere Maestro` title and logo image allow the user to return to home page from each part of landing page. |
| Non logged in user can access to sign in and login pages.| User can click the `Login` button on the right side of the header and will be redirected to the login page. For signing in, there are 2 navigation buttons `Sign up and Book now!` on hero image and in the footer. By clicking these buttons the user is redirected to the sign up page. |
| Logged in user can access to profile page and log out. | Logged in user can view `Profile` and `Logout` buttons on the right side of the page header. Sign up buttons are not visible to the logged in user. |
| Logged in user can view the bookings.| List of bookings is available on user's profile page. User can acccess the profile page by clicking `Profile` button on the navigation bar. |
| Logged in user can log out of their profile.| User can click `Logout` button on the navigation bar and  log out of their profile. |

##### User Forms

| Test |  Result |          
| ------------------ | ------------- |
| User can create account. | User is redirected to the registration page by clicking `Sign up and Book now!` on the homepage. Also user can access registration page from login page. They will be asked to register if they don't already have an account. The registration form has error handling built in so the user must make the correct inputs. If inputs are incorrect the user is shown a message about incorrect data entry. |
| User can log in. | User is redirected to the login page by clicking `Login` button. Also user can access login page from registration page. They will be asked to log in if they have an account. If the username or password is incorrect,  the message `Username or password is wrong! Try again...` is displayed to the user. |
| Logged in user can make a booking. | Logged in user can access booking page from `Our staff` part of landing page by clicking `Book now` button, and also from user profile page by clicking  `Book an appointment`. Then user is redirected to the booking page. On the booking page, the user can fill out a form by selecting services from the list, barbers from the list, choose the date and time of the appointment, and then click `Book` button. User can make a booking when all fields complete. User is redirected to the profile page to view the list of their appointments. | 

| Logged in user can update the bookings.| Each booking in the bookings list has an `Update` button. On clicking `Update` the user is redirected to update page. Full details of the current booking are displayed on the update page and the user is prompted to change the booking by filling out the booking form below. User can update a booking when all fields complete. Updated booking data is displayed on profile page.  |  

#####  Security Tests

| Test |  Result |          
| ------------------ | ------------- |
|Non logged in user cannot make a booking. | The booking page is available only to authorized users. If non logged in user clicks `Book` button on the landing page an informational message is displayed asking them to log in to make an appointment.  |
|Non logged in user cannot access profile page. | The link to the profile page is visible only to authorized users.|
|User cannot delete a booking without confirmation. | Each booking in the bookings list has an `Delete` button. On clicking `Delete` the user is redirected to delete page and is asked to confirm that they want to cancel the appointment. Сlicking `Yes` deletes the booking. Updated booking data is displayed on profile page.
| Non superuser cannot access admin panel. | The admin panel is accessible only to the user with a superuser login and password. |

##### Admin Tests

| Test |  Result |          
| ------------------ | ------------- |
|Admin can view data in database tables. | Admin (superuser) can view all data from database tables including ManyToManyField data. To display ManyToManyField data in `list_display` field, a custom method was added to the class `BarberAdmin`. |
|Admin can add items to the following tables: Services, Barbers, Working Hours, Bookings and Users| Admin can access to all database tables and can add items to them.  |
|Admin can edit items in database. | Admin can access all fields in the database tables and make any changes. |
|Admin can search and filter data in database tables.  | Admin can search and filter data in database tables using custom fields specified in the corresponding classes. |
|Admin can delete items in database. | Admin can access all fields in the database tables and can delete a model instance. Any objects which had foreign keys pointing at the object to be deleted will be deleted along with it.
|Admin can manage the barber's availability. | Admin can check or uncheck `is_available` flag for each barber changing the work schedule in case the barber is sick, goes on vacation, or is absent for some other reason. Unchecked `is_available` flag means that the barber will not be available to the user on the booking form.
