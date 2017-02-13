#!C:/Python34/python
import cgi,cgitb
cgitb.enable()
print("content-type:text/html\r\n\r\n")

import mysql.connector

conn=mysql.connector.connect(user='root',password='',host='localhost',database='cabs')
mycursor=conn.cursor()

form=cgi.FieldStorage()

name1=form.getvalue('name1')
address=form.getvalue('address')
phone=form.getvalue('phone')
email=form.getvalue('email')
vehicle=form.getvalue('vehicle')
pickup=form.getvalue('pickup')
drop=form.getvalue('drop')
pickd=form.getvalue('pickd')
pickt=form.getvalue('pickt')



mycursor.execute('insert into customerbooking(customername,address,phoneno,email,vehicletype,pickup,droppoint,fromdate,todate) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(name1,address,phone,email,vehicle,pickup,drop,pickd,pickt))
conn.commit()
conn.close()
cd='''
<html>
<head>
<title>
Invoice | Smartcabs
</title>
<link href="css/form.css" rel="stylesheet" type="text/css" media="all"/>

</head>
<body>
<form>
    <center><h1>INVOICE</h1></center></br>

'''
print(cd)
print("<h2>Hi!! ",name1,",</h2></br>")
print("<h2> You have booked a seat in ",vehicle,"<h2></br>")
print("<h2> Our cab will be picking you at ",pickup," on the date ",pickd," by the time ",pickt," </h2></br>")
print("<h2> Our cab will drop you at ",drop," </h2>")
print("<h2>Thank you :)</h2></br>")
print("<h2>Regards SMARTCABS!!</h2>")

print('''
<div class="container">
 
  
  <a href="http://localhost/web/home.html" class="btn btn--style2" style="text-decoration:none">Send To Your Mail!</a>
  

</div>
''')
print("</form></body></html>")

import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login('smartcabs.pro@gmail.com','smart6474')
msg='''
Hi %s,
You have booked a seat in %s
Our cab will be picking you at %s on the date %s by the time %s
Our cab will drop you at %s
Thank you :)
Regards SMARTCABS!!
''' % (name1,vehicle,pickup,pickd,pickt,drop)
server.sendmail('smartcabs.pro@gmail.com',email,msg)
server.close()
