import MySQLdb
db=MySQLdb.connect("localhost","root","","the_alter")
insertrec=db.cursor()
sqlquery="insert into login(UserName,Password,Email) values ('Shashoda','shashoda','shashoda@gmail.com')"
insertrec.execute(sqlquery)
db.commit()
print("Record Saved Successfully..!")
db.close()