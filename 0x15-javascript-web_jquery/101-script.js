$(document).ready(function () {
    const new_item = '<li>Item</li>';
    $('DIV#add_item').click(function() {
        $('UL.my_list').append(new_item);
    });

    $('DIV#remove_item').click(function() {
        $('UL.my_list li:last-child').remove();
    });

    $('DIV#clear_list').click(function() {
        $('UL.my_list').empty();
    });
});
