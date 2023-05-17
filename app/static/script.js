// header items
var header = document.getElementsByTagName("header");
var h1 = document.getElementsByTagName("h1");
// div classes - arrays
var whitebox = document.getElementsByClassName("whitebox");
var content = document.getElementsByClassName("content");
// buttons
var startchatbuttons = document.getElementsByClassName("startchatbtn");

checkDevice();

// default
var userLoggedIn = false;
// if user is logged on
// if ("disabled" in startchatbuttons.classname == false) {userLoggedIn = true;} 
// ideally add an event listener to when user logs in or out

// RESPONSIVITY FOR DEVICE TYPE
function checkDevice() {
    var isMobile = false;
    var device = "";
    // determines touch support
    if ('ontouchstart' in window || navigator.maxTouchPoints) {
        isMobile = true;
    }
    if (isMobile) {
        device = "mobile";
        for (let i = 0; i < content.length; i++) {
            content[i].classList.add('contentMobile');   
            content[i].classList.remove('content');          
        }
    } 
    else {
        device = "computer";
    }
    console.log("you are on " + device);
}

var width = window.innerWidth;
var height = window.innerHeight;
// window.addEventListener("resize", reportWindowSize);
window.onresize = function(event) {
    if (width < 700 && height < 1000) {
        device == "mobile";
    }
};