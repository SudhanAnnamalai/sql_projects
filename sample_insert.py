import sqlite3

conn = sqlite3.connect("test_database")

c = conn.cursor()

c.execute('''
INSERT INTO products(product_id, product_name)
VALUES
(1, 'computer'),
(2, 'Blender'),
(3, 'Chair'),
(4, 'TV(80 inches)'),
(5, 'TV(50 inches)'),
(6, 'TV(90 inches)'),
(7, 'TV(120 inches)')
''')

c.execute('''
INSERT INTO prices(product_id, price)
VALUES
(1, 500),
(2, 500),
(3, 600),
(4, 800),
(5, 200),
(6, 1200),
(7, 1500)
''')

conn.commit()