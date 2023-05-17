var interestsDiv = document.getElementById("interestsInput");

// INTERESTS INPUT
// add placeholder
interestsDiv.addEventListener('focus', function() {
    if (interestsDiv.classList.contains('interestsPlaceholder')) {
        interestsDiv.textContent = '';
        interestsDiv.classList.remove('interestsPlaceholder');
    }
});
// remove placeholder
interestsDiv.addEventListener('blur', function() {
    if (interestsDiv.textContent.trim() === '') {
        interestsDiv.textContent = 'Enter your interests...';
        interestsDiv.classList.add('interestsPlaceholder');
    }
});
// listener when user hits enter
interestsDiv.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        var tagText = interestsDiv.textContent.trim();
        if (tagText !== '') {
            createTag(tagText);
            interestsDiv.textContent = ''; 
        }
    }
});
// create interests tag
// FIXME: tags not appearing inside div
function createTag(text) {
    var interestTag = document.createElement('span');
    interestTag.classList.add('interestTag');
    interestTag.textContent = text;
    interestsDiv.parentNode.insertBefore(interestTag, interestsDiv);
}