#!C:/Python34/python
import cgi,cgitb
cgitb.enable()
print("content-type:text/html\r\n\r\n")

import mysql.connector

conn=mysql.connector.connect(user='root',password='',host='localhost',database='cabs')
mycursor=conn.cursor()
qry=("SELECT * FROM employee")
mycursor.execute(qry)
result=mycursor.fetchall()
code='''
<!DOCTYPE HTML>
<html>
<head>
<title>SmartCabs</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
<link href='http://fonts.googleapis.com/css?family=Open+Sans:400,300,600,700' rel='stylesheet' type='text/css'>
<link href="css/style.css" rel="stylesheet" type="text/css" media="all"/>

<script type="text/javascript" src="js/jquery.js"></script>
<!-- start slider -->
	<link href="css/camera.css" rel="stylesheet" type="text/css" media="all" />
	<script src="js/jquery.min.js"></script>
    <script type='text/javascript' src="js/jquery.mobile.customized.min.js"></script>
    <script type='text/javascript' src="js/jquery.easing.1.3.js"></script> 
    <script type='text/javascript' src="js/camera.min.js"></script>
    <script>
		jQuery(function(){

			jQuery('#camera_wrap_2').camera({
				
				loader: 'bar',
				pagination: false,
				thumbnails: false
			});
		});
	</script>
<!-- end slider -->
</head>
<body>
<!--star wrap-->      
	    <div class="wrap">	
	    	<!--header--> 
	      		<div class="header">
	      				<!--start-logo-->
				        <div class="logo">	
				             <h1>SMART<span>CABS</span></h1>
				          </div>  
				        <!--end-logo-->
	      	 			<!--start-menu-->
					  	<div class="menu">
						    <ul class="nav">
								<li><a href="home.html">Home</a></li>
								<li><a href="services.html">Services</a></li>
								<li><a href="book.html">Book A Cab</a></li>
								<li><a href="fleet.py">Fleet</a></li>
								<li><a href="tarrif.html">Tariff</a></li>
								<li class="active"><a href="employee.py">Employees</a></li>
								<li><a href="index.html">Logout</a></li>
							<div class="clear"> </div>
						    </ul>
							<script type="text/javascript" src="js/responsive-nav.js"></script>
				        </div>	
						<!--end-menu-->
				            <div class="clear"> </div>				
				</div>
				</div>
		  <!--end-header-->
<!-----end wrap----->   
<!------top- heading------>
<div class="top-heading">
	<!--start-wrap-->
	<div class="wrap">
		<h1>Employees</h1>
	</div>
	<!--end wrap-->
</div> 
<!--start blog-->
	<div class="blog-content">
		<div class="wrap">
			<!--blog-grid-->
			<div class="blog-grids">
				<!-- blog-left-->
				<div class="blog-left">
					<!-- start slider -->


						<div class="text-2">
							<div class="icon1 icon4">
								<a href="#"><span> </span></a>
							</div>
							<div class="sinfo">


                           </div>
							 <div class="clear"> </div>

						</div>

					
						
'''
print(code)
print('''					<center>
							<div class="sinfo">

							<div class="sinfo-left">
							NAME<h6></h6>
							</div>
							<div class="sinfo-left">
							Desgination<h6></h6>
							</div>
							<div class="sinfo-left">
							Salary<h6></h6>
							</div>
							<div class="sinfo-left">
							Date of Join<h6></h6>
							</div>
							<div class="sinfo-left">							
							Phone No.<h6></h6>
							</div>	
							<div class="sinfo-left">							
							Email ID<h6></h6>
							</div>							
							</div>
							</br></br>
							</center>
''')

for x in result:
	print('<center><div class="sinfo"><div class="sinfo-left">',x[1],'</div><div class="sinfo-left">',x[3],'</div><div class="sinfo-left">',x[4],'</div><div class="sinfo-left">',x[5],'</div><div class="sinfo-left">',x[11],'</div><div class="sinfo-left">',x[12],'</div></div> </center>','</br>')

conn.commit()
conn.close()

code2='''
							</div>
						<h6> </h6>
						
						<!--end slider-->
					</div>
				<!--end blog-left-->


			<div class="clear"> </div>
				</div>
				
				<!--end blog-right-->

			</div>
			<!--end  blog-grids-->
		</div>
	
		
	
<!--end blog-->
<!--start footer-->
<div class="footer">
	<div class="footer-main wrap">
	<div class="footer-grids">
		<div class="fgrid">
			</div>
		<div class="fgrid">

		</div>
		<div class="fgrid">

	
		</div>
		<div class="clear"> </div>
	</div>
</div>
</div>
<!--End footer-->
<div class="copy-right">
	<div class="wrap">
		<div class="copy-right-left">

		</div>
	</div>
</div>



</body>
</html>'''
print(code2)