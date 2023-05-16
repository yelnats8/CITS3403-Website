// create account
var registerForm = document.getElementById("registerForm");
registerForm.addEventListener('submit', function (event) {
    checkRegister();
});
function checkRegister() {
    if (confirm_password.value == "") {
        errortext.innerHTML = "Please confirm your password.";
        event.preventDefault(); // Prevent form submission
    }
    else if (password.value != "" || confirm_password.value != "") {
        if (password.value != confirm_password.value) {
            errortext.innerHTML = "Passwords do not match.";
            event.preventDefault(); // Prevent form submission
        }
    }
    if (username.value == "" || password.value == "") {
        errortext.innerHTML = "Please enter a username and password.";
        event.preventDefault(); // Prevent form submission
    }
    
}