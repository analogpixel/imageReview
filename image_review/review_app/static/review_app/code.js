$(document).ready(function() {

    $('.noteField').on('change keyup paste', function() {
      //console.log('input got', this.dataset.filename, this.value);
      $.post('/update_note/' + this.dataset.filename, {note: this.value});
    });

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
