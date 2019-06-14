import sqlite3

connection= sqlite3.connect('mydata.db')

cursor= connection.cursor()

create_table="CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)
user= (1, 'jack', 'asdf')
insert_query= "INSERT INTO users VALUES (?, ?, ?)"
select_query= "SELECT * FROM users"
cursor.execute(insert_query, user)

users=[
    (2, 'wolf', 'abc'),
    (3, 'cat', '123')
]

cursor.executemany(insert_query,users)

for row in cursor.execute(select_query):
    print(row)
connection.commit()
connection.close()