import sqlite3 as sql

conn = sql.connect("test_database")

c = conn.cursor()

c.execute('''

CREATE TABLE IF NOT EXISTS products(
[product_id] INTEGER PRIMARY KEY, [product_name] TEXT)


''')

c.execute('''

CREATE TABLE IF NOT EXISTS prices(
[product_id] INTEGER PRIMARY KEY, [price] TEXT
)


''')

conn.commit()