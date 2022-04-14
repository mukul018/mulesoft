import sqlite3

# Connect to the database (new/existing)
db = sqlite3.connect('mydb.db')
cursor = db.cursor()

movies = [
    {'title': 'IRON MAN', 'year': 2008, 'director': 'JON FAVREAU', 'actor': 'ROBERT DOWNEY JR', 'actress': 'GWYNETH PALTROW'},
    {'title': 'THOR', 'year': 2011, 'director': 'ALAN TAYLOR', 'actor': 'CHRIS HEMSWORTH', 'actress': 'NATALIE PORTMAN'},
    {'title': 'AVENGERS', 'year': 2012, 'director': 'JOSS WHEDON', 'actor': 'ROBERT DOWNEY JR', 'actress': 'SCARLETT JOHANSSON'},
    {'title': 'SPIDER MAN NO WAY HOME', 'year': 2021, 'director': 'JON WATTS', 'actor': 'TOM HOLLAND', 'actress': 'ZENDAYA'},
    {'title': 'DR STRANGE', 'year': 2016, 'director': 'SCOTT DERRICKSON', 'actor': 'BENEDICT CUMBERBATCH', 'actress': 'TILDA SWINTON'},
    {'title': 'IRON MAN 3', 'year': 2013, 'director': 'SHANE BLACK', 'actor': 'ROBERT DOWNEY JR', 'actress': 'GWYNETH PALTROW'},
    {'title': 'CAPTAIN AMERICA CIVIL WAR', 'year': 2016, 'director': 'JOE RUSSO', 'actor': 'CHRIS EVANS', 'actress': 'ELIZABETH OLSEN'}
]

# Creating table 'Movies'
cursor.execute("CREATE TABLE Movies (title VARCHAR(60), actor VARCHAR(24), actress VARCHAR(24), year INT(4), director VARCHAR(24));")

# Inserting data into the table
for movie in movies:
    cursor.execute(f"INSERT INTO Movies VALUES (\'{movie['title']}\', \'{movie['actor']}\', \'{movie['actress']}\', {movie['year']}, \'{movie['director']}\');")

# Select all movies
print("\nSelect all movies:")
cursor.execute("SELECT * FROM Movies;")
for i in cursor.fetchall():
    print(i)
print("\n")

# Select all movies with the actor 'ROBERT DOWNEY JR'
print("Select all movies with the actor 'ROBERT DOWNEY JR':")
cursor.execute("SELECT title, year, director FROM Movies WHERE actor='ROBERT DOWNEY JR';")
for i in cursor.fetchall():
    print(i)
print("\n")


# Printing the table in a dataframe
# import pandas as pd
# print(pd.read_sql("SELECT * FROM Movies;", db),end="\n\n")
# print(pd.read_sql("SELECT title, year, director FROM Movies WHERE actor='ROBERT DOWNEY JR';", db))