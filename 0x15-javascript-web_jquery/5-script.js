const new_item = '<li>Item</li>';

$('DIV#add_item').click(function () {
    $('ul.my_list').append(new_item);
});
