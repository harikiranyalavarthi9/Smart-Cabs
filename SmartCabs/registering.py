print("""
<!DOCTYPE HTML>
<html>
<head>
<title>SmartCabs | Register</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link href="css/regis.css" type="text/css" rel="stylesheet" media="all"/>
<script>
jQuery(document).ready(function($){  
  //Name Split
  $("#name").change(function(){    
  	var nameVal = $(this).val()
    var nameLength = nameVal.length;
    var nameSplit = nameVal.split(" ");    
    var lastNameLength = nameSplit[0].length + 1;
    var lastName = nameVal.slice(lastNameLength);   
    $(".full-name").fadeOut(0);
    $('#first_name').val(nameSplit[0]);
    $('#last_name').val(lastName);
    $('.name-split').fadeIn(100);
  });  
  
  //Email Split
  $("#full_email").change(function(){    
  	var emailVal = $(this).val();    
    var emailSplit = emailVal.split("@");  
    $(".full-email").fadeOut(0);		
    $('#email').val(emailVal);
    $('#username').val(emailSplit[0]);    
		$('.email-split').fadeIn(100);
  });  

	//Password Split
 $("#full_password").change(function(){    
  	var passwordVal = $(this).val();      
    $(".full-password").fadeOut(0);
    $('#password').val(passwordVal);   
    $('.password-split').fadeIn(100);
		$('#password_confirm').focus();
  });  		
});
</script>
</head>
<body>
<div class="outer">
	<div class="container">
		<div id="infinity"></div>
		<h1>Auto-Split Input Fields</h1>
		<form class="form"> 
			<div class="full-name form-group">
				<label for="name">Name</label>
				<input type="text" id="name" placeholder="Enter your name" class="input" required/>
			</div>
			<div class="row name-split split">
				<div class="col-lg-6 col-md-6 form-group">
					<label for="first_name">First Name</label>
					<input type="text" name="fist_name" id="first_name" placeholder="Enter your first name" class="input" required/>
				</div>
				<div class="col-lg-6 col-md-6 form-group">
					<label for="last_name">Last Name</label>
					<input type="text" name="last_name" id="last_name" placeholder="Enter your last name" class="input" required/>
				</div>
			</div>
			<div class="full-email form-group">
				<label for="full_email">Email</label>
				<input type="email" id="full_email" placeholder="Enter your email" class="input" required/>
			</div>
			<div class="row email-split split">
				<div class="col-lg-6 col-md-6 form-group">
					<label for="email">Email</label>
					<input type="email" name="email" id="email" placeholder="Enter your email" class="input" required/>
				</div>
				<div class="col-lg-6 col-md-6 form-group">
					<label for="username">Username</label>
					<input type="text" name="username" id="username" placeholder="Enter your username" class="input" required/>
				</div>
			</div>
			<div class="full-password form-group">
				<label for="full_password">Password</label>
				<input type="password" id="full_password" placeholder="Enter your password" class="input" required/>
			</div>				
			<div class="row password-split split">
				<div class="col-lg-6 col-md-6 form-group">
					<label for="password">Password</label>
					<input type="password" name="password" id="password" placeholder="Enter your password" class="input" required/>
				</div>
				<div class="col-lg-6 col-md-6 form-group">
					<label for="password_confirm">Confirm Password</label>
					<input type="password" name="password_confirm" id="password_confirm" placeholder="Enter your password again" class="input" required/>
				</div>
			</div>     
			<input type="submit" class="submit" value="Create Account"/>				
		</form>
		<p class="well-lg text-center">
			Use tab to switch fields.  
		</p>
	</div>
</div>
</body>
""")
