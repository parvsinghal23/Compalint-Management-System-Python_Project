import sqlite3

class ConnectionDatabase:
	def __init__(self):
		self._db = sqlite3.connect('complaintDB.db')
		self._db.row_factory = sqlite3.Row
		self._db.execute("""create table if not exists complainTable(
							ID integer primary key autoincrement, 
							FirstName varchar(255), 
							LastName varchar(255), 
							Room Text, 
							Gender varchar(255), 
							Comment text,
							Status text default "Unsolved" Not Null) 
							""")
		self._db.commit()
		
	def Add(self, firstname, lastname, Room, gender, comment):
		self._db.execute('insert into complainTable (FirstName, LastName, Room, Gender, Comment) values (?,?,?,?,?)', 
		(firstname, lastname, Room, gender, comment))

		self._db.commit()
		return 'Your complaint has been submitted.'
		
	def ListRequest(self):
		cursor = self._db.execute('select * from complainTable')
		return cursor

	def updateStatus(self, Id):

		print(str(Id) + ".")
		self._db.execute('UPDATE complainTable set Status = "Solved" where ID = "' + str(Id) + '"' )
		self._db.commit()

		# cur = self._db.cursor()
		# cur.execute('select * from complainTable')
		# cur.commit()
		# print(cur.fetchall())

		