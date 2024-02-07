const newItem = '<li>Item</li>';

$('DIV#add_item').click(function () {
  $('ul.my_list').append(newItem);
});
