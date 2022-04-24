
const fieldClasses = {
    first_name: 'First Name',
    last_name: 'Last Name',
    mobile: 'Mobile Phone',
    email: 'Email'
};

let csrfToken = '';

function getFieldClass(textDivJQuery)
{
    let element = textDivJQuery[0];
    for(const cssClass of element.classList)
    {
        if(fieldClasses.hasOwnProperty(cssClass))
            return cssClass;
    }
    return null;
}

function groundEvent(event)
{
    event.preventDefault();
    event.stopPropagation();
}


function getEventRow(event)
{
    groundEvent(event);
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
    input.attr('name', fieldClass);
    input.addClass('edit');
    input.addClass(fieldClass);
    textDiv.after(input);
    input.val(displayText);
}


function setDisplayFields(row, contact_json)
{
    for(const cssClass in fieldClasses)
    {
        let div = row.find(`div.${cssClass}`).first();
        if(div.length === 0)
            continue;

        let value = contact_json[cssClass];
        if(!value)
            continue;

        div.text(value);
    }
}


function newClicked(event)
{
    let lastRow = getEventRow(event);
    lastRow.before(
        '<tr data-pk="">\n' +
            '<td>\n' +
                '<button class="edit">Edit</button>\n' +
                '<button class="save" style="display: none">Save</button>\n' +
                '<button class="cancel" style="display: none">Cancel</button>\n' +
            '</td>\n' +
            '<td>\n' +
                '<div class="display first_name"></div>\n' +
            '</td>\n' +
            '<td>\n' +
                '<div class="display last_name"></div>\n' +
            '</td>\n' +
            '<td>\n' +
                '<div class="display mobile"></div>\n' +
            '</td>\n' +
            '<td>\n' +
                '<div class="display email"></div>\n' +
            '</td>\n' +
        '</tr>\n'
    );

    let newRow = lastRow.prev();
    newRow.find('button.edit').click(editClicked);
    newRow.find('button.save').click(saveClicked);
    newRow.find('button.cancel').click(cancelClicked);
    editClickedInner(newRow);
}


function editClicked(event)
{
    let tr = getEventRow(event);
    editClickedInner(tr);
}


function editClickedInner(row)
{
    // I seperated this from editClicked so when the new button is clicked
    // the new row is placed into an edit state.

    // hide the text used to display the value
    let display = row.find("div.display");
    display.hide();
    display.each(setInputField);

    toggleRowButtons(row);
}


function saveClicked(event)
{
    let row = getEventRow(event);
    let pk = row.attr('data-pk') || null;

    let data = {
        pk: pk
    };

    for(const cssClass in fieldClasses)
    {
        let description = fieldClasses[cssClass];
        let value = row.find(`input.${cssClass}`).val();
        if(!value)
        {
            alert(`Enter a value for ${description}`);
            return;
        }
        data[cssClass] = value;
    }

    let ajaxSettings = {
        url: null,
        method: null,
        headers: {
            'X-CSRFToken': csrfToken
        },
        contentType: "application/json; charset=utf-8",
        dataType: 'json',
        data: JSON.stringify(data),
        context: row
    };

    if(pk)
    {
        ajaxSettings.url = `/contacts/${pk}/`;
        ajaxSettings.method = 'PUT';
    }
    else
    {
        ajaxSettings.url = '/contacts/';
        ajaxSettings.method = 'POST';
    }

    $.ajax(
        ajaxSettings
    ).done(
        function(data)
        {
            let row = this;
            row.attr('data-pk', data.pk);
            cancelClickedInner(row);
            setDisplayFields(row, data);
        }
    ).fail(
        function(jqXHR, textStatus, errorThrown)
        {
            alert(jqXHR.responseJSON.errors.join(' | '));
        }
    );
}


function cancelClicked(event)
{
    let row = getEventRow(event);
    cancelClickedInner(row);
}

function cancelClickedInner(row)
{
    toggleRowButtons(row);
    row.find('div.display').show();
    row.find('input.edit').hide();

    for(const cssClass in fieldClasses)
    {
        row.find(`input.${cssClass}`).val("");
    }
}


function documentReady()
{
    csrfToken = Cookies.get('csrftoken');

    // Set up event handlers
    $('button.new').click(newClicked);
    $('button.edit').click(editClicked);
    $('button.save').click(saveClicked);
    $('button.cancel').click(cancelClicked);
}


$(document).ready(documentReady);