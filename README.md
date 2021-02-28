<h1 align="center">Your PMP Journey</h1>

<img src="/static/img/intro.png">

<h2 align="center">Introduction</h2>

Sligo PMI Training is an approved provider of project management training by the Project Management Institute (PMI). As a PMI Authorized Training Partner (ATP), our training courses have been reviewed against PMI's Quality Assurance guidelines.

For Sligo PMI Training to gain accreditation for its educational programmes, accreditation bodies carefully evaluate and verify that Sligo PMI Training meets and exceeds their rigorous quality criteria for course content, qualified instructors, instructional design, verified learning outcomes and maintenance of the highest standards of professional and ethical business practices.

PMP certification can be extremely valuable if you plan to advance in the current company you are working at. It puts you way ahead of your colleagues in terms of moving up the career ladder. Also, a certified manager can do much better in a gruelling project management interview than a non-certified one.

The fail rate for the PMP exam is quite high at an estimated 40-50% for first-time test-takers. There is no specific number of questions that must be answered correctly in order to pass the PMP exam.  This is high and can be a costly journey.  

Anyone who aspires to attain PMP certification should be prepared for the exam. Consequently, first-time test takers should also be advised that the PMP certification exam is extremely difficult. The exam consists of 200 multiple-choice questions in a period of only four hours.

<h2 align="center">Table of Contents</h2>

