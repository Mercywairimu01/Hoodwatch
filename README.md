
## Hoodwatch
Hoodwatch Application
## Author
Martin Misigo<br>
Mercy wambui
## Description
This a django web application that allows registered users to know about everything happening in your current neighborhood.
---
## Behaviour Driven Development(BDD)
Behaviour   Input   Output
* The program navigates to the authentication page  Load the application    Navigate to the login/register page
Navigate to the Registration Page   Click on Register link  A registration form is displayed
If registration is successful navigate to login page    Click on Login Link Application navigates to the homepage where posts are displayed
* A post creation form is displayed with the empty fields. After saving the user is redirected to homepage to view the posts.   Click on create post button and submit button   A form with post picture,name,description is displayed.
* Application navigates to the business creation form . After saving user is redirected to all businesses page. Click on create business button A form with business name,email and hood name is displayed.A submit button is also displayed.
* All user details including the name, posts and businesses created by the user are displayed   User clicks on the Profile link A User profile with all info pertaining the user is displayed.
* An Edit Form is displayed to update user info.    Use clicks the edit profile button, makes changes and submits the form  A user edit form with update fields is shown to the user to enable them update necessary info.
* A list of all businesses in that neighbourhood is displayed with all the information  User clicks on View businesses link on the navbar   All businesses are displayed in that particular neighbourhood
* User is logged out of the application User clicks on the Logout dropdown  User logged out and redirected to the register/login page.
---

## Project Setup instructions
Use the following commands to use this project.
git clone https://github.com/Mercywairimu01/Hoodwatch.git
install python3.9

cd Hoodwatch
Navigate to the virtual environment using source virtual/bin/activate
atom . //For those using atom text editor.
code . //For those using Visual Studio editor.
### Install dependancies
Install dependancies that will create an environment for the app to run pip install -r requirements.txt

Use the package manager pip to install all project requirements. 
```sh
(virtual) $ pip install -r requirements.txt
```
### Installing

To get a development env running, use the **.env.example** file to create a **.env** file with appropriate values

### Running the tests

Run automated tests for this system

```sh
(virtual) $ python3 manage.py test hood
```
1. IDE of Choice
2. Python3
3. Browser

* Please ensure you're working from a Windows/MacOS/Linux
* Install Django through `pip install django`

Run python3.6 manage.py runserver
Access the application on this localhost address http://127.0.0.1:8000

## Technologies used
* The different technologies that were used to develop this program include:
1. Python3.9
2. Bootstrap
3. HTML
4. CSS
5. Sqlite3
6. Bootstrap

Link to live site
Here is a link to the live site  https://uniquehood.herokuapp.com
## Project Contribution or Development:

To contribute to this project, please follow the following steps:
* Fork this repository.
* Create a branch: `git checkout -b <branch_name>`.
* Make your changes and commit them: `git add .` && `git commit -m '<commit_message>'` && `git push origin <branch_name>`
* Push to the original branch: `git push origin <main>`
* Create the pull request.
* Once a PR is reviewed, the changes will be pushed to the main branch for integration.

Please see the GitHub documentation on [Creating a Pull Request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)
### Contact Me
If you have any suggestions, additions or modifications on this project you can reach me via my email: misigomartin@gmail.com or [mercy.mambui@student.moringaschool.com](mailto:mercy.mambui@student.moringaschool.com)
### License
MIT

Copyright (c) 2022 Mercy Wairimu

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
 https://uniquehood.herokuapp.com

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

