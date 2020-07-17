from tkinter import *
import backend

def get_selected_item_row(event):
    global selected_tuple
    index=list1.curselection()[0] #We only want the first number, not the whole tuple
    selected_tuple=list1.get(index) #Fetch row "X" (index) from the list, keep it.
    #print(selected_tuple) (Keep for debugging)
    #return(selected_tuple) (replaced with global variable)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])
    e5.delete(0,END)
    e5.insert(END,selected_tuple[5])

def delete_items_command():
    backend.delete_item(selected_tuple[0]) #Get global variable set by "get_selected_item_row"
    view_items_command()


def view_items_command():
    list1.delete(0,END) #Nuke everything from the list
    for row in backend.view_items():
        list1.insert(END,row) #Add item to the "end" of the listbox

def search_items_command():
    list1.delete(0,END) 
    for row in backend.search_items(item_text.get()): #I could also choose to search by the other values, in which case I'd add them here.
        list1.insert(END,row) 

def add_item_command():
    backend.insert_item(item_text.get(),price_text.get(),discount_text.get(), buy_text.get(),get_text.get())   
    #Now show the item
    list1.delete(0,END)  
    list1.insert(END,(item_text.get(),price_text.get(),discount_text.get(), buy_text.get(),get_text.get()))

def update_item_command():
    #print(selected_tuple) --Debugging
    backend.update_item(selected_tuple[0],item_text.get(),price_text.get(),discount_text.get(), buy_text.get(),get_text.get())  

def show_basket():
    list2.delete(0,END) 
    for row in backend.show_basket()[0]:
        list2.insert(END,row[0] + ' x ' + str(row[1]))

    list2.insert(END,' ')     

    for row2 in backend.show_basket()[1]:
        list2.insert(END,row2)     

def add_item_to_basket_command():
    backend.add_one_to_basket(selected_tuple[0]) 
    show_basket()

def empty_basket_command():
    list2.delete(0,END)
    backend.empty_basket()                     

window = Tk()
window.wm_title("ECS Excercise")

l1=Label(window,text="Item")
l1.grid(row=0,column=0)

l2=Label(window,text="Price")
l2.grid(row=0,column=2)

l3=Label(window,text="Discount")
l3.grid(row=1,column=0)

l4=Label(window,text="Buy")
l4.grid(row=1,column=2)

l5=Label(window,text="get")
l5.grid(row=1,column=4)

item_text=StringVar()
e1=Entry(window,textvariable=item_text)
e1.grid(row=0,column=1)

price_text=StringVar()
e2=Entry(window,textvariable=price_text)
e2.grid(row=0,column=3)

discount_text=StringVar()
e3=Entry(window,textvariable=discount_text)
e3.grid(row=1,column=1)

buy_text=StringVar()
e4=Entry(window,textvariable=buy_text)
e4.grid(row=1,column=3)

get_text=StringVar()
e5=Entry(window,textvariable=get_text)
e5.grid(row=1,column=5)

list1=Listbox(window,heigh=6, width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list2=Listbox(window,heigh=6, width=35)
list2.grid(row=11,column=0,rowspan=6,columnspan=2)

sb2=Scrollbar(window)
sb2.grid(row=11,column=2,rowspan=6)

#This code associates lists with scollbars
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
list2.configure(yscrollcommand=sb1.set)
sb2.configure(command=list2.yview)

#This enables us to use whatever is selected in the listbox
list1.bind('<<ListboxSelect>>',get_selected_item_row)

b1=Button(window,text="View Catalogue",width=12,command=view_items_command)
b1.grid(row=3,column=3)

b2=Button(window,text="Add Item",width=12,command=add_item_command)
b2.grid(row=4,column=3)

b3=Button(window,text="Update Item",width=12,command=update_item_command)
b3.grid(row=5,column=3)

b4=Button(window,text="Delete Item",width=12,command=delete_items_command)
b4.grid(row=6,column=3)

b5=Button(window,text="Search Item",width=12,command=search_items_command)
b5.grid(row=7,column=3)

b6=Button(window,text="Add to Basket",width=12, command=add_item_to_basket_command)
b6.grid(row=9,column=1)

b7=Button(window,text="Empty Basket",width=12, command=empty_basket_command)
b7.grid(row=10,column=1)

#Show contents of basket
show_basket() 

window=mainloop()
