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