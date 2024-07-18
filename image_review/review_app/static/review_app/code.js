$(document).ready(function() {
    $('.star').click(function() {

      $.get('/update_star/' + $(this).data('filename'));

      if ( $(this).text().match('✩')) {
        $(this).html("⭐️");
      } else {
        $(this).html("✩");
      }
      console.log($(this).data('filename'));
    });
});
