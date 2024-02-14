# BOOKZONE

![Bookzone](docs/readme/project-mockup.jpg)

A web application that enables users to sell, and buy second-hand books.

Visit the live site: [Bookzone]()

# Table of contents

- [User Experience (UX)](#User-Experience-UX)
  - [User Stories](#User-Stories)

- [Agile Metodology](#Agile-metodology)

- [Design](#Design)

  - [Flowchart](#Flowchart)
  - [Database Schema](#Database-Schema)
  - [Colour Palette](#Colour-Palette)
  - [Typography](#Typography)
  - [Imagery](#Imagery)
  - [Wireframes](#Wireframes)
  - [Features](#Features)
  

- [Technologies Used](#Technologies-Used)

  - [Languages Used](#languages-used)
  - [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

- [Deployment & Local Development](#Deployment--Local-Development)

  - [Deployment](#Deployment)
  - [Local Development](#Local-Development)
    - [How to Fork](#How-to-Fork)
    - [How to Clone](#How-to-Clone)

- [Testing](#Testing)

- [Credits](#Credits)
  - [Code Used](#code-used)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgments](#Acknowledgments)

---

## User Experience (UX)

#### Key information for the site

This section provides insight into the UX process, with a focus on the people who this restaurant booking system has been created for, the main aims of the project and how it can help users to meet their needs.

Project goals:

- To encourage people to sell and buy second-hand books by using the application.

- To provide an easy and user-friendly web app where users can buy and sell books and know more.

- To provide a system where the product owner can manage books and interact with customers.

### User Stories

|   EPIC                                |ID|                                User Story                                                   |
| :-------------------------------------|--|:------------------------------------------------------------------------------------------- |
|**CONTENT AND NAVIGATION**             |  ||
|                                       |1A| As a user, I want to easily access all the content in the shop |             
|                                       |1B| As a user, I want to see relevant information about the books|
|                                       |1C| As a user, I want the website to have a nice and intuitive design that will match the shops's theme|
|**USER REGISTRATION/AUTENTHICATION**   |  || 
|                                       |2A| As a user, I want to be able to register on the website|
|                                       |2B| As a user, I want to be able to authenticate using only email and password|
|                                       |2C| As a user, I want to be able to log out at any time|
|**BOOKS**                            |  ||
|                                       |3A| As a logged-in user, I want to be able to find the available books to buy and list any books I have to sell|
|                                       |3B| As a logged-in user, I want to be able to select the book I want to buy or sell|                                  
|**USER PROFILE**                       |  ||
|                                       |4A| As a logged-in user, I want to create en entry|
|                                       |4A| As a logged-in user, I want to view a list of my books|
|                                       |4B| As a logged-in user, I want to be able to edit my books|
|                                       |4C| As a logged-in user, I want to be able to delete my books|
|**ADMIN MANAGE BOOKS**              |  ||
|                                       |5A| As a logged-in admin member, I want to see the the books and store information|
|                                       |5B| As a logged-in admin member, I want to be able to filter books|
|**CONTACT**                            |  ||
|                                       |6A| As a user, I want to see contact information on the website|
                                      

---

## Agile Metodology

The MoSCow method was used with accompanying custom Github project labels to help me to prioritise the important tasks.

![Github user stories](docs/readme/user-stories-1.jpg)

### MoSCoW Prioritization
I've decomposed my Epics into stories prior to prioritizing and implementing them. Using this approach, I was able to apply the MoSCow prioritization and labels to my user stories within the Issues tab.

- **Must Have:** guaranteed to be delivered (max 60% of stories)
- **Should Have:** adds significant value, but not vital (the rest ~20% of stories)
- **Could Have:** has small impact if left out (20% of stories)
- **Won't Have:** not a priority for this iteration

---

## Design

### Flowchart

![Flowchart](docs/readme/P04-flowchart.jpeg)

### Database Schema
The database schema shows the structure of the database, the type and their relationship. This schema was done using 
[Lucid Chart](https://www.lucidchart.com/)

![Database Schema](docs/readme/P04-database-schema.jpg)

### Colour Palette
blabla

![Colour palette](docs/readme/colour-palette.png)

### Typography
For the logo I have used Family Dancing which is a script typeface and looks elegant which matches the rest of the visual identity.
This font was used in some headings such as the homepage in order to embellish it and then for the body copy a readable sans serif, optimal for web design such as Roboto. This last one is also used in the form headings as it is easier to read.
The fonts were taken from Google Fonts:

- [Roboto](https://fonts.google.com/specimen/Roboto)
- [Dancing Script](https://fonts.google.com/specimen/Dancing+Script)

### Imagery

The images are taken from the royalty-free sites credited [here](#Credits).

### Wireframes

Wireframes for desktop, tablet and mobile versions are as follows:

- Home 
![Home]()


### Features

#### Existing Features

**Logo**

- The website visual identity.

![Logo](docs/readme/features/logo.png)

**Nav Bar**

- All pages include a navigation bar

![Nav Bar](docs/readme/features/nav-bar.jpg)

**Footer**

- All pages include a footer with social media links

![Footer](docs/readme/features/footer.jpg)

**Hero Image**

- The home page includes a hero image.

![Hero](docs/readme/features/hero-image.jpg)

**Contact**

- The contact details are presented to the user.

![About us](docs/readme/features/about-the-venue.jpg)

**Books list**

- A list of the bookings is displayed on this page.

![Booking List](docs/readme/features/bookings.jpg)

**Edit books**

- The user can edit their bookings.

![Edit bookings](docs/readme/features/edit-booking.jpg)

**Delete books**

- The user can delete their bookings.

![Delete bookings](docs/readme/features/delete-button.jpg)

**Confirmation message**

- A confirmation message is displayed before deleting a booking.

![Success message](docs/readme/features/confirm-delete.jpg)

**User Feedback**

- The user receives feedback providing messages with relevant information such as their logged in status or booking success as in the example bellow:

![User feedback](docs/readme/features/success.jpg)

---

### Features Left to Implement

In the future, I would like to:

- Add a barcode scanner that can read the book iban and add it to the database.

---

## Technologies Used

### Languages Used

The language used is Python

### Frameworks, Libraries & Programs Used

[Lucid chart](https://www.lucidchart.com/pages/) - Used to create flowcharts.

[Git](https://git-scm.com/) - For version control.

[GitHub](https://github.com/) - To save and store the files for the website.

[Shields](https://shields.io/) - To add badges to the readme file.

[Amiresponsive](https://ui.dev/amiresponsive) - To generate a mockup in different screen sizes.

[Windows photo feature](https://www.microsoft.com/en-us/windows/photo-movie-editor) - To trim screen recording.

[Veed](https://www.veed.io/convert/mp4-to-gif?gad=1&gclid=CjwKCAjwgqejBhBAEiwAuWHioCzHSc5XTTdsnixrxavlvLKEi4i_YeN__Xol0nANQCBhw60caeyF3RoC31wQAvD_BwE) - To convert mp4 to gif

[Heroku](https://id.heroku.com/) - To deploy the App.

[Code Institute template](https://github.com/Code-Institute-Org/p3-template) - To run the game in the terminal using Heroku.

[Django](https://www.djangoproject.com/) - Web Framework.

[Elephantsql](https://www.elephantsql.com/) - PostgreSQL as a Service.

[Cloudinary](https://cloudinary.com/) - For storing static data

## Deployment & Local Development

### Deployment

- This site was deployed by completing the following steps:

####  Django
In order to protect the django app secret key it was set as environment variable and stored in env.py file

####  Heroku
1. Log in to [Heroku](https://id.heroku.com) or create an account
2. Click “New”
3. Click “Create new app”
4. Give your app a name and select the region closest to you. When you’re done, click “Create app” to confirm
5. Open the Settings tab and add the config vars

####  ElephantSQL
1. Log in to [ElephantSQL](https://www.elephantsql.com/) or create an account
2. Click “Create New Instance”
3. Set up your plan
 - Give your plan a Name (this is commonly the name of the project)
 - Select the Tiny Turtle (Free) plan
 - You can leave the Tags field blank
4. Select “Select Region”
5. Select a data center near you
6. Then click “Review”
7. Check your details are correct and then click “Create instance”
8. Return to the ElephantSQL dashboard and click on the database instance name for this project
9. In the URL section, click the copy icon to copy the database URL
10. Paste this URL into env.py file as DATABASE_URL value and save the file.


####  Cloudinary
1. Log in to [Cloudinary](https://cloudinary.com/) or create an account
2. Navigate to dashboard/console https://console.cloudinary.com/console/ and copy API Enviroment variable starting with "cloudinary://".
3. Paste copied url into env.py file as CLOUDINARY_URL value and save the file.


### Local Development

#### How to Fork

To fork the Zest-studi-o/P05-BookZone repository:

1. Log in (or sign up) to Github.
2. Go to the repository for this project, Zest-studi-o/p04-restaurant-booking.
3. Click the Fork button in the top right corner.

#### How to Clone

To clone the Zest-studi-o/P05-BookZone repository:

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, Zest-studi-o/P05-BookZone.
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

---

## Testing

Please refer to [TESTING.md](TESTING.md) file for all testing carried out.

## Credits

### Code Used

- Other students examples helped me to understand the structure of a restaurant booking system app, how to link user stories to epics & what is expected for the README.md such as [project](projecturl)

- [Code Institue](https://learn.codeinstitute.net/ci_program/diplomainsoftwaredevelopmentecomm) walkthrough tutorial "Boutique Ado".

- [Stack overflow](https://stackoverflow.com/) helped me to troubleshoot many of the issues encountered.

- I also researched on [W3 Schools](https://www.w3schools.com/) & [Django Documentation](https://docs.djangoproject.com/en/4.2/).

### Content

- I used [Chapters](https://chaptersbookstore.com/) for books content including images.


### Media

I took from [Pexels](https://www.pexels.com/) and [Freepik](https://www.freepik.com/) the following images:

- [BookZone home page background](https://www.freepik.com/free-photo/modern-bookstore-showcasing-rows-vibrant-books_84718526.htm)


### Acknowledgments

- My Code Institute Mentor.
- Tutor support at Code Institute.
