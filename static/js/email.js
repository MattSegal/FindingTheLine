var inputEl = document.getElementById('email-input')

inputEl.addEventListener('keypress',function(e) {
	enterPress(e,submitEmail)
}) 

function submitEmail() {
	var inputText = inputEl.value

	if (isValidEmail(inputText)) {
		postEmailRequest(inputText)
			.done(function(data) {
				renderEmailSuccess()
			})
			.fail(function(data) {
				renderEmailFailure()
			})	

	} else if (isEmptyString(inputText)) {
		alert("Please enter your email before submitting")

	} else {
		alert("Please enter a valid email")
	}
}

function postEmailRequest(email) {
	return $.ajax({
	        type: "POST",
	        url: '/email/',
	        data: email,
	        dataType: "text"
   	 	});
	}

function renderEmailSuccess() {
	console.log("sucessfully posted email")
	inputEl.value = ""
	inputEl.placeholder = "Success!"
	inputEl.style.borderColor = "#9f9"
	setTimeout(function() {
		inputEl.placeholder = "Press Enter to submit."
		inputEl.style.borderColor = null
	},5000)
}

function renderEmailFailure() {
	// log to console, make bar red, change input placeholder text
	alert("We failed to save your email (sorry!). Try again later.")
	inputEl.style.borderColor = "#f99"
	setTimeout(function() {
		inputEl.style.borderColor = null
	},5000)
}


function enterPress(event,fn) {
	// check for enter in a keypress event
	if (event.keyCode == 13) {
		fn()
	}
}	

function isEmptyString(str) {
	// returns True if sting is all whitespace
  	return str.replace(/^\s+|\s+$/g, '').length == 0;
}

function isValidEmail(email) {
	var valid_email_regex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	return valid_email_regex.test(email);
}