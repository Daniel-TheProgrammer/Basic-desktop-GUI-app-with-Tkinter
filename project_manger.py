from tkinter import*

#-----------Create Window object---------
app=Tk()

#-------Part----------
part_text= StringVar()
part_label= Label(app,text='Part Name',font=('bold',14),pady=20)
part_label.grid(row=0,column=0,sticky=W)
part_entry=Entry(app, textvariable=part_text)
part_entry.grid(row=0,column=1)

#-------Customer----------
customer_text= StringVar()
customer_label= Label(app,text='Customer',font=('bold',14))
customer_label.grid(row=0,column=2,sticky=W)
customer_entry=Entry(app, textvariable=customer_text)
customer_entry.grid(row=0,column=3)

#-------Retailer----------
retailer_text= StringVar()
retailer_label= Label(app,text='Retailer',font=('bold',14))
retailer_label.grid(row=1,column=0,sticky=W)
retailer_entry=Entry(app, textvariable=retailer_text)
retailer_entry.grid(row=1,column=1)

#-------Price----------
price_text= StringVar()
price_label= Label(app,text='Price',font=('bold',14))
price_label.grid(row=1,column=2,sticky=W)
price_entry=Entry(app, textvariable=price_text)
price_entry.grid(row=1,column=3)

#--------Parts list(Listbox)-------
parts_text=StringVar()
parts_label=Label(app,text='Parts',font=('bold',14))
parts_list=Listbox(app,height=8,width=50,border=0)
parts_list.grid(row=3,column=0,columnspan=3, rowspan=6, pady=20, padx=20)

#---------------Create Scrollbar-----------
scrollbar=Scrollbar(app)
scrollbar.grid(row=3,column=3)

#------------Set scroll to listbox------------
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_lists.yview)

#Buttons
add_btn=Button(app,text='Add Part',width=12,command=add_item)
add_btn.grid(row=2,column=0,pady=20)

remove_btn=Button(app,text='Remove Part',width=12,command=remove_item)
remove_btn.grid(row=2,column=1)

update_btn=Button(app,text='update Part',width=12,command=update_item)
update_btn.grid(row=2,column=2)

clear_btn=Button(app,text='Clear Input',width=12,command=clear_text)
clear_btn.grid(row=2,column=3)

app.title('Part manager')
app.geometry('700x350')


#------Start Program-------
app.mainloop()
