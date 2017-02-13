#!C:/Python34/python
import cgi,cgitb
cgitb.enable()

import mysql.connector

conn=mysql.connector.connect(user='root',password='',host='localhost',database='cabs')

#print("Content-type:text/html")

form=cgi.FieldStorage()

mycursor=conn.cursor()

name1=form.getvalue('name1')
email=form.getvalue('email')
phone=form.getvalue('phone')
username=form.getvalue('username')
password=form.getvalue('password')
confirm=form.getvalue('confirm')


def redirect(url):
    print("Content-Type: text/plain")
    print("Refresh: 0; url=%s" % url)
    print()
    print("Redirecting...")

    



if(password==confirm):
    mycursor.execute('insert into register(name,email,phone,username,password) values(%s,%s,%s,%s,%s)',(name1,email,phone,username,password))
    conn.commit()
    conn.close()
    redirect('login.html')
else:
    redirect('reg.py')



