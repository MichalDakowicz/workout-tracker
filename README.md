<div align="center" id="top"> 
  <img src="icon.png" alt="Workout Tracker" style="width: 25%;"/>

</div>

<h1 align="center">Workout Tracker</h1>

<p align="center" >
<a href="https://www.python.org/" target="_blank">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"> 
</a>
<a href="https://flask.palletsprojects.com/en/3.0.x/" target="_blank">
    <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"> 
</a>
<a href="https://www.w3.org/html/" target="_blank">
    <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
</a>
<a href="https://www.javascript.com/" target="_blank"> 
    <img src="    https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E">
</a>
<a href="https://www.sqlite.org" target="_blank">
    <img src="https://img.shields.io/badge/Sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white"> 
</a>
<a href="https://github.com/MichalDakowicz" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"> 
</a>
</p>

<h4 align="center">	🚧  Workout Tracker 💪 NOT SUPPORTED ANYMORE 🚧 </h4>

```bash
NOW RELEASED TO THE PUBIC FOR TESTING
WHEN STARTING LOG INTO THE "ADMIN" ACCOUNT USING THE PASSWORD "admin"
TO ADD EXERCISES DELETE USERS ETC. GO TO "http://localhost:5000/admin" OR "http://127.0.0.1:5000/admin"
```

<div align="center">
    A simple web application built with Flask for tracking workouts measuring strength and much more.
</div>

<hr>

## Table of Contents

-   [Introduction](#introduction)
-   [Installation](#installation)
-   [Running the program](#running-the-program)
-   [Features](#features)
    -   [Feature Requests](#feature-requests)
    -   [Feature Plans](#feature-plans)
-   [Usage](#usage)
    -   [Login and Register](#login-and-register)
    -   [Home Page](#home-page)
    -   [Exercise List](#exercise-list)
    -   [Tracking Your Workout](#tracking-your-workout)
    -   [Strength Tracking](#strength-tracking)
    -   [Additional Information](#additional-information)
-   [Contributing](#contributing)
-   [Issues](#issues)
-   [License](#license)

FOR TECHNICAL DOCUMENTATION GO [HERE](technical.adoc)

## Introduction

This Flask Workout Tracker is designed to help users keep track of their workouts. It allows users to register, log in, and record their workouts along with exercises performed.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/MichalDakowicz/workout-tracker.git
    ```
2. Navigate to the project directory:
    ```bash
    cd workout-tracker
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the program

1. Run the Flask application:
    ```bash
    python app.py
    ```
2. Open your web browser and go to http://localhost:5000 or http://127.0.0.1:5000.

## Features

-   User authentication: Register and log in securely.
-   Record and view workouts with date and exercises performed.
-   Strength tracking (not finished yet)
-   More coming soon.

#### Feature Requests

Have a suggestion or want to see a new feature added? Your input is invaluable! Visit GitHub Issues to create a new issue, and mark it as an _"enhancement"_ request. I'll review your proposal with enthusiasm!

#### Feature Plans

1. IMPLEMENTING STRENGTH SCORES 50% (PAGE LEFT)

2. ADDING A PROGRESS PAGE

3. ADDING A USER PROFILE PAGE ✅

4. ADDING PROFILE PICTURE SUPPORT ✅

5. ADD MORE EXERCISES ✅

6. ADD AN SEARCH FOR EXERCISE FIELD IN WORKOUT SECTION

7. BETTER CSS 50%

8. UPDATING THE README WHEN DONE

9. ADD A WORKOUT INFO PAGE FOR WORKOUTS

10. HOME PAGE WORKOUT CALENDAR

11. STRENGTH GRAPH ON PROGRESS PAGE

12. ADD A SEPARATE CATEGORY FOR BODYWEIGHT EXERCISES

13. WORKOUT SUGGESTER FROM BODY PARTS SELECTED (RANDOM EXERCISES)

14. WORKOUT TEMPLATES

15. WORKOUT PRESETS

16. BETTER DATA STRUCTURE FOR STORING WORKOUT DATA ✅

## Usage

#### Login and Register

When you launch the application and navigate to the website, you'll encounter a login form. To log in, enter your username and password, then click the login button.

<br>

![Login Form](readme-images/login.png "Login Form")

_picture of the login page with the login form_

If you're new to the platform, click the register button located below the login form.

<br>

![Register Button](readme-images/register_button.png "Register Button")

_picture of the register button_

You'll be directed to the registration page where you can choose a username and password.

<br>

![Register Form](readme-images/register.png "Register Form")

_picture of the register page with the register form_

Confirm your password by entering it again, then click the register button to complete the registration process. Once registered, you'll be redirected to the login page where you can proceed to log in.

Alternatively, while on the registration page, you can switch back to the login form by clicking the login text below the registration form.

<br>

![Login Button](readme-images/login_button.png "Login Button")

_picture of the login button_

#### Home Page

Upon successful login, you'll be directed to the home page. Here, you'll find a concise overview of your past training sessions.

<br>

![Home page](readme-images/home.png "Home Page")

_picture of the home screen with the workout history panel_

When you do a workout it will display a simple overview of it inside the _"Workout history"_ panel.

<br>

![Home page with a workout](readme-images/home_with_workout.png " Home Page With an Existing Workout")

_picture of the home screen with the workout history panel with a workout_

#### Exercise List

To access the list of exercises, click the _"Exercises"_ button at the top of the page. You'll be taken to a webpage where exercises are categorized by muscle group, along with specific muscle targeting information.

<br>

![Exercises](readme-images/exercises.png "Exercises Page")

_picture of the exercise list (not the whole list added yet)_

#### Tracking Your Workout

Navigate to the _"Workout"_ page by clicking the corresponding button on the top navigation bar. Here, you can track your workout sessions.

1. Select an exercise from the list.

2. Input the number of sets and click _"Confirm"_.

3. Enter the number of reps and weight for each set.

    **Please note: Ensure all fields are accurately filled out before saving your workout.**

4. Click _"Confirm"_ to add the exercise to your workout.

5. Repeat the process for each exercise you wish to include.

6. Once finished, click the _"Save"_ button at the bottom of the list to record your workout.

#### Strength Tracking

On this dedicated page, diligently input all relevant data into the provided form. After entering the necessary information, click the _"Confirm"_ button to process your input. Subsequently, you'll witness your results meticulously displayed as a comprehensive strength level analysis.

#### Additional Information

Please note that any unsaved changes made on the _"Workout"_ page will not be retained once you leave the page.

To return to the home page at any time, simply click the _"Home"_ button located at the top of the page. This will swiftly redirect you back to the home page, allowing for seamless navigation throughout the application.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-branch
    ```
3. Make your changes.
4. Commit your changes:
    ```bash
    git commit -am 'Add new feature'
    ```
5. Push to the branch:
    ```bash
    git push origin feature-branch
    ```
6. Create a new pull request.

## Issues

Encountered a bug or have an issue with the application? Please head to GitHub Issues and click on the _"New Issue"_ button. Specify your problem in detail, and make sure to select _"bug"_ as the label. Rest assured, I'll strive to address it promptly.

## License

This project is licensed under the **[MIT License](LICENSE)**

<hr>
<a href="#top">Back to top</a>

&#xa0;

Made with :heart: by <a href="https://github.com/MichalDakowicz" target="_blank">Michu</a>
