from tkinter import *

window = Tk()

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

#Now associate lists with scollbars
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
list2.configure(yscrollcommand=sb1.set)
sb2.configure(command=list2.yview)

b1=Button(window,text="View Catalogue",width=12)
b1.grid(row=3,column=3)

b2=Button(window,text="Add Item",width=12)
b2.grid(row=4,column=3)

b3=Button(window,text="Update Item",width=12)
b3.grid(row=5,column=3)

b4=Button(window,text="Delete Item",width=12)
b4.grid(row=6,column=3)

b5=Button(window,text="Search Item",width=12)
b5.grid(row=7,column=3)

b6=Button(window,text="Add to Basket",width=12)
b6.grid(row=9,column=1)

b7=Button(window,text="Empty Basket",width=12)
b7.grid(row=10,column=1)

window=mainloop()
