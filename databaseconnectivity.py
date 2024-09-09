import pymysql

conn=pymysql.connect(host="localhost",db="facebook",user="root")
print("Database connected")
mycursor=conn.cursor()

#que="create table techsrijan(name varchar(40),age int (3))"
#que="insert into techsrijan(name,age)values('abc',22)"
#que="update techsrijan set name='xyz' where name='abc'"
que="select * from techsrijan"
mycursor.execute(que)
result = mycursor.fetchall()
print(result)
conn.commit() # to save the value in database
#print("table created successfully")
print("data inserted/updated successfully")
mycursor.close()