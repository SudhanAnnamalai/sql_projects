import mysql.connector
import pandas as pd
#import sqlite3

conn = mysql.connector.connect(
    host = "localhost",
    user = "sudhanmagic",
    password = "findercorser"
)
# conn = sqlite3.connect("Science.db")

# c = conn.cursor()
print(conn)

# query = c.executescript('''
# BEGIN;

# PRAGMA total_count = (SELECT COUNT(*) FROM iris);

# SELECT total_count - COUNT(*) FROM iris WHERE sepal_length > 6;

# END;
# ''')
# cols = [i[0] for i in query.description]

# print(pd.DataFrame.from_records(data=query.fetchall(), columns = cols))