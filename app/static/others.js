var searchbtn = document.getElementsByClassName("submitsearchbtn")[0];
var searchInput = document.getElementById("searchInput");
var searchForm = document.getElementById("searchForm");

searchForm.addEventListener('submit', function (event) {
    checkSearch();
});
function checkSearch() {
    if (searchInput.value.trim() == "") {
        event.preventDefault();
    }
}