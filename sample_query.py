import sqlite3
import pandas as pd
conn = sqlite3.connect("test_database")

c = conn.cursor()

output = c.execute('''
SELECT products.product_name as PRODUCT, prices.price as CURRENT_PRICE FROM products, prices
WHERE products.product_id = prices.product_id;

''')
cols = [column[0] for column in output.description]

results = pd.DataFrame.from_records(data = output.fetchall(), columns = cols)
print(results)
