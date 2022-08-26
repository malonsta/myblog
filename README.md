# Blog API Application
> A simple blog API application.


## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Technology Usage](#technology-usage)
* [Project Status](#project-status)



## General Information
- A simple blog API with an interface that cosumes the data.
- Project Assessment



## Technologies Used
- Python - version 3.10
- Django - version 4.0
- Django Rest Framework - version 3.13.1
- Boostrap - version 4.0
- Crispy-Form - version 1.14.0


## Features
List the ready features here:
- View page of all published articles.
- View a single article in a blog and filter acccording to category.
- Store user contacts.


## Screenshots
![Screenshot (1)](https://user-images.githubusercontent.com/69899719/186845987-4b1549a9-7362-4413-90ec-dff55078416e.png)
![Screenshot (2)](https://user-images.githubusercontent.com/69899719/186846016-1ff16bd8-12e1-46ec-b0c6-52559a47dddb.png)
![Screenshot (3)](https://user-images.githubusercontent.com/69899719/186846061-c74bc7c8-d6dd-49c5-9ca1-27f0c0551b27.png)


## Setup
- pip install Django==4
I used Django becuase of it has a lot of libraries that makes my work a lot easier and i am able to build a minimum viable product very fast. Most importantly is that its scalable. 
- pip install DjangoRestFramework
Enables the building of web APIs using Django. It is flexible and fully-featured toolkit with modular and customizable architecture that makes possible development of both simple, turn-key API endpoints and complicated REST constructs.
- pip install Bootstrap
Bootstrap saves all the time to write all the HTML, CSS, and JavaScript and allows me to focus on the backend. It handles all the frontend without the need of writing frontend code from scratch.
- pip install Crispy-Form
Helps with adjusting form properties without having to re-write them in the template. So i can focus on whether the form works or not rather than be disturbed by how it looks.
Open the project file in your terminal.
Run the following two commands to get the database ready to go.
python manage.py makemigrations

python manage.py migrate

Everything should be ready! All that's left is to run the server via the command python manage.py runserver and the site will be available at http://127.0.0.1:8000/myblog/ .


##Technology Usage
You can write and publish posts for your online visitors and store your users contact details.


## Project Status
Project is: complete


