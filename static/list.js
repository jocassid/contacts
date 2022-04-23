
const fieldClasses = [
    'first_name',
    'last_name',
    'mobile_phone',
    'email'
];

function getFieldClass(textDivJQuery)
{
    let element = textDivJQuery[0];
    for(const cssClass of element.classList)
    {
        if(fieldClasses.includes(cssClass))
            return cssClass;
    }
    return null;
}


function getEventRow(event)
{
    return $(event.target).parents('tr');
}


function toggleRowButtons(row)
{
    let firstCell = row.find('td').first();
    if(!firstCell)
    {
        console.error("Unable to find 1st cell");
        return null;
    }

    firstCell.find('button.edit').toggle();
    firstCell.find('button.save').toggle();
    firstCell.find('button.cancel').toggle();
}


function setInputField(index, textDiv)
{
    textDiv = $(textDiv);
    let displayText = textDiv.text();

    let input = textDiv.siblings('input').first();
    if(input.length === 1)
    {
        input.show();
        input.val(displayText);
        return;
    }

    let fieldClass = getFieldClass(textDiv);
    if(!fieldClass)
    {
        console.error("no field class found");
        return;
    }

    input = $(document.createElement('input'));
    input.attr('name', 'fieldClass');
    input.addClass('edit');
    input.addClass(fieldClass);
    textDiv.after(input);
    input.val(displayText);
}


function newClicked(event)
{
    console.log('newClicked');
}


function editClicked(event)
{
    let tr = getEventRow(event);

    // hide the text used to display the value
    let display = tr.find("div.display");
    display.hide();
    display.each(setInputField);

    toggleRowButtons(tr);
}


function saveClicked(event)
{
    console.log('saveClicked');
}


function cancelClicked(event)
{
    let tr = getEventRow(event);
    toggleRowButtons(tr);
    tr.find('div.display').show();
    tr.find('input.edit').hide();
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