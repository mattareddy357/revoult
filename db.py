import sqlite3

con = sqlite3.connect('user.db')

con.execute("CREATE TABLE  user (name TEXT,dob DATE)")

print('Table crated successfully')

con.close()