- [1. User Experience (UX)](#1-user-experience--ux-)
  * [Project Goals](#project-goals)
  * [User Stories](#user-stories)
  * [Design Choices](#design-choices)
    + [Colour Scheme](#colour-scheme)
    + [Imagery](#imagery)
    + [Font & Icons](#font---icons)
  * [Wireframes](#wireframes)
- [2. Features](#2-features)
  * [Navbar](#navbar)
  * [Footer](#footer)
  * [Home Page](#home-page)
    + [Hero Carousal](#hero-carousal)
    + [Customer Testimonials](#customer-testimonials)
    + [Product Reviews](#product-reviews)
  * [Contact Us Page](#contact-us-page)
  * [About Us Page](#about-us-page)
  * [Products Page](#products-page)
  * [Products Details](#products-details)
  * [Courses Page](#courses-page)
  * [Course Details](#course-details)
  * [Shopping Basket](#shopping-basket)
  * [Checkout](#checkout)
    + [Order Summary](#order-summary)
    + [Customer Details](#customer-details)
  * [Checkout Success](#checkout-success)
  * [Order Confirmation Email](#order-confirmation-email)
  * [Profile Page](#profile-page)
  * [Product Management](#product-management)
  * [Django-allauth features](#django-allauth-features)
    + [Sign Up](#sign-up)
    + [Sign In](#sign-in)
  * [404 and 500 error pages](#404-and-500-error-pages)
  * [Features Left to Implement](#features-left-to-implement)
- [3. Information Architecture](#3-information-architecture)
  * [Database choice](#database-choice)
  * [Data Modelling](#data-modelling)
- [4. Technologies Used](#4-technologies-used)
  * [Languages](#languages)
  * [Libraries & Frameworks](#libraries---frameworks)
  * [Tools](#tools)
  * [Databases](#databases)
- [5. Testing](#5-testing)
  * [Validators](#validators)
    + [Html](#html)
    + [CSS](#css)
    + [JavaScript](#javascript)
    + [Python](#python)
    + [Compatibility and Responsiveness](#compatibility-and-responsiveness)
- [6. Deployment](#6-deployment)
  * [Local Deployment](#local-deployment)
  * [Deployment to Heroku](#deployment-to-heroku)
    + [Hosting media files with AWS](#hosting-media-files-with-aws)
    + [Sending email via Gmail](#sending-email-via-gmail)
    + [Google Maps API key set up](#google-maps-api-key-set-up)
- [7. Code & Credits](#7-code---credits)
- [8. Acknowledgements](#8-acknowledgements)
# 1. User Experience (UX)

-   ## Project Goals

The Journey to accomplishing the PMP (Project Management Professional) accreditation is not easy. It requires hours of study and that’s after you complete the PMI® Authorized PMP® Exam Prep 5 day course. This website is a guide to persons on the PMP trial. It provides plenty of study resources suggestions in our Products section and of course we offer the first step, the PMI® Authorized PMP® Exam Prep 5 day course. The main objective in creating the PMP Journey application is to provide the user with a simple to use e-commerce site, with filtering of Products & Courses by Price, Category & Author. Ability to book Courses by date. The PMP Journey application also offers authenticated users the option to add Product Reviews and Course Testimonials.

     
-   ## User Stories
  
ID | As a          |  I want to be able to | So that I can
------------  | ------------- |  ------------        | -------------
||| **Viewing and Navigation**          
1 | Shopper | View Website easily on all my Devices | Ensure the websites usability no matter what device
2 | Shopper | View a list of Products & Courses | Select Products & Courses to Purchase
3 | Shopper | View individual Product & Course Details | Select Courses & Products to Purchase
4 | Shopper | View Site Users Product Reviews & Customer Rating | Make a better choice by reading what Site User shared about their purchases and average Customer rating for each product
5 | Shopper | View Site Users Course Testimonials | Make a better choice by reading what Site User Course Testimonials
6 | Shopper | Easily view the total of my purchases at each stage | Make sure I dont overspend
7 | Shopper | To read about the Business | Decide if I am going to find what I am looking for
8 | Shopper | Contact the Business Owners| Submit any queries I have regarding Products & Courses
  ||| **Registation and User Accounts**
9 | Site Users | Easily Register for an account | Have a personal account and be able to view my profile
10 | Site Users | Easily Login & logout to my account | Access my personal account information
11 | Site Users | Add Product Reviews & Rating | Help others make a better choice by reading about your purchases and the average Customer rating for each product
12 | Site Users | Add Course Testimonials  | Help others make a better choice by reading your Course Testimonial
13 | Site Users | Easily recover my password if I forget | Recover access to my account
14 | Site Users | Receive email confirmation when I register | Verify that my account registration was successful
15 | Site Users | Be personalised User | View and edit my profile details and view my order history
16 |  Site Users | Receive email order confirmation | Record of my transaction
  ||| **Sorting & Searching**
17| Shopper| Sort the list of available Products | Easily identify by Price (high to low), by Author (A-Z), by Customer (A-Z), by Category (Books or On Demand Videos)
18| Shopper| Sort the list of Courses | Easily identify by Price (high to low), by provider (A-Z)
19| Shopper| Search for a Product by name or description | Find a specific product I would like to purchase or attend
20| Shopper| Easily see what I searched for and the number of results | Quickly find if the product I am looking for is available
  ||| **Puchasing and Checkout**
21| Shopper| Easily select the quantity of a product when purchasing it | Ensure I dont accidently select the wrong product or quantity of product
22| Shopper| Easily select the number of participants for a Course if applicable | Ensure I dont accidently select the wrong Course or number of participant’s
23| Shopper| Easily select the number months I want to subscribe to On Demand Videos | Ensure I dont accidently select the wrong number of month's
24| Shopper| View items in my basket to be purchased | View the total cost of my purchase an all items I will receive
25| Shopper| Adjust the quantity of products in the basket |Easily make changes to my product selected for purchase before checkout
26| Shopper| Adjust the no of participants for Course in the basket | easily make changes to my Courses selected for purchase before checkout
27| Shopper| Easily enter my payment information | Checkout smoothly and quickly
28| Shopper| Feel my payment information is safe & secure | Confidentally provide the information needed for the purchase
29| Shopper| Receive an email confirmation after checkout | Ensure sure the payment was successful & retain the confirmation of what I purchased
 ||| **Admin and Product Management**
30| Shop Owner| Conveniently and securely access admin section | easily maintain the Website
31| Shop Owner| Add a Product or Course | Add new Products & Courses to my shop
32| Shop Owner| Add Course Available Dates | Maintain Course dates 
33| Shop Owner| Edit/Update a Product or Course | Change any of the criteria for any Product or Courses in my shop
34| Shop Owner| Delete a Product or Course | Remove Products or Courses from my shop
35| Shop Owner| Delete a Customer Review or Testimonial | Remove a Customer Review or Testimonial from my shop
36| Shop Owner| Receive emails from Users when they submit the contact form | Reply to User queries

-   ## Design Choices
  
   -   ### Colour Scheme
        - The orange NavBar is eye catching and and the orange text in the footer pulls the two elements together.  
        - There is alot of whitespace in the Product and Course, Basket and Checkout Pages.  The whitespace draws attention and attracts the user to the eyecatching buttons             and good quality images
    
   -   ### Imagery 
       I selected images that are relevant to the content of the application.  
      
      
   -   ### Font & Icons 
       - I selected Josefin Sans for consistent font throughout the Site 
       - The icons in the navbar are a good fit for the theme of the application
       - Icons break up the information visually, creating space for the user and not overwhelming them with too much info at once.     

-   ## Wireframes
    
    Wireframes were built in the early stages of development to get a rough outline of the structure needed for the planned features of the site. The wireframes were created     using Balsamiq. These can be viewed below:

    -   Desktop & Tablet - [View](data/wireframes/desktop_tablet.pdf)
    -   Mobile - [View](data/wireframes/mobile.pdf)
         
# 2. Features

-   ## Navbar
-    For Visitors to the site, the following links are available in the Navbar - 
       - Log in
       - Register
      The navigation bar features the PMP Journey logo in the top left corner and aslo search option for visitors.
      
     <img src="/static/img/nav_u.png">
     
 -    For Users, the following links are available in the Navbar - 
       - My Profile
       - Add Testimonial
       - Log Out
       
      <img src="/static/img/nav_login.png">
    
-    For Super Users, the following links are available in the Navbar - 
       - My Profile
       - Product Management
       - Add Testimonial
       - Log Out
       
     <img src="/static/img/nav_super.png">
 

 -   The navbar is collapsed into a burger icon on small screens
     
     <img src="/static/img/nav_sm.png">
 
 
-   ## Footer

-   The footer consists of useful links for Visitors & Users

     <img src="/static/img/footer_lg.png">
     
-   The footer is responsive on small devices

     <img src="/static/img/footer_sm.png">
     
-   ## Home Page 

    ### Hero Carousal
-  The Hero images consist of one lady running to suggest a journey like the PMP trail.  The other image is a lady studying happily.  There is a 'View Our Products' button.
    
    <img src="/static/img/car_lg.png">
    
-   Hero Carousal on small device:
    
    <img src="/static/img/car_sm.png">
        
     ### Customer Testimonials
-    Registered site Users have the option to add a Testimonial.  Our Customer Testimonials are rendered from the Testimonial app and displayed in a carousal.  Testimonials are maintainable in the Admin                section.    
     
     <img src="/static/img/test_lg.png">
      
-   Customer Testimonials on small device:
    
    <img src="/static/img/test_sm.png">
    
    Registered User can access the Add Testimonial form from the NavBar.  As registered Users, their User ID is captured from the User Model
    
-   Add Testimonials on large device:
    
    <img src="/static/img/test_add_lg.png">
      
-   Add Testimonials on small device:
    
    <img src="/static/img/test_add_sm.png">   
    
    
     ### Our Courses
-    This section showcases our Courses and Course Availability.  Our Course Availability is rendered from the DatesAvailable Model in the Products app.  Course Availability      is maintainable from the Admin section.    
     
      <img src="/static/img/course_lg.png">
      
-   Our Courses on small device :
    
    <img src="/static/img/course_sm1.png">
    <img src="/static/img/course_sm2.png">

    ### Product Reviews
-    Registered site Users have the option to add a Product Review.  Our Product Reviews are rendered from the ProductReview Model in the Products app and displayed in a           carousal.  Product Reviews are maintainable in the Admin section.  

     <img src="/static/img/review_lg.png">
     
-   Product Reviews on small device:
    
    <img src="/static/img/review_sm.png">
   
-    Our Product rating is the average customer rating for that product, calculated in the Product Model with the following function - 

     <img src="/static/img/rating.png">
     
-   Registered User can access the Add Review from the Product Detail page.  As registered Users, their User ID is captured from the User Model.
    
-   Add Product Review on large device:
    
    <img src="/static/img/review_add_lg.png">
      
-   Add Product Review on small device:
    
    <img src="/static/img/review_add_sm.png">        

-    Visitors can view the Products reviews for each product in the Products Details page, but are unable to submit a review.

     <img src="/static/img/review_visitor.png">  

-   ## Contact Us Page

-   The Contact Us page consists of two sections side by side, the Contact Us form and our Contact Details and location on Google Maps.

     <img src="/static/img/contact.png">  
     
     - The Contact Us form is accessible to both Visitor and Registered Users.  For Registered Users the Full Name Field and email will be populated automatically from the          Profile model. An email will be sent to the admin of the website with django send_mail() functionality.
     - The Contact details area provides company's Name & Address, phone number and email, along with a map showing Sligo PMP Training location. When User clicks on the red          marker, company name pops up. Google Map API was used to display locations lat & long.
     
-    Once email is submitted successfully, User will get a message to screen - 
     
      <img src="/static/img/contact_success.png">  

     - The register page allows user's to create a new account. The user is asked to fill the fields "username","firstname","password" and "confirm password". When adding a             username, the code compares it against existing usernames to ensure that it is unique. A username must be 3-15 characters long. 
     - The password field is a required field. The "confirm password" field must match the original password. All passwords are hashed for security purposes. If user's         input does not meet requirements, flash messages will inform a user about the error. When the form is submitted successfully, a user is redirected to the home page and           informed that account was created. There is also a link to the login page for existing users at the bottom of the Registration form.
    
-   ## About Us Page
      The User learns in the About page that Sligo PMI Training is an approved provider of project management training by the Project Management Institute (PMI), as a person      who wishes to complete the PMP Training been an approved provider is a must.
      
      <img src="/static/img/about.png">  

  
  -   ## Products Page
     
   The "All products" page displays each Product card.  The Product card contains the following Product information - Image, Category, Name, Customer Rating, Price & Type.      The User can see at the top right of the page how many Products are available.  In the top left of the page the User can sort the Products by - Price, Name, Category &        Author.  When User clicks on the Product image they are redirected to the Product Details page.
     
   <img src="/static/img/products.png">  
     
  -   ## Products Details
     
  The Product Details page contains the following Product information - Details, Image, Category, Name, Customer Rating, Price & Type.  In the Product Detail page the User      can enter the Quantity of the Product they wish to Purchase and add the Product to their basket.  The Product Detail page also gives the Registered User the option to        Add a Product Review.
     
   <img src="/static/img/products_detail.png">
 
 If the Category of the Product selected is'On Demand Video', then this means the price is a monthly subscription
 
 <img src="/static/img/products_video.png">
     
  -   ## Courses Page
     
   The "All Courses" page displays each Course card.  The Course card contains the following Course information - Image, Name & Description.  The User can see at the top right of the page how many Courses are available.In the top left of the page the User can sort the Courses by - Price, Name & Author.  When User clicks on the Course image they are redirected to the Course Details page.
     
   <img src="/static/img/courses.png">  
     
  -   ## Course Details
     
  The Course Details page contains the following Course information - Details, Image, Name & Price.  On the Course Detail page the User will select from the Dates Available dropdown the date they would like to start the course.  The Dates Available for each course is rendered to the Product Details page from the Dates Available model in the Product App.  The User will also enter the number of persons they are booking the course for.
     
   <img src="/static/img/courses_detail.png">      
        
   Once the User clicks 'Add to Basket', they will be prompted with success confirmation message that Course has been added to basket with the Date Booked for and the number    of participants
     
   <img src="/static/img/courses_basket.png">   
     
    
-   ## Shopping Basket

     The Users shopping basket will contain all items.  If the item is a product it will detail the Name, Type & Quantity.  If the item has a Product Category of 'On Demand        Video' then the number months subscription selected will be visible.  If the item is a Course, the Start Date selected will be visible along with the number of                participants selected.

     <img src="/static/img/basket_total.png">  
     
-   ## Checkout

      The Checkout page contains 2 section: The Customer Details & the Order Summary. 
      
       ### Order Summary
     In the Order Summary, if the item is a product it will detail the Name, Type & Quantity.  If the item has a Product Category of 'On Demand Video' then the number months      subscription selected will be visible.  If the item is a Course, the Start Date selected will be visible along with the number of participants selected.
     The Order Summary also contains the Total Cost, Delivery Cost & the grand Total.
    
    ### Customer Details
     If a user already has a profile with the shipping information saved, the form will be pre-populated with this information.
     The User is informed how much the card will be charged in the paragraph below the Proceed to payment button.
     The user must provide card number, expiration date and CVC.  For Testing purposes, card number 4242 4242 4242 4242 is used for successful stripe payment.
     A webhook is used to make sure that the order is processed even in the cases when the payment process is interrupted (e.g. if a user accidentally closes the page or          browser after clicking "Proceed to payment" button).
     
     <img src="/static/img/basket_checkout.png">
       
  ## Checkout Success
  
   Once the form is submitted and the payment is successfully proceeded, the Checkout success page is loaded and a confirmation email is sent to the user's email.  A           toast message appears to inform the user that the order was processed successfully.
      
   <img src="/static/img/basket_checkout_success.png">
     
  ## Order Confirmation Email 
  
  The Order Confirmation Email has been configured to display the Course details.  

  <img src="/static/img/order_mail.png">
  
  If the order has only Course bookings then the shipping details will not be included in the email.
  
  <img src="/static/img/order_mail_course.png">
      
## Profile Page
   The Profile page is only available to authenticated users.

   The Profile page contains the Users Default Delivery Information.  User can update their Profile Information.
   
   The Users Order History is also available and each Order contains a link that will redirect the User to the Order History page.
   
   <img src="/static/img/profile.png">
   
## Product Management

The Product Management feature is available only to Superusers. The application allows SuperUsers to add new products, edit products & delete products.  If the form is valid, the product is added to the database and the user is redirected to the newly created product details page.  

## Django-allauth features

### Sign Up
The sign up page allows a user to create a new account. The user is asked to fill the fields "email", "username", "password" and "password (again)".  When the form is submitted, a verification email is sent to the user's email to verify the email and complete the Sign Up process.  There is also a link to the login page for existing users at the bottom of the form.

<img src="/static/img/signup.png">

### Sign In
In The Sign In form User must populate "username" and "password" fields. If the login was successful, a user is redirected to the home page and the toast success message appears confirming a successful Sign In.
There is a link to the sign up page for new users at the bottom of the form.  There is also a link to the forgot password functionality.

<img src="/static/img/signin.png">

## 404 and 500 error pages
The website contains the following basis  404 and 500 pages  Each page contains a heading, information about the error and a "Home" and a "Contact Us" button. 


<img src="/static/img/404.png">
<img src="/static/img/500.png">

## Features Left to Implement

I would like to allow User to Edit / Delete their Reviews and Testimonial.  At the moment this is only possible from the Django Admin Area.  I would also like to render the Users testimonial & Reviews to their User Profile page

 
# 3. Information Architecture
## Database choice

During the development phase I worked with sqlite3 database which is installed with Django.  For deployment(production), a PostgreSQL database is provided by Heroku as an add-on.

## Data Modelling
The User model is provided by Django as a part of defaults django.contrib.auth.models.

The following apps were created for this website -  About, Bag, Checkout, Contact, Home, Products, Profiles & Testimonials.

- The Products App contains the following Models - Product, Category, ProductReview & DatesAvailable.
- The Checkout App contains the following Models - Order & OrderLineItem

The following is the websites ERD (Entity Relationship Diagram) - 

 <img src="/static/img/ERD.png">
 
 The following is description of the websites Model Relationships - 
 
  <img src="/static/img/ERD_DETAIL.PNG">

# 4. Technologies Used

## Languages
-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://www.javascript.com/)
-   [Python](https://www.python.org/)
-   [Jinja](https://jinja.palletsprojects.com/en/2.10.x/)

## Libraries & Frameworks
- [Django](https://www.djangoproject.com/) - Python framework for building the project.
- [Bootstrap](https://www.bootstrapcdn.com/) - The front-end framework for layout and design.
- [Google Fonts](https://fonts.google.com/) - To import fonts.
- [FontAwesome](https://fontawesome.com/) - Provide icons used across the project.
- [Gunicorn](https://pypi.org/project/gunicorn/) - A Python WSGI HTTP Server to enable deployment to Heroku.
- [Psycopg2](https://pypi.org/project/psycopg2/) - Enable the PostgreSQL database to function with Django.
- [Stripe](https://stripe.com/ie) - Handle financial transactions.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Style Django forms.
- [Google Maps JavaScript API](https://developers.google.com/maps/documentation/javascript/overview)- Render the map in Contact page.

## Tools
- [GitPod](https://www.gitpod.io/) - Online IDE for developing this project.
- [Git](https://git-scm.com/) - Version control.
- [GitHub](https://github.com/) - Remotely storing project's code.
- [PIP](https://pip.pypa.io/en/stable/installing/) - Installation of necessary tools.
- [Pillow](https://python-pillow.org/) - Saving image file formats
- [Heroku](https://dashboard.heroku.com/apps) - Host the project.
- [AWS S3 Bucket](https://aws.amazon.com/) - Store static and media files in prodcution.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - Compatibility with AWS.
- [GIMP](https://www.gimp.org/) - Flipping, Editing & Resizing images.
- [Balsamiq](https://balsamiq.com/) - Create wireframes.
- [Draw.io](https://app.diagrams.net/) - Create ERD Diagram.
- [Am I responsive](http://ami.responsivedesign.is/) - Testing & Displaying responsivness.
- [PEP 8 Online Validator](http://pep8online.com/)- Check Python code.
- [W3C Validator](https://validator.w3.org/)- Check the validity HTML and CSS.
- [Online JavaScript Beautifier](https://beautifier.io/)- Beautift HTML and JavaScript.
- [GitHub Wiki TOC generator](https://ecotrust-canada.github.io/markdown-toc/)- Generate MarkDown TOC.
- [AOS](https://michalsnik.github.io/aos/)- Animate Elements.

## Databases
- [SQlite3](https://www.sqlite.org/index.html) - a development database.
- [PostgreSQL](https://www.postgresql.org/) - a production database.


# 5. Testing

The application was tested to ensure it successfully met the expectations of each User Story without error.  Please view the Executed Test Protocol in link below - 

 -   Executed Test Protocol - [View](Test_Protocol/Test_Scripts_performed.pdf)
    
## Validators

### Html

All the HTML files were tested through W3C Markup Validation Service.

### CSS

CSS files were tested through W3C CSS Validation Service.

### JavaScript

Script files were tested through W3C CSS Validation Service. 


### Python

All python files were tested through PEP8 Online validator. 


### Compatibility and Responsiveness

 I used the Google Chrome's developer tools to see how it looks across all the different device screen sizes to ensure compatibility and responsiveness.
 I also used Am I Responsive online tool for checking responsiveness on different devices.
 
# 6. Deployment

## Local Deployment

1. Running Code Locally Follow this [link](https://github.com/bridcourtney/Your_PMP_Journey) to my Repository on Github and open it.
2. Click Clone or Download.
3. In the Clone with HTTPs section, click the copy icon.
4. In your local IDE open Git Bash.
5. Change the current working directory to where you want the cloned directory to be made.
6. Type git clone, and then paste the URL you copied earlier.
7. Press enter and your local clone will be ready.
8. Create and start a new environment:
python -m .venv venv
source env/bin/activate
9. Install the project dependencies:
pip install -r requirements.txt
10. Create a new file, called env.py and add your environment variables:
import os
os.environ.setdefault("STRIPE_PUBLISHABLE", "secret key here") os.environ.setdefault("STRIPE_SECRET", "secret key here") os.environ.setdefault("DATABASE_URL", "secret key here") os.environ.setdefault("SECRET_KEY", "secret key here") os.environ.setdefault("AWS_ACCESS_KEY_ID", "secret key here") os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "secret key here")
11. Go to settings.py file and add your environment variables.
12. Add env.py to .gitignore file
13. Go to terminal and run the following: python3 manage.py makemigrations, then python3 manage.py migrate to migrate all existing migrations to postgres database.
14. Create a superuser: python3 manage.py createsuperuser
15. Run it with the following command:
python manage.py runserver
16. Open localhost:8000 on your browser
17. Add /admin to the end of the url address and login with your superuser account and create new products.

## Deployment to Heroku
The following steps are required to deploy this site to Heroku:

1. Create a new app in Heroku with a unique name, chose your region
2. Go to Resources, within Add-ons searched Heroku Postgres, choose Hobby Dev - Free version, then click Provision button.
3. In Settings click on Reveal Config Vars button, and copy the value of DATABASE_URL
4. Return to terminal window and run sudo pip3 install dj_database_url
5. Run sudo pip3 install psycopg2. Create a requirements.txt file using the terminal command pip3 freeze > requirements.txt
6. Go to settings.py and add import dj_database_url and updated DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))} also update env.py with os.environ.setdefault("DATABASE_URL", "postgres://postgres key - copied earlier from Heroku")
7. Run python3 manage.py makemigrations, then python3 manage.py migrate to migrate all existing migrations to postgres database.
8. Create a superuser: python3 manage.py createsuperuser
9. Log into Amazon AWS, Go to S3 and create a new S3 bucket.
10. Return to terminal window and run sudo pip3 install django-storages and sudo pip3 install boto3.
11. In settings.py add storages to INSTALLED_APPS.
12. In settings.py add the following lines:

AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }
    # Bucket Configuration
    AWS_STORAGE_BUCKET_NAME = 'pmp-journey'
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

13. Update env.py with AWS keys (these keys are from S3).
14. Create custom_storages.py at the top level:
15. From django.conf import settings
16. From storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
   location = settings.STATICFILES_LOCATION

class MediaStorage(S3Boto3Storage):
   location = settings.MEDIAFILES_LOCATION

17. Go to settings.py and add:
STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'

MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

18. Return to terminal window and run python3 manage.py collectstatic
19. Return to Heroku. In Settings click on Reveal Config Vars button, and add the following config vars from env.py:   

Key           | Vavue         | 
------------  | ------------- |
 AWS_ACCESS_KEY_ID |secret key here | 
 AWS_SECRET_ACCESS_KEY |secret key here | 
 DATABASE_URL |secret key here |
 USE_AWS |1| 
 SECRET_KEY |secret key here| 
 STRIPE_PUBLIC_KEY |secret key here|
 STRIPE_SECRET_KEY |secret key here|
 STRIPE_WH_SECRET |secret key here|
 EMAIL_HOST_PASS |secret key here|
 GOOGLE_MAP_API_KEY |secret key here|
 EMAIL_HOST_USER |host.@mail.com|

20. Click to Deploy, then GitHub, search for repository and click to connect button.
21. Return to terminal window and run sudo pip3 install gunicorn and add to requirements.txt
22. Create a Procfile using the following command: echo web: gunicorn ms4.wsgi:application
22. Run git add ., git commit -m "my commit message" and git push commands to push all changes to GitHub repository.
23. Return to Heroku and hit Deploy Branch
24. Once the build is complete, click on Open app
25. Go to settings.py and add pmp-journey.herokuapp.com to ALLOWED_HOSTS
26. Run git add ., git commit -m "my commit message" and git push commands to push all changes to GitHub repository.
27. Returned to Heroku and hit Deploy Branch again.

### Hosting media files with AWS

The static files and media files (that will be uploaded by superuser - product images) are hosted in the AWS S3 Bucket. To host them, you need to create an account in AWS and create your S3 basket with public access.

### Sending email via Gmail

To send real emails from the application, you need to connect it to your Gmail account, setting up your email address in EMAIL_HOST_USER variable and your app password generated by your email provider in EMAIL_HOST_PASS variable.

### Google Maps API key set up
1. In the Google Cloud Platform Console create a new project.
2. Click Continue to enable the API and any related services.
3. Get an API key and set the API key restrictions on the Credentials page. 
4. Add your Google Maps key into the environment variable locally in the env.py file:
5. os.environ["GOOGLE_MAP_KEY"] = "<Your Google Map key>" and in production in the Heroku Config Vars as GOOGLE_MAP_KEY.

# 7. Code & Credits
 - The idea of Google Map API in Contact Form was inspired from https://github.com/irinatu17/Art-of-Tea
 - The idea to flag course by Boolean is_a_service in the Product Model was inspired from https://github.com/irinatu17/Art-of-Tea
 - The project's code was developed by following the Code Institute lessons for the Boutique Ado Django Mini-Project, and customised to meet the requirements of my project

# 8. Acknowledgements

-   My Mentor Brian Macharia for continuous helpful feedback, excellent support material and very productive mentoring sessions

-   Tutor support at Code Institute for their support.
