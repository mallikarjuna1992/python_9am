import pymysql 

conn = pymysql.connect(user='root',password='',host='localhost',database='python_10am')

#print(conn)
cur=conn.cursor()

#cur.execute('create database python_10am')

#cur.execute('create table std_details(std_name varchar(20),std_email varchar(25),std_course varchar(15),std_fee int(5),std_mobile varchar(10))')
print(cur.execute('show tables'))
print(cur.fetchone())
conn.close()