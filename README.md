# Birthdays
A web application that tracks Birthdays with CRUD development
This project is based on CS50's instructions developed by krigjo25

The assignment were to create a replica of a webpage that uses CRUD.

The application was implemented as an assignment at xCS50
Please respect, and keep the [Academic Honesty Policy](https://cs50.harvard.edu/x/2023/honesty/) in mind.<br>
A demo of the application can be watched at [CS50 HomePage](https://cs50.harvard.edu/x/2024/psets/9/birthdays/)

## Installation
1. Clone the repository:
```sh
#   Using HTTPS
git clone https://github.com/krigjo25/webapp-Birthdays-flask.git

#   Using SSH
ssh git@github.com:krigjo25/webapp-Birthdays-flask.git

#   Using Github CLI
gh repo clone krigjo25/webapp-Birthdays-flask
```

2. Navigate to the project directory
```sh
cd webapp-Birthdays-flask
```

3. Install given requirements
```sh
pip install -r requirements.txt
```

4. Run the file
```sh
flask run --debug ( opens up the development environment)
```

## JavaScript
Through the client, the server can fetch the html content by using ajax to send the content to the server.

-   Using ajax to send responses to the server ✅
-   Submit the form ✅

## Python
Through the server the user can 
- Create a record
- Update a record
- Delete a record
- filter records by Name

as a consequence of using AJAX and not using one of its commands, i had to find a workaround to update the table

##  Database
SQLite was choosen as a database as it's lightweight and the operations does not need a server to handle them.

Through the database it is possible to store the values which is created,<br>
it is also possible to fetch stored values.

## Challanges

- Encountered a challange regarding sending content editable data to the server

I created a function containing ajax to send the information which was required to do the task.

- While looping through the contenteditable content
The challenge was solved by using a for loop to interate through the content and ensuring the values matches with the button value

- Encountered a problem with the form submission with the edit button

Which i tried to solve where the server fetches the clicked button and the data was processed through javascript.
There were another wqay, which was quite easier fetching the whole ajax content, and use it to gain the ability to edit the contenteditable text.

## Credits

### Responsories
[flask - Pallets project](https://github.com/pallets)
[CS50 - CS50 team](https://cs50.harvard.edu/x/2024/)

#   LICENCE
The application is under [The UnLicense](./LICENCE).

#   Notes from the developer
Created with love, for python programming,

Thanks for reading, and have a blessed day,
@krigjo25