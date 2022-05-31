import sqlite3
con=sqlite3.connect('marks.db')
query='''CREATE TABLE if not exists students(RollNo INT PRIMARY KEY,Name TEXT,Maths TEXT,Python TEXT)'''
con.execute(query)
con.commit()
query='''INSERT  INTO students VALUES(?,?,?,?)'''
cursor=con.cursor()
multiple_rows=[(1,'Lohith','A+','O'),(2,'Vamsi','F','B'),(3,'Charan','A+','A'),(4,'Praveen','A+','A+'),(5,'Teja','B','B+')]
cursor.executemany(query,multiple_rows)
con.commit()
query='''SELECT* FROM students'''
cursor.execute(query)
all_rows=cursor.fetchall()
for row in all_rows:
  print(row)