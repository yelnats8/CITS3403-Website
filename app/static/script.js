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
// interests div
var interestsDiv = document.getElementById("interestsDiv");
// text
var h2 = document.getElementsByTagName("h2");
var h3 = document.getElementsByTagName("h3");
var p = document.getElementsByTagName("p");
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
window.addEventListener("resize", checkDevice);
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
    scaleUpContent(2); 
    // make header and header items bigger
    header[0].style.height = "7%";
    h1[0].style.fontSize = "300%";
    // h1[0].innerHTML += "&nbsp;";
    icon.style.width = h1[0].offsetHeight + "px";
    icon.style.height = h1[0].offsetHeight + "px";
    for (var i = 0; i < headerbtn.length; i++) {  
        headerbtn[i].style.fontSize = "260%";  
        // headerbtn[i].innerHTML += "&nbsp;";       
    }
    // make content div bigger
    var windowHeight = window.innerHeight;
    var headerHeight = header[0].offsetHeight;
    var bodyHeight = windowHeight - headerHeight;
    var marginPercent = (content[0].offsetHeight / bodyHeight) * 100;
    console.log(marginPercent);
    content[0].style.marginTop = marginPercent + 20 + "%";
    content[0].style.width = "90%";
    // make buttons bigger
    for (var i = 0; i < startchatbtns.length; i++) {
        startchatbtns[i].style.width = "160%";
    }
    // make interests div bigger
    interestsDiv.style.width = startchatbtns[0].offsetWidth + "px";
}

function resizeForTablet() {
    scaleUpContent(1.6);
    // make header and header items bigger
    header[0].style.height = "7%";
    h1[0].style.fontSize = "200%";
    icon.style.width = h1[0].offsetHeight + "px";
    icon.style.height = h1[0].offsetHeight + "px";
    for (var i = 0; i < headerbtn.length; i++) {  
        headerbtn[i].style.fontSize = "170%";         
    }
    // make content div bigger
    var windowHeight = window.innerHeight;
    var headerHeight = header[0].offsetHeight;
    var bodyHeight = windowHeight - headerHeight;
    var marginPercent = (content[0].offsetHeight / bodyHeight) * 100;
    console.log(marginPercent);
    content[0].style.marginTop = marginPercent + "%";
    content[0].style.width = "90%";
    // make buttons bigger
    for (var i = 0; i < startchatbtns.length; i++) {
        startchatbtns[i].style.width = "140%";
    }
    // make interests div bigger
    interestsDiv.style.width = startchatbtns[0].offsetWidth + "px";
}

// from chat gpt pasted
/*
window.addEventListener("resize", handleResize);
handleResize();
function handleResize() {
    if (window.matchMedia("(max-width: 768px)").matches) {
        // Mobile devices
        scaleUpContent(1.2); // Scale up by 20%
    } else if (window.matchMedia("(max-width: 1024px)").matches) {
        // Tablet devices
        scaleUpContent(1.5); // Scale up by 50%
    } else {
        // Desktop devices
        scaleUpContent(1); // Reset to original size
    }
}
*/

function scaleUpContent(scaleFactor) {
    var allContent = document.querySelector('.content');
    allContent.style.zoom = scaleFactor;
}