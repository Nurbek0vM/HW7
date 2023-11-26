import sqlite3

def create_connection(db_name):
    conn = None
    try:
        conn =sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

def insert_product(conn, products):
    sql = '''INSERT INTO products
    (product_title, price, quantity)
    VALUES
    (?, ?, ?)
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def update_product(conn, products):
    sql = '''UPDATE products SET quantity = ?, price = ?
    WHERE id = ?
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def delete_product(conn, id):
    sql = '''DELETE FROM products WHERE id = ?
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def select_all_products(conn):
    sql = '''SELECT * FROM products
        '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows_list = cursor.fetchall()

        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)

def select_all_by_price_by_quantity(conn, price_quantity_limit):
    sql = '''SELECT * FROM products WHERE price < ? and quantity > 5
        '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (price_quantity_limit,))
        rows_list = cursor.fetchall()

        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)

def search_by_word(conn, word):
    sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, ('%' + word + '%',))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

sql_to_create_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    round(price FLOAT(10),2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
'''

connection = create_connection('hw.db')
if connection is not None:
    print('Succesfully connected to DB!')
    # create_table(connection, sql_to_create_products_table)
    # insert_product(connection, ('Milk', 80, 2))
    # insert_product(connection, ('Tea', 60, 23))
    # insert_product(connection, ('butter', 185, 1))
    # insert_product(connection, ('salt', 15, 20))
    # insert_product(connection, ('Bread', 30, 25))
    # insert_product(connection, ('Meat', 500, 15))
    # insert_product(connection, ('fish', 250, 20))
    # insert_product(connection, ('cheeze', 75, 30))
    # insert_product(connection, ('eggs', 13, 60))
    # insert_product(connection, ('dried milk', 120, 9))
    # insert_product(connection, ('kefir', 90, 18))
    # insert_product(connection, ('sour cream', 50, 26))
    # insert_product(connection, ('yogurt', 70, 6))
    # insert_product(connection, ('caramel', 150, 26))
    # insert_product(connection, ('chokolate', 230, 3))
    # update_product(connection, (24, 28, 10))
    # delete_product(connection, 5)
    # select_all_products(connection)
    # select_all_by_price_by_quantity(connection, 100)
    # search_by_word(connection, 'milk')
    connection.close()
