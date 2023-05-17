// other variables
var whitebox = document.getElementsByClassName("whitebox");
var startchatbuttons = document.getElementsByClassName("startchatbtn");

// default
var userLoggedIn = false;
// if user is logged on
// if ("disabled" in startchatbuttons.classname == false) {userLoggedIn = true;} 
// ideally add an event listener to when user logs in or out

// RESPONSIVITY FOR DEVICE TYPE
// chatgpt gave me this lol
var isMobile = false;
if ('ontouchstart' in window || navigator.maxTouchPoints) {isMobile = true;}
if (isMobile) {
  // Apply mobile-specific styles or modifications
} else {
  // not mobile, keep current css
}

// and this is my pathetic code
var width = window.innerWidth;
var height = window.innerHeight;
// window.addEventListener("resize", reportWindowSize);
window.onresize = function(event) {
    if (width < 700 && height < 1000) {device == "mobile";}
};