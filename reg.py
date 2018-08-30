#!C:/Python34/python
import cgi,cgitb
cgitb.enable()

print( "Content-type:text/html")
s='''
<html>
<head>
<title>SmartCabs | Register</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link href="css/sty.css" type="text/css" rel="stylesheet" media="all"/>
</head>
<body>
<div class="row">
  <h1>REGISTER FOR SMART<span style="color:#f3af9d;">CABS</span></h1>

<div class="linear-container">
  <div class="linear"></div>
</div>
</div>
<form action="somefine.py" method="POST">
<div class="row">
  <span>
    <input class="basic-slide" name="name1" type="text" placeholder="Your best name" /><label for="name1">Name</label>
  </span>
  <span>
    <input class="gate"   name="email" type="text" placeholder="Your favorite email" /><label for="email">Email</label>
  </span>
  <span>
    <input class="slide-up"  name="phone" type="text" placeholder="You can trust us" /><label for="phone">Phone</label>
  </span>
</div>
<div class="row">
  <span>
    <input class="balloon" name="username" type="text" placeholder="Your short name!" /><label for="username">Username</label>
  </span>
  <span>
    <input class="swing"  name="password" type="password" placeholder="You can trust us" /><label for="password">Password</label>
  </span>
  <span>
    <input class="card-slide"  name="confirm" type="password" placeholder="Go ahead and type the same" /><label for="confirm">Confirm Password</label>
  </span>
</div>
<!--
<div class="row">
<div class="main-button">
    <div class="button-overlay"></div>
   <a href="login.html" style="text-decoration:none"> <span>REGISTER</span></a>
</div>
</div>
-->
<div class="row">
<div class="round">
<input type="submit" id="Flamingo" value="REGISTER"/>
</div>
</div>
</form>
</body>
</html>
'''
print(s)
