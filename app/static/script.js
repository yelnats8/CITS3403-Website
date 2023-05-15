// probably need to combine with python files for that
var isLoggedIn = false; // idk

// dimensions of window
var width = window.innerWidth;
var height = window.innerHeight;
// other variables
var whitebox = document.getElementsByClassName("whitebox");
var buttons = document.getElementsByClassName("startchatbtn");

// window.addEventListener("resize", reportWindowSize);
window.onresize = function(event) {
    if (width < 700 && height < 1000) {device == "mobile";}
};

function isUserLoggedIn() {
    // if user is logged in...
    for (var i = 0; i < buttons.length; i++) {
        buttons[i].remove("disabled");
    }
    return;
}

// is this working
