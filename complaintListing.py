from tkinter import *
from tkinter.ttk import *
import sqlite3

from configdb import ConnectionDatabase


class ComplaintListing:
    def __init__(self):
        self.connectionDB = ConnectionDatabase()
        self.connectionDB.row_factory = sqlite3.Row
        self.root = Tk()
        self.root.title('List of Complaints')
        tree = Treeview(self.root)
        tree.pack()
        tree.heading('#0', text='ID')
        tree.configure(column=('#FirstName', '#LastName', '#Room', '#Gender', '#Comment', '#Status'))
        tree.heading('#FirstName', text='First Name')
        tree.heading('#LastName', text='Last Name')
        tree.heading('#Room', text='Room')
        tree.heading('#Gender', text='Gender')
        tree.heading('#Comment', text='Comment')
        tree.heading('#Status', text='Status')
        tree.column('#0', stretch=NO, minwidth=0, width=100)
        tree.column('#1', stretch=NO, minwidth=0, width=100)
        tree.column('#2', stretch=NO, minwidth=0, width=100)
        tree.column('#3', stretch=NO, minwidth=0, width=100)
        tree.column('#4', stretch=NO, minwidth=0, width=100)
        tree.column('#5', stretch=NO, minwidth=0, width=300)
        tree.column('#6', stretch=NO, minwidth=0, width=100)
        cursor = self.connectionDB.ListRequest()
        for row in cursor:
            tree.insert('', 'end', '#{}'.format(row['ID']), text=row['ID'])
            tree.set('#{}'.format(row['ID']), '#FirstName', row['FirstName'])
            tree.set('#{}'.format(row['ID']), '#LastName', row['LastName'])
            tree.set('#{}'.format(row['ID']), '#Room', row['Room'])
            tree.set('#{}'.format(row['ID']), '#Gender', row['Gender'])
            tree.set('#{}'.format(row['ID']), '#Comment', row['Comment'])
            tree.set('#{}'.format(row['ID']), '#Status', row['Status'])

