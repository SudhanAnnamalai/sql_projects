import sqlite3
import csv
import pandas as pd

conn = sqlite3.connect("Science.db")

cur = conn.cursor()

file = open("iris.csv")

content = csv.reader(file)
next(content)

cur.execute('''
CREATE TABLE IF NOT EXISTS iris(
sepal_length REAL NOT NULL,
sepal_width REAL NOT NULL,
petal_length REAL NOT NULL,
petal_width REAL NOT NULL,
species INTEGER NOT NULL)

''')


records = "INSERT INTO iris(sepal_length, sepal_width, petal_length, petal_width,species) VALUES (?,?,?,?,?)"

cur.executemany(records,content)

query = cur.execute('''
SELECT * FROM iris
''')

cols = [column[0] for column in query.description]

print(pd.DataFrame.from_records(data = query.fetchall(), columns=cols))

conn.commit()

