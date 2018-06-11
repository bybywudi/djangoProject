import pymysql

pymysql.install_as_MySQLdb()

db = pymysql.connect("localhost","root","by1994313by","djtest1")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("version : %s" % data)

db.close()
