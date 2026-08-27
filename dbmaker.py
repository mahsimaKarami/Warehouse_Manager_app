import sqlite3

conn = sqlite3.connect("warehouse.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("""
CREATE TABLE products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        barcode TEXT UNIQUE,
        name TEXT,
        price REAL,
        stock INTEGER DEFAULT 0,
        min_stock INTEGER DEFAULT 0
        )
               """)

cursor.execute("""
CREATE TABLE transactions(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               receiver TEXT,
               sender TEXT,
               type TEXT,
               date TEXT DEFAULT (date('now')), 
               description TEXT,
               totalprice REAL DEFAULT 0
               )
""")

cursor.execute("""
CREATE TABLE goodsoftransactions(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               transaction_id INTEGER,
               product_id INTEGER,
               number INTEGER,
               totalprice REAL,
               FOREIGN KEY(transaction_id) REFERENCES transactions(id),
               FOREIGN KEY(product_id) REFERENCES products(id)
               )
""")

conn.commit()
conn.close()