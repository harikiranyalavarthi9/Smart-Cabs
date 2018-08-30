#!C:/Python34/python

import cgi,cgitb

cgitb.enable()

import mysql.connector

conn=mysql.connector.connect(user='root',password='',host='localhost',database='cabs')

form=cgi.FieldStorage()

mycursor=conn.cursor()

username=form.getvalue('username')
password=form.getvalue('password')

def redirect(url):
    print("Content-Type: text/plain")
    print("Refresh: 0; url=%s" % url)
    print()
    print("Redirecting...")

sel=("select username,password from register where username=%s and password=%s")
mycursor.execute(sel,(username,password))
res1=mycursor.fetchall()
if(len(res1)==1):
    redirect('book.html')
else:
    redirect('login.html')
