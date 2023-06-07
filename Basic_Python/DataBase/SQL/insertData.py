import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("insert into test2.table_1 values(123 , 'sudh' , 'sujeet')")
mycursor.execute("insert into test2.table_1 VALUES(200905092 ,'sujeet', 'sujeet.amberkar@gmail.com')")
