import sqlite3

# create connection by connecting to data file, it could be any file extension, as long as u know
connection = sqlite3.connect("data.db")

# now get cursor() object from connection
cursor = connection.cursor() #cursor object will be used to execute SQL statement

#let's create a table
create_table = "CREATE TABLE users (id int, username text, password text)"

# now used cursor object to execute create_table statement
cursor.execute(create_table)

# now, let's create insert query
insert_query = "INSERT INTO users VALUES (?, ?, ?)"

# insert 1 user by execute method
user = (1, 'pankaj', 'asdf')
cursor.execute(insert_query, user)

# insert many user in a users list by using executemany
users = [
    (2, 'victoria', 'asdf'),
    (3, 'menow', 'asdf'),
    (4, 'bubbu', 'asdf')
]
cursor.executemany(insert_query, users)


# now, let's crearte select query
select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print (row)

# commit the connection
connection.commit()

# close the connection
connection.close()
