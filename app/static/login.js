// login
var loginForm = document.getElementById("loginForm");
loginForm.addEventListener('submit', function (event) {
    checkLogin();
});
function checkLogin() {
    if (username.value == "" || password.value == "") {
        errortext.innerHTML = "Please enter a username and password.";
        event.preventDefault();
    }
}