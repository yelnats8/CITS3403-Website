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
function loadVarLogRegReset() { // set variables
    var requiredfields = document.getElementsByClassName("inputFields");
    var username = document.getElementById("username");
    var password = document.getElementById("password");
    var confirmpassword = document.getElementById("confirmpassword");
    var errortext = document.getElementById("errortext");
}

var form = document.getElementById("registerForm"); // Reference the form element

form.addEventListener('submit', function (event) {
    checkRegister();
    loadVarLogRegReset();
});

function checkRegister() {
    loadVarLogRegReset();
    if (username.value == "" || password.value == "") {
        errortext.innerHTML = "Please enter a username and password.";
        event.preventDefault(); // Prevent form submission
    }
    // TODO: if confirm password is empty, form still submits
    else if (password.value != "" && confirmpassword.value != "") {
        if (password.value != confirmpassword.value) {
            errortext.innerHTML = "Passwords do not match.";
            event.preventDefault(); // Prevent form submission
        }
    }
}