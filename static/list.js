
function setInputField(index, textDiv)
{
    console.log('setInputField');
    textDiv = $(textDiv);

    let input = textDiv.siblings('input');

    console.log('foo');
}


function newClicked(event)
{
    console.log('newClicked');
}


function editClicked(event)
{
    console.log('editClicked');
    let tr = $(event.target).parents('tr');

    // hide the text used to display the value
    let display = tr.find("div.display");
    display.hide();
    display.each(setInputField);
}


function saveClicked(event)
{
    console.log('saveClicked');
}


function cancelClicked(event)
{
    console.log('cancelClicked');
}


function documentReady()
{
    // Set up event handlers
    $('button.new').click(newClicked);
    $('button.edit').click(editClicked);
    $('button.save').click(saveClicked);
    $('button.cancel').click(cancelClicked);
}


$(document).ready(documentReady);