# HobbyBuddy
HobbyBuddy is a Web Application designed to help people search new hobbies during the pandemic.

## Theme
Our team chose “Mental Health” as our theme because this category is incredibly broad, yet helpful for the community. We had the liberty to choose everything from prevention to the countermeasures to help with a person’s mental health, which means more room for us to explore our options in how to help the community in regards to their mental health.

## Project Background
Our team think that this topic is very relevant to our current situation because since the start of the Covid-19 pandemic, we noticed that awareness for mental health has been incredibly emphasised because of the sudden drastic change on everyone’s daily routine which increased stress levels and cases of depression.

According to a paper about the Analysis of Time-Varying Associations between Hobbies and Depression1, there is a 30% lower odds of having depression when a person takes up a new hobby.

Unfortunately, the process of finding, researching, and fully taking up a new hobby takes a long time and is quite confusing. Our team found that it is often hard to find the starting point of a certain hobby when you are just starting out.

Therefore, with the facts stated above in mind, we wanted to create a safe way for people to reduce their stress levels and hopefully tackle cases of depression in the midst of the pandemic and also after. Introducing HobbyBuddy. HobbyBuddy is created to help people find new activities and hobbies that fit their personal preferences, whether its outdoor or indoor activities, creative or sporty activities, we provide a platform for those who want to easily research for new activities or hobbies to do


## Dependencies and Requirements
- Python
- Django
- Pillow
- Django

## Run on Windows   
### Run Method 1
1. Open command prompt in the directory
2. venv\Scripts\activate (this will run the virtual environment venv)
3. python manage.py runserver
4. Open Browser 127.0.0.1:8000

### Run Method 2
1. Open command prompt in the directory
2. pip install virtualenv
3. virtualenv hobbybuddyenv (this will create a new virtual environment hobbybuddyenv)
4. hobbybuddyenv\Scripts\activate (this will run the virtual environment hobbybuddyenv)
5. python -m pip install --upgrade pip
6. pip install django
7. pip install pillow
8. python3 manage.py runserver
9. Open Browser 127.0.0.1:8000

## Run on Mac (Python and Pip Required)
1. Open terminal in the directory
2. pip install virtualenv
3. virtualenv hobbybuddyenv (this will create a new virtual environment hobbybuddyenv)
4. source hobbybuddyenv\bin\activate (this will run the virtual environment hobbybuddyenv)
5. python -m pip install --upgrade pip
6. pip install django
7. pip install pillow
8. python manage.py runserver
9. Open Browser 127.0.0.1:8000

## Django Admin to Acces Database
- Access through 127.0.0.1:8000/admin
- Username: admin
- Password: admin

## Create New Activity and Category
1. Login as Admin
2. Go to 127.0.0.1:8000/restricted/create-activity (create new activity) or 127.0.0.1:8000/create-category (create new category)

# The FEMTECH TEAM
1. Michael Shane
2. Eduardus Bagaskara
3. Felicia Winna