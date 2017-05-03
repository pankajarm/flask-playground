import sqlite3

# create connection by connecting to data file, it could be any file extension, as long as u know
connection = sqlite3.connect("data.db")

# now get cursor() object from connection
cursor = connection.cursor() #cursor object will be used to execute SQL statement

#let's create a table
create_table = "CREATE TABLE users (id INTEGER PRIMARY KEY, username text, password text)"

# now used cursor object to execute create_table statement
cursor.execute(create_table)

# commit the connection
connection.commit()

# close the connection
connection.close()
