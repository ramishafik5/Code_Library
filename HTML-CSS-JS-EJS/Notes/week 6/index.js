const dynamicContent = document.getElementById('dynamic-content');
const changeTextButton = document.getElementById('changeTextButton');
const changeStyleButton = document.getElementById('changeStyleButton');
const createElementButton = document.getElementById('createElementButton');
const toggleVisibilityButton = document.getElementById('toggleVisibilityButton');

// Basic DOM Manipulation - Change Text
changeTextButton.addEventListener('click',function() {
    dynamicContent.textContent = 'The text has been changed using JS'
    alert('Text content has been updated');
});

// Basic DOM Manipulation - Change Style
changeStyleButton.addEventListener('click',function() {
    dynamicContent.style.color = 'red';
    dynamicContent.style.fontSize = '2em'
    alert('Style has been updated');
});

// Basic DOM Manipulation - Create New Element 
createElementButton.addEventListener('click',function() {
    const newPara = document.createElement('p') // <p></p>
    newPara.textContent = 'This is newly created paragraph element'
    // above line --> <p>This is newly created paragraph element</p>
    newPara.style.color = 'blue';
    document.querySelector('.container').appendChild(newPara)
    // change the visibility of new-element
    newElementDiv.style.display = 'block'
    alert('Element has been created');
});
// toggle visibility
toggleVisibilityButton.addEventListener('click',function() {
    const content = document.getElementById('content')
    if(content.style.display === 'none')
    {
        content.style.display = 'block';
        toggleVisibilityButton.textContent = 'Hide Content'
    }
    else
    {
        content.style.display = 'none';
        toggleVisibilityButton.textContent = 'Show Content'
    }
    alert('Content Visibility toogles');
});


