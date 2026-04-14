# Django

- Webframe 

### How a website works 
- website needs 
    - Frontend  -> HTML and css
    - backend   -> Logic (python, Django framework)
    - Database  -> Stores data


# Some good concepts to know

- i want to create a CLI application using python -  what will you do .
- CLI application - calculator
- __name__ == '__main__'



## virtual environment

Virtual environment is a isolated environment which help to manage the packages specific to project requirements and help to overcomes the version confilts while working with multiple projects.

to Create virtual environment use the below command :

> python -m venv <virtual-environment-name>

`python -m venv django-virtual-environment`


To Activate Virtual environment

> <Virtual-environment-name/Scripts/activate>


`\django-virtual-environment\Scripts\activate`


after activating you will get the virtual environment name before the folder path

## Steps to create Django Webapplication

### Step1 : Create virtual environment

- Its a good practice to create virtual environemnt whenever we are creating a django project

### Step2 : Install required packages

- `pip install django`
 
### Step3 : Create a django project

- `django-admin startproject <projectname>`

> django-admin startproject project1


### Step4 : Create a app

- go to project folder using `cd <project-name>`
> python manage.py startapp <appname>

### step5 : register apps in the settings.py file

- go to settings.py file in the project folder and find the installed apps list and add  app names as the list items.

### step6 : Run the Django app 

> python manage.py runserver


## Create our firts webpage

### Step1 : 
