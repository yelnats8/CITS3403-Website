var interestsTagsDiv = document.getElementById("interestsTagsDiv");
var interestsDiv = document.getElementById("interestsDiv");
var interestsInput = document.getElementById("interestsInput");

// INTERESTS INPUT
const tagsArray = [];
interestsDiv.addEventListener('click', function() {
    interestsInput.focus();
});
// create interests tag
function createTag(input) {
    interestsInput.value = "";
    input = input.trim();
    var tagId = input.replace(/\s+/g,"_").replace(/[^\w-]/g,""); // remove bad characters
    tagId = "tag." + tagId;
    if (!tagsArray.includes(tagId) && input != "") {
        var interestTag = document.createElement('span');
        interestTag.textContent = input;
        interestTag.classList.add('interestTag');
        interestTag.id = tagId;
        tagsArray.push(interestTag.id);
        interestTag.setAttribute("onclick", "removeTag('" + interestTag.id + "')");
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
        interestsInput.placeholder = "Enter your interests..."
    }
}