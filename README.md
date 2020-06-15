# KairuBlog

### Author: [rosekairu](https://github.com/rosekairu)

### Description
 
A python-flask based blogging web-app where users can create and share their opinions and other users can read and comment on them.

## Live Link

[View Site](https://kairublogs.herokuapp.com/)

### Setup/Installation Requirements

* Github and Heroku account - from where the application can be cloned or downloaded
* Git installed in pc - for downloading the application to interact with it locally i.e. on one's device
* Text Editor e.g. Visual Studio or Atom or pycharm - for creating, viewing and editing the code.
* A CLI (Command Line Interface) or terminal where the user can interact with the application using the various python commands e.g. python3.6 run.py or test commands.
* Browser - from where to view and further interact with the application

## Development Installation

To get the code...

1. Clone the repository:

  ```bash
  https://github.com/rosekairu/KairuBlog.git
   ```

2. Move to the folder:

  ```bash
  cd A-SixtySec-Pitch
  ```

3. Install requirements:

  ```bash
  pip install -r requirements.txt
  ```

4.Exporting Configurations:

  ```bash
  export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
  ```

5.Running the application

  ```bash
  python3.6 manage.py server
  ```

6.Testing the application

  ```bash
  python3.6 manage.py test
  ```
 Open the application on your browser `127.0.0.1:5000`

## BDD

| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** | Home,Random Quote, Blogs, Select between SignUp and SignIn|
| Select Register| **Email**,**Firstname**,**Lastname**,**Username**,**Password** | Redirect to signin page |
| Select Login| **Email**, **Password** | Redirect to Login page |
| On Login page load | **On page load** | Redirect to page with Welcome message, Random Quote and Blogs and Subscription option|
| Select add blog button | **If Not LoggedIn** | Redirect to signin page |
| Select add blog button | **If LoggedIn** | Form that you share your Blog post|
| Select comment button | **Comment** | Form that you input your comment|
| Click on submit |  | Redirect to all comments template with your comment and other comments|
| Want to Edit,Delete,or comment on your blog | **If LoggedIn** | Click **username** top right corner, Select **my account** |
| Want to LogOut|  | Click **username** top right corner| Select **my account** |


### Known Bugs

No known bugs

### Technologies Used

1. Python3.6
2. Flask
3. Postgres
4. HTML
5. CSS

### Support and contact details

If you have any comments, suggestions, questions, and/or contributions, please email me at [rosekairu@gmail.com]

### [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/rosekairu/KairuBlog/blob/master/LICENSE) <br>

Copyright (c) **Rose Kairu June 2020**
