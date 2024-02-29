# Flask Workout Tracker

A simple web application built with Flask for tracking workouts.

## THE PROGRAM IS STILL A WORK IN PROGGRESS AND THE UI ISN'T COMPLETE THE READNME ME TOO

<!-- Technologies: In the introduction or a separate section, briefly mention the technologies used (Python, Flask, database).

Future Plans: If you have a roadmap for additional features, include a section titled "Planned Features" or "Future Development" to let users know what they can look forward to. -->

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Running the program](#running-the-program)
- [Features](#features)
- [Usage](#usage)
   - [Login and Register](#login-and-register)
   - [Home Page](#home-page)
   - [Exercise List](#exercise-list)
   - [Tracking Your Workout](#tracking-your-workout)
   - [Strength Tracking](#strength-tracking)
   - [Additional Information](#additional-information)
- [Contributing](#contributing)
- [Issues](#issues)
- [Feature Requests](#feature-requests)
- [License](#license)

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
2. Open your web browser and go to http://localhost:5000 or the ip adress given during the starting process of the program.

## Features

- User authentication: Register and log in securely.
- Record and view workouts with date and exercises performed.
- Strength tracking (currently broken)
- More comming soon.

## Usage

#### Login and Register

When you launch the application and navigate to the website, you'll encounter a login form. To log in, enter your username and password, then click the login button.

<br>

![Login Form](readme-images/login.png "Login Form")
*picture of the login page with the login form*

If you're new to the platform, click the register button located below the login form.

<br>

![Register Button](readme-images/register_button.png "Register Button")
*picture of the register button*

You'll be directed to the registration page where you can choose a username and password. 

<br>

![Register Form](readme-images/register.png "Register Form")
*picture of the register page with the register form*

Confirm your password by entering it again, then click the register button to complete the registration process. Once registered, you'll be redirected to the login page where you can proceed to log in.

Alternatively, while on the registration page, you can switch back to the login form by clicking the login text below the registration form.

<br>

![Login Button](readme-images/login_button.png "Login Button")
*picture of the login button*

#### Home Page

Upon successful login, you'll be directed to the home page. Here, you'll find a concise overview of your past training sessions.

<br>

![Home page](readme-images/home.png "Home Page")
*pcture of the home screen with the workout history panel*

When you do a workout it will display a simple overwiew of it inside the *"Workout history"* panel.

<br>

![Home page with a workout](readme-images/home_with_workout.png " Home Page With an Existing Workout")
*picture of the home screen with the workout history panel with a workout*


#### Exercise List

To access the list of exercises, click the *"Exercises"* button at the top of the page. You'll be taken to a webpage where exercises are categorized by muscle group, along with specific muscle targeting information.

<br>

![Exercises](readme-images/exercises.png "Exercises Page")
*picture of the exercise list (not the whole list added yet)*

#### Tracking Your Workout

Navigate to the *"Workout"* page by clicking the corresponding button on the top navigation bar. Here, you can track your workout sessions.

1. Select an exercise from the list.

2. Input the number of sets and click *"Confirm"*.

3. Enter the number of reps and weight for each set.

   **Please note: Ensure all fields are accurately filled out before saving your workout.**

4. Click *"Confirm"* to add the exercise to your workout.

5. Repeat the process for each exercise you wish to include.

6. Once finished, click the *"Save"* button at the bottom of the list to record your workout.

#### Strength Tracking

On this dedicated page, diligently input all relevant data into the provided form. After entering the necessary information, click the *"Confirm"* button to process your input. Subsequently, you'll witness your results meticulously displayed as a comprehensive strength level analysis.

#### Additional Information

Please note that any unsaved changes made on the *"Workout"* page will not be retained once you leave the page.

To return to the home page at any time, simply click the *"Home"* button located at the top of the page. This will swiftly redirect you back to the home page, allowing for seamless navigation throughout the application.

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

Encountered a bug or have an issue with the application? Please head to GitHub Issues and click on the *"New Issue"* button. Specify your problem in detail, and make sure to select *"bug"* as the label. Rest assured, I'll strive to address it promptly.

## Feature Requests
Have a suggestion or want to see a new feature added? Your input is invaluable! Visit GitHub Issues to create a new issue, and mark it as an *"enhancement"* request. I'll review your proposal with enthusiasm!

## License

This project is licensed under the **[MIT License](LICENSE)**