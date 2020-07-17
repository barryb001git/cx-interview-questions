import sqlite3
import math

def connect():
    conn=sqlite3.connect("shopping.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS item (id INTEGER PRIMARY KEY, item text, price integer, discount integer, buy integer, get integer)")
    conn.commit()
    conn.close

    conn=sqlite3.connect("shopping.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS basket (id INTEGER PRIMARY KEY,item_id integer)") #For speed of this excercise I've assumed one item/quantity per row, this is storage inefficient
    conn.commit()
    conn.close

def insert_item(item,price,discount, buy,get):
    conn=sqlite3.connect("shopping.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO item VALUES(NULL,?,?,?,?,?)",(item,price,discount, buy,get)) #Pass in as tuple
    conn.commit()
    conn.close

def view_items():
    conn=sqlite3.connect("shopping.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM item")
    rows=cur.fetchall() #Tuple
    conn.close        
    return rows

def search_items(item_name): 
    conn=sqlite3.connect("shopping.db")
    cur=conn.cursor()
    cur.execute('SELECT * FROM item where item=?',[item_name]) #Pass in list literal
    rows=cur.fetchall() #Tuple
    conn.close        
    return rows 

def search_item_by_id(item_id): 
    conn=sqlite3.connect("shopping.db")
    cur=conn.cursor()
    cur.execute('SELECT * FROM item where id=?',[item_id]) #Pass in list literal
    rows=cur.fetchall() #Tuple
    conn.close        
    return rows     

def delete_item(id):
    conn=sqlite3.connect("shopping.db")
    cur=conn.cursor()
    cur.execute("DELETE from item WHERE id=?",(id,)) #Pass in as "tuple"
    conn.commit()
    conn.close  

def update_item(id,item,price,discount, buy,get):  
    conn=sqlite3.connect("shopping.db")
    cur=conn.cursor()
    cur.execute("UPDATE item SET item=?,price=?,discount=?,buy=?,get=? WHERE id=?",(item,price,discount, buy,get,id)) #Pass in as tuple
    conn.commit()
    conn.close

def buy_to_acquire(desired, buy=1, free=0, price=0):
    #print('desired: ',desired)
    #print('price: ',price)
    pack = buy + free
    buy_packs = desired // pack
    #print('buy_packs: ',buy_packs)
    buy_individual = desired % pack
    #print('buy_individual: ',buy_individual)
    buy_to_aquire_result = buy * buy_packs + buy_individual
    #print('buy_to_aquire_result: ',buy_to_aquire_result)
    buy_to_acquire_discount = desired*price - (buy_to_aquire_result * price)
    #print('buy_to_acquire_discount: ',buy_to_acquire_discount)
    return buy_to_acquire_discount

def show_basket():
    subtotal = 0
    discount = 0
    total = 0
    
    conn=sqlite3.connect("shopping.db")
    cur=conn.cursor()
    cur.execute("SELECT item, total_in_basket, total_in_basket*price total_before_discount, total_in_basket * discount_applied item_discount, buy, get, price from (SELECT item, count(*) total_in_basket, price,discount,buy,get, (price*ifnull(discount,0))/100 discount_applied from (SELECT item, price,discount,buy,get FROM item INNER JOIN basket ON item.id = basket.item_id) group by item, price,discount,buy,get)")
    rows=cur.fetchall() #Tuple
    #This is the basket logic
    print(rows)
    for row in rows:
            print("Item: ", row[0])
            print("total_in_basket: ", row[1])
            print("total_before_discount: ", row[2])
            subtotal += row[2] 
            print("percent_discount: ", row[3])
            discount += row[3]
            print("Buy: ", row[4])
            print("Free: ", row[5])
            print("Price: ", row[6])
            if row[4] != "": #If we have a buy to acquire discount
                buy_to_acquire_discount = buy_to_acquire(int(row[1]),buy=int(row[4]),free=int(row[5]),price=row[6])
                print("buy_to_acquire_discount: ",buy_to_acquire_discount)
                discount += buy_to_acquire_discount
            print("\n")
    conn.close 

    #print('subtotal: ',round(subtotal,2)) #No...rounds down 0.945
    total = math.ceil(subtotal*100)/100 - math.ceil(discount*100)/100
    subtotal = math.ceil(subtotal*100)/100
    discount = math.ceil(discount*100)/100
    print('subtotal: ',subtotal) 
    print('discount: ',discount) 
    print('total: ',total)  

    totals = ('subtotal: ' + str(subtotal), 'discount: ' + str(discount), 'total: ' + str(total))

    return rows, totals

def empty_basket():
    conn=sqlite3.connect("shopping.db")
    cur=conn.cursor()
    cur.execute("DELETE from basket") 
    conn.commit()
    conn.close 

def add_one_to_basket(item_id):  
    conn=sqlite3.connect("shopping.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO basket  VALUES(NULL, ?)",(item_id,)) #Pass in as tuple (again, I'd ideally want user to be able to pass in a quantity)
    conn.commit()
    conn.close                          

#Create the database (if applicable) every time program is run
connect()  

#Check backend code
#insert_item("Eggs",10.99,0.99,3,1)
#print(view_items())  
#print(search_items(item_name="Eggs",))
#print(search_items("Yeti"))
#delete_item(1)
#print(search_items(item_name="Eggs",))
#update_item(id=2,item="Yeti2",price="3",discount="4",buy="1",get="9")
#print(view_items()) 
#print(show_basket())
#add_one_to_basket(4)
#print(show_basket())
#empty_basket()
#print(show_basket())

