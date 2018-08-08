import sqlite3

def create_table():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()

def delete(item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=(?)",(item,))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

choice=input("Press 1 to enter data \n Press 2 to delete data \n Press 3 to view data \n")
if choice == "1":
    item=input("Enter the name of ITEM ")
    quantity=int(input("Enter Quantity "))
    price=float(input("Enter Price "))
    insert(item,quantity,price) # or insert("Wine Glass",2,30.5)

elif choice == "2":
    item=input("Enter the name of ITEM to delete ")
    delete(item) # or insert("Wine Glass")

elif choice == "3":
    print(view())