// Uses the jQuery API to add a red class to the header tag and turn it
// red when the DIV#red_header tag is clicked

$('DIV#red_header').click(function () {
    $('header').addClass('red');
  });

