// header items
var header = document.getElementsByTagName("header");
var h1 = document.getElementsByTagName("h1");
var headerbtn = document.getElementsByClassName("headerbtn");
// div classes - arrays
var whitebox = document.getElementsByClassName("whitebox");
var content = document.getElementsByClassName("content");
// buttons
var startchatbuttons = document.getElementsByClassName("startchatbtn");

checkDevice();

// var userLoggedIn = false;
// if (startchatbuttons.classname.includes("disabled")) {userLoggedIn = true;} 
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
        // make header and header items bigger
        header[0].classList.add('headerMobile');
        h1[0].classList.add('h1Mobile');
        for (var i = 0; i < headerbtn.length; i++) {
            // headerbtn[i].setAttribute('data-index', i); // debug
            // console.log('Element at index', i, headerbtn[i]); // debug
            headerbtn[i].classList.add('headerbtnMobile');           
        }
        // make content div fit whole screen
        for (var i = 0; i < content.length; i++) {
            content[i].classList.add('whiteboxMobile');
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