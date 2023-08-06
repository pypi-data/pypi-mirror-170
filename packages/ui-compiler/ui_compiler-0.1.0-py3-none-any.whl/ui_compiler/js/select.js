function set_select_options(select_id, options) {
    const select = document.getElementById(select_id);
    options.forEach(value => {
        const option = document.createElement('option');
        option.appendChild(document.createTextNode(value));
        option.setAttribute('value', value);
        select.appendChild(option);
    });
}

function get_select_options(select_id) {
    const select = document.getElementById(select_id);
    const options = [];
    for (let op of select.options) {
        options.push(op.innerText);
    }
    return options
}

function clear_select_options(select_id) {
    /* remove all options from a select element. */
    let select = document.getElementById(select_id);
    while (select.options.length > 0) {
        select.remove(0);
    }
}

