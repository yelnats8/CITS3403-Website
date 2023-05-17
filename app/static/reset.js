// reset password
var resetForm = document.getElementById("resetForm");
resetForm.addEventListener('submit', function (event) {
    checkReset();
});
function checkReset() {
    if (new_password.value == "") {
        errortext.innerHTML = "Please enter a new password.";
        event.preventDefault(); 
    }
    else if (password.value != "" || new_password.value != "") {
        if (password.value === new_password.value) {
            errortext.innerHTML = "Passwords are the same.";
            event.preventDefault(); 
        }
    }
    if (username.value == "" || password.value == "") {
        errortext.innerHTML = "Please enter a username and password.";
        event.preventDefault();
    }
    
}