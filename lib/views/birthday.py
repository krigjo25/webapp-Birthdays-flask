#   Birthday View 

#   Importing required dependencies
import os

#   Importing required dependencies
from dotenv import load_dotenv
from markupsafe import Markup
from flask.views import MethodView
from flask import jsonify, redirect, render_template, request, flash

# CS50 responsories
from cs50 import SQL


#   Load the environment variables
load_dotenv()

class Index(MethodView):

    #   Initializing databases
    methods = ['GET', 'POST']
    DB = SQL(os.getenv('SQLITE_URL'))

    def get(self): return render_template('index.html', entries = self.DB.execute('SELECT * FROM birthdays;'))

    def post(self):

        query = "SELECT * FROM birthdays ORDER BY"
        #   Json Requests
        if request.is_json:
            if self.process(request.get_json()) == True:
                return render_template("index.html", entries=self.DB.execute(f"{query} id;"))


        for i in request.form:
            #   Requested forms
            if str(i) == 'add_record': return self.appendrow()
            elif str(i) == 'update': return self.updaterow()
            elif str(i) == 'del_record': return self.droprow()

            #   Ordering the table
            elif str(i) == 'ORDER_bday': return render_template("index.html", entries=self.DB.execute(f"{query} birthday;"))
            elif str(i) == 'ORDER_name': return render_template("index.html", entries=self.DB.execute(f"{query} name;"))

    def appendrow(self):
        try:
            #   Ensure the user has inputted a name and its alphabetical
            if not request.form['name']: raise Exception('Name is missing')

            #   Ensure the user is not already registered
            for i in self.DB.execute('SELECT * FROM birthdays;'):
                if i['name'] == request.form['name'] and request.form['birthday'] == i['birthday']: raise Exception(f'Can not duplicate an exsisting record')


        except Exception as e:
            flash(f'{e}')
            return render_template("index.html", entries=self.DB.execute('SELECT * FROM birthdays ORDER BY id;'))

        # Insert the user's entry into the database
        self.DB.execute(f"INSERT INTO birthdays (name, birthday) VALUES(?, ?);", request.form['name'], request.form['bday'])

        return render_template("index.html", entries=self.DB.execute('SELECT * FROM birthdays ORDER BY id;'))

    def droprow(self):
        try:
            self.DB.execute('DELETE FROM birthdays WHERE id = ?', int(request.form['del_record']))

        except Exception as e:

            #   Send user message
            flash('Row Does not exist !')
            return render_template("index.html", entries=self.DB.execute('SELECT * FROM birthdays ORDER BY id;'))
        return render_template("index.html", entries=self.DB.execute('SELECT * FROM birthdays ORDER BY id;'))
    def updaterow(self):

        flash('The record was just updated')
        return render_template("index.html", entries=self.DB.execute('SELECT * FROM birthdays ORDER BY id;'))

    def process(self, jsonData):
        if jsonData['btn_name'] == 'update':

            try:
                #   Validating the name
                for i in str(jsonData['updated_name']).split(' '):
                    if not i.isalpha(): raise Exception(f'A name consist of alphabetic characters')

                for i in self.DB.execute('SELECT * FROM birthdays;'):
                    if i['name'] == jsonData['updated_name'] and int(i['id']) != int(jsonData['id']): raise Exception(f'{jsonData['updated_name']} Already Exists in the database')
                    elif i['name'] == jsonData['updated_name'] and int(i['id']) == int(jsonData['id']) and i['birthday'] == jsonData['updated_bday']: raise Exception(f' Data was not modified therefore database not updated')

                #   Validating the birthdays
                bday = str(jsonData['updated_bday']).split('-')

                if not str(jsonData['updated_bday']).split('-'): raise Exception ('Birthdays has to be seperated with "-')
                for i in bday:
                    if not i.isdigit(): raise Exception ('Birthdays can only contain numeric values and seperated with "/"')

            except Exception as e: return e

            #   Update values in the database
            self.DB.execute("UPDATE birthdays SET birthday = ? WHERE id = ?;", jsonData['updated_bday'], int(jsonData['id']))
            self.DB.execute("UPDATE birthdays SET name = ? WHERE id = ?;", jsonData['updated_name'], int(jsonData['id']))

            return render_template("index.html", entries=self.DB.execute('SELECT * FROM birthdays ORDER BY id;'))

