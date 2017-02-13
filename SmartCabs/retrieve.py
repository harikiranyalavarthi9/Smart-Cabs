#!C:/Python34/python
import cgi,cgitb
cgitb.enable()

import mysql.connector
con=mysql.connector.connect(user='root', password ='',host='localhost', database='cabs')
cur=con.cursor()
form=cgi.FieldStorage()
veh=form.getvalue('vehicletype')
regno=form.getvalue('regno')
fuel=form.getvalue('fueltype')
seats=form.getvalue('seats')
ac=form.getvalue('ac')
def redirect(url):
    print("Content-Type: text/plain")
    print("Refresh: 0; url=%s" % url)
    print()
    print("Redirecting...")

sel=("insert into fleet(vehicletype,regno,fueltype,seats,ac) values(%s,%s,%s,%s,%s)")
cur.execute(sel,(veh,regno,fuel,seats,ac))
con.commit()
con.close()
redirect('fleet.py')
