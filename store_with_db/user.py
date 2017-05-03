import sqlite3
from flask_restful import Resource, reqparse

# User class
class User():

    """docstring for User."""

    def __init__(self, _id, _username, _password):
        self.id = _id
        self.username = _username
        self.password = _password

    # create class method of finding username from database
    @classmethod
    def find_by_username(cls, _username):
        # connect with db
        connection = sqlite3.connect('data.db')
        # get cursor object
        cursor = connection.cursor()

        # create query
        query = "SELECT * FROM users WHERE username=?"
        # execute query
        result = cursor.execute(query, (_username,))
        # fetch the first result of query
        row = result.fetchone()
        # now check for null VALUES
        if row:
            user = cls(row[0], row[1], row[2])
            # pythonic way
            # user = cls(*row)
        else:
            user = None

        # commit to db, if any udpate to tables data
        # connection.commit()
        # close db
        connection.close()
        return user

    # create class method of fidning id from database
    @classmethod
    def find_by_id(cls, _id):
        # connect with db
        connection = sqlite3.connect('data.db')
        # get cursor object
        cursor = connection.cursor()

        # create query
        query = "SELECT * FROM users WHERE id=?"
        # execute query
        result = cursor.execute(query, (_id,))
        # fetch the first result of query
        row = result.fetchone()
        # now check for null VALUES
        if row:
            user = cls(row[0], row[1], row[2])
            # pythonic way
            # user = cls(*row)
        else:
            user = None

        # commit to db, if any
        # connection.commit()
        # close db
        connection.close()
        return user

class UserRegister(Resource):

    # create post method which will register user by going to endpoint /register
    def post(self, arg):
        pass
