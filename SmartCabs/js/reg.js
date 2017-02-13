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