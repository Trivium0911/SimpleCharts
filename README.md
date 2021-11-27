# SimpleCharts [![View project](https://img.shields.io/badge/view-project-brightgreen)](https://simplechartsgrads.herokuapp.com/)

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/Trivium0911/SimpleCharts?color=brightgreen&style=plastic)
![GitHub last commit](https://img.shields.io/github/last-commit/Trivium0911/SimpleCharts?style=plastic)


### _Technologies:_
[![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen)](https://www.python.org/)
[![django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)](https://docs.djangoproject.com/en/3.2/)
[![last.fm API](https://img.shields.io/badge/last.fm_API-100000?style=for-the-badge&logo=last.fm&logoColor=EA0303&labelColor=121111&color=151515)](https://www.last.fm/api/)
[![heroku](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)](https://devcenter.heroku.com/categories/reference)
[![postgresql](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![pycharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)](https://www.jetbrains.com/ru-ru/pycharm/)
[![bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)

### _About the project:_

__SimpleCharts__ is a service for viewing statistics of listened tracks, top artists, albums and artists on last.fm in a more informative form.

### _The project is a website with the following functions:_

* registration and authorization of users;
* getting information from __last.fm__ user.
* saving __last.fm__ user's information to the database.
* viewing the songs you've listened to.
* viewing top listened tracks per week / month / 3 months / 6 months / year.
* viewing top listened artists per week / month / 3 months / 6 months / year.
* viewing top listened albums per week / month / 3 months / 6 months / year.


### _Installing and running the project:
1. Create an account at __last.fm__ (https://www.last.fm/)
2. Create API and get API tokens from __last.fm API__ (https://www.last.fm/api/account/create?_pjax=%23content)
3. Install packages from requirements.txt file
4. Set the environment variable DEBUG (True - for local launch)
5. Set the environment variables API_KEY and API_SECRET received from __last.fm API__.
6. Add the environment variable DATABASE_URL, indicating the url to the connected database
7. (not necessary) Set the environment variable lastfm_username according to the name of the account owner of the API.
4. Run the following commands from the directory:

    - Apply migrations
        ```
        python manage.py migrate
        ```
    - Create a superuser for access to project administration (the project configuration is set to Russian)
        ```
        python manage.py createsuperuser
        ```
    - Start the local server
        ```
        python manage.py runserver
        ```
---	
