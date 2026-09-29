import sqlite3 # import sqlite module

# sqlite browser

# create datebase and connect
db = sqlite3.connect("app.db")

# create the table and fields
#db.execute("Create Table if not exists Skills (name text, progress integer, user_id integer)")

# setting up the cursor
cr=db.cursor()

# Create the tables and fields
cr.execute("Create Table if not exists users (user_id integer, name text)")
cr.execute("Create Table if not exists Skills (name text, progress integer, user_id integer)")

# inserting data
cr.execute("insert into users(user_id,name) values(1,'Ahmed')")
# cr.execute("insert into users(user_id,name) values(2,'Shrief')")
# cr.execute("insert into users(user_id,name) values(3,'Samir')")
# cr.execute("insert into users(user_id,name) values(4,'Omar')")
# cr.execute("insert into users(user_id,name) values(5,'mohamed')")

my_list=["Ahmed","Shrief","Samir","Omar","Mohamed","Ibrahim","Mahmoud"]
for key,name in enumerate(my_list):
    cr.execute(f"insert into users(user_id,name) values({key+1},'{name}')")

# Update Data
cr.execute("update users set name='Gamal' where user_id =7")

# Delete Data
cr.execute("delete from users where user_id=6")

# Fetch data
cr.execute("select name from users")
# print(cr.fetchone()) # ('Ahmed',)
# print(cr.fetchone()) # ('Shrief',)
# print(cr.fetchone()) # ('Samir',)
# print(cr.fetchone()) # ('Omar',)
# print(cr.fetchone()) # ('Mohamed',)
# print(cr.fetchone()) # ('Ibrahim',)
# print(cr.fetchone()) # ('Mahmoud',)
# print(cr.fetchone()) # None
#print(cr.fetchall()) # [('Ahmed',), ('Shrief',), ('Samir',), ('Omar',), ('Mohamed',), ('Ibrahim',), ('Mahmoud',)]

cr.execute("select * from users")
print(cr.fetchall()) # [(1, 'Ahmed'), (2, 'Shrief'), (3, 'Samir'), (4, 'Omar'), (5, 'Mohamed'), (6, 'Ibrahim'), (7, 'Mahmoud')]

#print(cr.fetchmany(3)) # [(1, 'Ahmed'), (2, 'Shrief'), (3, 'Samir')]



# save (commit) changes
db.commit()

# close date base
db.close()


