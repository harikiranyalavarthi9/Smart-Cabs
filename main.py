#!C:/Python34/python

import cgi,cgitb
cgitb.enable()
print("Content-type:text/html\r\n\r\n")

st='''
<html>
<body>
<h1>Welcome</h1>
</body>
</html>
'''
print(st)
