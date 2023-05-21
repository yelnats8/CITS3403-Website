// header items
var header = document.getElementsByTagName("header");
var h1 = document.getElementsByTagName("h1");
var headerbtn = document.getElementsByClassName("headerbtn");
var icon = document.getElementById("icon");
// div classes
var whitebox = document.getElementsByClassName("whitebox");
var content = document.getElementsByClassName("content");
// buttons
var startchatbtns = document.getElementsByClassName("startchatbtn");
// text
var p1 = document.getElementById("p1");
var p2 = document.getElementById("p2");

// IF USER IS NOT SIGNED IN
function disableHome() { /* currently not in use */
    p1.innerHTML = "Please sign in or register to begin a chat.";
    p2.innerHTML = "No you have to be signed in to click this button.";
    for (var i = 0; i < startchatbtns.length; i++) {
        startchatbtns[i] = startchatbtns[i].setAttribute("disabled",true);
        startchatbtns[i].classList.add("disabled");
    }
}

// RESPONSIVITY FOR DEVICE TYPE
window.onresize = function(event) {checkDevice();};
checkDevice();
function checkDevice() {
    var width = window.innerWidth;
    var height = window.innerHeight;
    var isMobile = false;
    // determines touch support
    if ('ontouchstart' in window || navigator.maxTouchPoints) {
        isMobile = true;
    }
    if (isMobile) {
        var aspectRatio = width/height;
        console.log("width "+width,"height "+height);
        console.log("aspect ratio: " + aspectRatio);
        if (aspectRatio < 0.6) {
            console.log("you are on mobile");
            resizeForMobile();
        }
        else if (aspectRatio < 1 && aspectRatio > 0.6) {
            console.log("you are on tablet portrait orientation");
            resizeForTablet();
        }
        else {console.log("you are on long touch screen device");}
        return;
    } 
    else if (isMobile == false) {
        console.log("you are on computer");
        return;
    }
}

function resizeForMobile() {
    // make header and header items bigger
    header[0].style.height = "5%";
    h1[0].style.fontSize = "250%";
    icon.style.width = h1[0].offsetHeight + "px";
    icon.style.height = h1[0].offsetHeight + "px";
    for (var i = 0; i < headerbtn.length; i++) {  
        headerbtn[i].style.fontSize = "200%";         
    }
    // make content div fit whole screen
    var windowHeight = window.innerHeight;
    var headerHeight = header[0].offsetHeight;
    var bodyHeight = windowHeight - headerHeight;
    var marginPercent = content[0].offsetHeight;
    // var marginPercent = (bodyHeight - 400) / 2;
    console.log(marginPercent);
    content[0].style.marginTop = marginPercent + "px";
    content[0].style.width = "95%";
    content[0].style.height = "";
}

function resizeForTablet() {
    // make header and header items bigger
    header[0].style.height = "5%";
    h1[0].style.fontSize = "200%";
    icon.style.width = h1[0].offsetHeight + "px";
    icon.style.height = h1[0].offsetHeight + "px";
    for (var i = 0; i < headerbtn.length; i++) {  
        headerbtn[i].style.fontSize = "150%";         
    }
    // make content div fit whole screen
    var windowHeight = window.innerHeight;
    var headerHeight = header[0].offsetHeight;
    var bodyHeight = windowHeight - headerHeight;
    var marginPercent = content[0].offsetHeight;
    // var marginPercent = (bodyHeight - 400) / 2;
    console.log(marginPercent);
    content[0].style.marginTop = marginPercent + "px";
    content[0].style.width = "95%";
    content[0].style.height = "";
}