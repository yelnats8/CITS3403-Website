// other variables
var whitebox = document.getElementsByClassName("whitebox");
var startchatbuttons = document.getElementsByClassName("startchatbtn");

// default
var userLoggedIn = false;
// if user is logged on
// if ("disabled" in startchatbuttons.classname == false) {userLoggedIn = true;} 
// ideally add an event listener to when user logs in or out


// dimensions of window
var width = window.innerWidth;
var height = window.innerHeight;
// window.addEventListener("resize", reportWindowSize);
window.onresize = function(event) {
    if (width < 700 && height < 1000) {device == "mobile";}
};

// LOGIN AND REGISTERING
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
var loginForm = document.getElementById("loginForm");
loginForm.addEventListener('submit', function (event) {
    checkLogin();
});
function checkLogin() {
    if (username.value == "" || password.value == "") {
        errortext.innerHTML = "Please enter a username and password.";
        event.preventDefault(); // Prevent form submission
    }
}