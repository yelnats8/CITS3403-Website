var interestsTagsDiv = document.getElementById("interestsTagsDiv");
var interestsDiv = document.getElementById("interestsDiv");
var interestsInput = document.getElementById("interestsInput");

// INTERESTS INPUT
// add placeholder
/*
interestsInput.addEventListener('focus', function() {
    if (interestsInput.classList.contains('interestsPlaceholder')) {
        interestsInput.textContent = '';
        interestsInput.classList.remove('interestsPlaceholder');
    }
});
// remove placeholder
interestsInput.addEventListener('blur', function() {
    if (interestsInput.textContent.trim() === '') {
        interestsInput.textContent = 'Enter your interests...';
        interestsInput.classList.add('interestsPlaceholder');
    }
});
// listener when user hits enter
interestsInput.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        var input = interestsInput.textContent.trim();
        if (input !== '') {
            interestsInput.textContent = ''; 
            createTag(input); 
        }
    }
});
*/
// create interests tag
function createTag(input) {
    interestsInput.value = "";
    var interestTag = document.createElement('span');
    interestTag.textContent = input;
    interestTag.classList.add('interestTag');
    interestsTagsDiv.appendChild(interestTag);
}