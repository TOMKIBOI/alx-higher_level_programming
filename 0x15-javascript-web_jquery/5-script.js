// Adds an LI element to the list when the DIV#add_item tag is clicked
// The new element must be <li>Item</li> & should be included in <li>Item</li>

$('DIV#add_item').click(function () {
    let element = '<li>Item</li>';
    $('ul.my_list').append(element);
  });
