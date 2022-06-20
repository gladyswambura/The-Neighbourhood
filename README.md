# The-Neighbourhood
This is a web application that allows you to be in the loop about everything happening in your neighborhood. 
From contact information of different handyman to meeting announcements or even alerts.

## AUTHOR 
**Gladys Wambura**

## DESCRIPTION
- This is a web application allows you to be in the loop about everything happening in your neighborhood. From meeting announcements to even alerts.
- 
- ![image](https://user-images.githubusercontent.com/97955649/174562768-809c0251-a092-472c-9770-16215208b90c.png)

## FEATURES && USER STORY 
- As a user of the web application you will be able to:

- Sign up and log in
- 
![image](https://user-images.githubusercontent.com/97955649/174563432-e5086357-539c-4e9a-bc1b-7bb0eabb4830.png)

-View posted businesses and post by other users from your neighbourhood

-Search for a business in the hood

-See authorities and health services around

-JOin && Leave a neighbourhood

![image](https://user-images.githubusercontent.com/97955649/174564413-720201cd-39cf-4b7b-bc93-33aa927db8ad.png)

# **SETUP/INSTALLATION.**

# Prerequisites
-python3.6
-virtual environment
-pip

*** To view the app.Visit -> [THe-Neighbourhood](https://github.com/gladyswambura/The-Neighbourhood)

1. Clone this repo: git clone https://github.com/gladyswambura/The-Neighbourhood
2. The repo comes in a zipped or compressed format. Extract to your prefered location and open it.
3. open your terminal and navigate to gallery then create a virtual environment.For detailed guide refer  [here](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
3. To run the app, you'll have to run the following commands in your terminal
    
    
       pip install -r requirements.txt
4. On your terminal,Create database awwards using the command below.


       CREATE DATABASE awwards; 
       **if you opt to use your own database name, replace awwards your preferred name, then also update settings.py variable DATABASES > NAME

5. Migrate the database using the command below


       python3 manage.py migrate
6. Then serve the app, so that the app will be available on localhost:8000, to do this run the command below


       python manage.py runserver
7. Use the navigation bar/navbar/navigation pane/menu to navigate and explore the app.


# Technologies Used

* Python 3.8
* Django
* Postgresql
* Bootstrap4


## Known Bugs  
* There are no known bugs currently && pull requests are allowed.
  

  ## Contact Information   
If you have any question or contributions, please email me at [gladyswahito7@gmail.com]  


## live link 
https://gladysneighborhood.herokuapp.com/

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
