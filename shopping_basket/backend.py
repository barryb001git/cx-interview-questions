import sqlite3

def connect():
    conn=sqlite3.connect("items.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS item (id INTEGER PRIMARY KEY, item text, price integer, discount integer, buy integer, get integer)")
    conn.commit()
    conn.close

    conn=sqlite3.connect("baskets.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS basket (id INTEGER PRIMARY KEY,item_id integer)") #For speed of this excercise I've assumed one item/quantity per row, this is storage inefficient
    conn.commit()
    conn.close

def insert_item(item,price,discount, buy,get):
    conn=sqlite3.connect("items.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO item VALUES(NULL,?,?,?,?,?)",(item,price,discount, buy,get)) #Pass in as tuple
    conn.commit()
    conn.close

def view_item():
    conn=sqlite3.connect("items.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM item")
    rows=cur.fetchall() #Tuple
    conn.close        
    return rows

def search_items(item_name): 
    conn=sqlite3.connect("items.db")
    cur=conn.cursor()
    cur.execute('SELECT * FROM item where item=?',[item_name]) #Pass in list literal
    rows=cur.fetchall() #Tuple
    conn.close        
    return rows 

def delete_item(id):
    conn=sqlite3.connect("items.db")
    cur=conn.cursor()
    cur.execute("DELETE from item WHERE id=?",(id,)) #Pass in as "tuple"
    conn.commit()
    conn.close  

def update_item(id,item,price,discount, buy,get):  
    conn=sqlite3.connect("items.db")
    cur=conn.cursor()
    cur.execute("UPDATE item SET item=?,price=?,discount=?,buy=?,get=? WHERE id=?",(item,price,discount, buy,get,id)) #Pass in as tuple
    conn.commit()
    conn.close  

def show_basket():
    conn=sqlite3.connect("baskets.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM basket")
    rows=cur.fetchall() #Tuple
    conn.close        
    return rows

def empty_basket():
    conn=sqlite3.connect("baskets.db")
    cur=conn.cursor()
    cur.execute("DELETE from basket") 
    conn.commit()
    conn.close 

def add_one_to_basket(item_id):  
    conn=sqlite3.connect("baskets.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO basket  VALUES(NULL, ?)",(item_id,)) #Pass in as tuple (again, I'd ideally want user to be able to pass in a quantity)
    conn.commit()
    conn.close                          

#Create the database (if applicable) every time program is run
connect()  

#Check backend code
#insert_item("Eggs",10.99,0.99,3,1)
#print(view_item())  
#print(search_items(item_name="Eggs",))
#print(search_items("Yeti"))
#delete_item(1)
#print(search_items(item_name="Eggs",))
#update_item(id=2,item="Yeti2",price="3",discount="4",buy="1",get="9")
#print(view_item()) 
print(show_basket())
add_one_to_basket(4)
print(show_basket())
empty_basket()
print(show_basket())

