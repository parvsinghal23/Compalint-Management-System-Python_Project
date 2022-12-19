from pydoc import text
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

from complaintListing import ComplaintListing
from configdb import ConnectionDatabase

#Config
conn = ConnectionDatabase()
root = Tk()
root.geometry('550x350')
root.title('Complaint Management System')
root.configure(bg='black')


labels = ['First Name:', 'Last Name:', 'Room:', 'Gender:', 'Comment:']
for i in range(5):
    Label(root, text=labels[i]).grid(row=i, column=0, padx=10, pady=10)


ButtonList = Button(root, text='View Complain')
ButtonList.grid(row=5, column=0, columnspan=2)

Buttonadmin = Button(root, text='Admin')
Buttonadmin.grid(row=5, column=1, columnspan=2)

ButtonSubmit = Button(root, text='Submit Now')
ButtonSubmit.grid(row=5, column=2, columnspan=2)

# Entries
firstname = Entry(root, width=40, font=('Arial', 14))
firstname.grid(row=0, column=1, columnspan=2)

lastname = Entry(root, width=40, font=('Arial', 14))
lastname.grid(row=1, column=1, columnspan=2)

Room = Entry(root, width=40, font=('Arial', 14))
Room.grid(row=2, column=1, columnspan=2)

GenderGroup = StringVar()
Radiobutton(root, text='Male', value='male', variable=GenderGroup).grid(row=3, column=1)
Radiobutton(root, text='Female', value='female', variable=GenderGroup).grid(row=3, column=2)


comment = Text(root, width=40, height=5, font=('Arial', 14))
comment.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

def SaveData():
    message = conn.Add(firstname.get(), lastname.get(), Room.get(), GenderGroup.get(), comment.get(1.0, 'end'))
    firstname.delete(0,'end')
    lastname.delete(0, 'end')
    Room.delete(0, 'end')
    comment.delete(1.0, 'end')
    showinfo(title='Information summitted', message=message)

def ShowComplainList():

    listrequest = ComplaintListing()

def updatestatus():

    adminPage = Tk()
    adminPage.geometry('550x350')
    adminPage.title('Complaint Management System')
    adminPage.configure(bg='black')

    # Entries
    ID = Entry(adminPage, width=40, font=('Arial', 14))
    ID.grid(row=0, column=1, columnspan=2)

    Label(adminPage, text='ID').grid(row=0, column=0, padx=10, pady=10)
    
    Id = 1
    print(str(Id) + ".")

    Label(adminPage, text='ID').grid(row=0, column=0, padx=10, pady=10)
    
    button = Button(adminPage, text='Submit Now', command= conn.updateStatus(Id))
    button.grid(row=2, column=2, columnspan=3)


ButtonSubmit.config(command=SaveData)
ButtonList.config(command=ShowComplainList)
Buttonadmin.config(command=updatestatus)


root.mainloop()
