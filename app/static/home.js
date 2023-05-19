var interestsTagsDiv = document.getElementById("interestsTagsDiv");
var interestsDiv = document.getElementById("interestsDiv");
var interestsInput = document.getElementById("interestsInput");

// INTERESTS INPUT
const tagsArray = [];
interestsDiv.addEventListener('click', function() {
    interestsInput.focus();
});
// dynamically adjust input size
interestsInput.addEventListener('input', function() {
    interestsInput.value = interestsInput.value.toLowerCase();
    this.style.width = ((this.value.length + 1) * 8) + 'px';
    // this.style.width = this.value.length + "ch";
    if (interestsInput.value == "") {
        this.style.width = "initial";
    }
});
interestsInput.addEventListener('keydown', function() {
    if (event.keyCode === 13) {
        event.preventDefault();
        createTag(this.value);
    }
    if (event.keyCode == 8) {
        this.style.width = this.value.length + "ch";
    }
    if (interestsInput.value == "") {
        this.style.width = "initial";
    }
});
// create interests tag
function createTag(input) {
    interestsInput.value = "";
    input = input.trim();
    var tagId = input.replace(/\s+/g,"_").replace(/[^\w-]/g,""); // remove bad characters
    tagId = tagId.toLowerCase();
    tagId = "tag." + tagId;
    if (!tagsArray.includes(tagId) && input != "") {
        var interestTag = document.createElement('span');
        interestTag.textContent = input;
        interestTag.classList.add('interestTag');
        interestTag.id = tagId;
        tagsArray.push(interestTag.id);
        interestTag.setAttribute("onclick", "removeTag('" + interestTag.id + "')");
        interestsInput.style.width = interestsInput.value.length + "ch";
        interestsInput.placeholder = "";
        interestsTagsDiv.appendChild(interestTag);
    }
}
// remove interests tag
function removeTag(tag) {
    var toDelete = document.getElementById(tag);
    toDelete.remove();
    var i = tagsArray.indexOf(tag);
    tagsArray.splice(i, 1);
    if (tagsArray.length === 0) {
        interestsInput.style.width = "initial";
        interestsInput.placeholder = "Enter your interests..."
    }
}