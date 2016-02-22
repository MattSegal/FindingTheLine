var inputEl = document.getElementById('email-input')

inputEl.addEventListener('keypress',function(e) {
	enterPress(e,submitEmail)
}) 

function submitEmail() {
	var inputText = inputEl.value

	if (isValidEmail(inputText)) {
		postEmailRequest(inputText)
			.done(function(data) {
					console.log("sucessfully posted email")
					renderEmailSuccess()
			})
				.fail(function(data) {
					alert("failed to post email")
					renderEmailFailure()
			})	

	} else if (isEmpty(inputText)) {
		alert("Please enter your email before submitting")

	} else {
		alert("Please enter a valid email")
	}
}

function postEmailRequest(email) {
	return $.ajax({
	        type: "POST",
	        url: '/email/',
	        data: {email: email},
	        dataType: "json",
   	 	});
	}

function renderEmailSuccess() {
	// log to console, make bar green, change input placeholder text
}

function renderEmailFailure() {
	// log to console, make bar red, change input placeholder text
}


function enterPress(event,fn) {
	// check for enter in a keypress event
	if (event.keyCode == 13) {
		fn()
	}
}	

function isEmpty(str) {
	// returns True if sting is all whitespace
  	return str.replace(/^\s+|\s+$/g, '').length == 0;
}

function isValidEmail(email) {
	var valid_email_regex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	return valid_email_regex.test(email);
}



function removeAllWhitespace(str) {
	// replaces all whitespace with ''
	// \s is whitespace
	// + is one or more repetitions
	// /.../ is regex
	// g modifier specifies global match - remove ALL whitespace, not first occurrence of whitespace
	return str.replace(/\s+/g, '')
}
