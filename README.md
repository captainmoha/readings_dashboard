# Readings Dashboard Demo Flask App
A demo Python dashboard webapp that utilizes Pandas. With full documentation on how to run it and a deployed version of the code.
### Contents
- [Code Structure](#code-structure)
- [Perspective](#perspective)
- [Dependancies](#dependancies)
- [Installation](#installation)
- [Deployed App](#deployed-app)


#### Code Structure
###### Code is divided into two main sections
1. **load_csv_to_db.py** a script to load _**.csv**_ into a SQLite database.
2. **flaskapp** directory. A **Flask** web application that serves data from database and logs each data access in the same database.

#### Perspective
- In **load_csv_to_db.py**, I loaded the data from **_task_data.csv_** into a database.
- I used **Pandas** (Great at handling data) and **SQLalchemy** (ORM) to read the data from csv and create a database & table for it then load data into the db.
- Afterwards, I created a **Flask** web app to serve the data from database in a neat(thanks **Bootstrap**) **HTML** format.
- With each **GET** request a Log entry is created with a timestamp of when the data was accessed.
- For convenience, I show the number of times the data was accessed as well as the last time it was accessed in the navigation bar.

- Further, I added a section that shows some useful statistics (Thanks **Pandas**) about relevant fields in the database i.e. (Temperature, and Duration).


#### Dependancies
0. Python 3.6.* or higher is installed. Install instructions [here](https://www.python.org/downloads/).
1. Make sure virtualenv is installed, if not check [here](https://virtualenv.pypa.io/en/latest/installation/).
2. Make sure SQLite is installed, if not check [here]( https://linoxide.com/linux-how-to/install-use-sqlite-linux/).


#### Installation
1. Clone repository into an empty directory on your machine. 
`git clone app.git`
2. Create a virtual env in the same parent directory in which you cloned the repo.
`virtualenv -p python3 app_env`
3. Activate virutal env in your terminal.
`source app_env/bin/activate`
4. Go to repo directory.
`cd app`
5. Install requirements
`pip install -r requirements.txt`
6. Run load_csv_to_db.py to load data from **_csv_** into database.
`python load_csv_to_db.py`
7. Run **Flask** web app.
`python run.py`
8. Open browser to check out the running app
go to `localhost:5000`


#### Deployed App
- For convenience, I have also deployed the application on **Heroku** cloud platform to see a quick glance of the application.
- Link: https://readings-dashboard.herokuapp.com/
