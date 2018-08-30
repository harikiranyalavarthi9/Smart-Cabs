#!C:/Python34/python

import cgi,cgitb
cgitb.enable()

print("Content-type:text/html")
print("<html>")
print("<body>")

import mysql.connector

conn=mysql.connector.connect(user='root',password='',host='localhost',database='cabs')

mycursor=conn.cursor()

'''form=cgi.FieldStorage()

name=form.getvalue('name1')
email=form.getvalue('email')
phone=form.getvalue('phone')
username=form.getvalue('username')
password=form.getvalue('password')
confirm=form.getvalue('confirm')
'''
def redirect(url):
    print ("Content-Type: text/plain")
    print( "Refresh: 0; url=%s" % url)
    print()
    print ("Redirecting...")

if(password==confirm):
    mycursor.execute("INSERT INTO register VALUES("name","email","phone","username","password")"
    conn.commit()
    conn.close()
    redirect('login.html')
    
else:
    print("password not matched..")
    print("Re-enter the password")
    redirect('reg.py')
print("</body>")
print("</html>")
