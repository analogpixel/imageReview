$(document).ready(function() {

    $('.delTag').click(function() {
      console.log('del tag', $(this).data('filename'));
      //var tag = $(this).data('tag');
      var tag = prompt("Please enter a tag", "");
      $.post('/del_tag/' + $(this).data('filename'), {tag: tag});
      
      // update tag list
      $('div.tags[data-filename="' + $(this).data('filename')  + '"] span.tag:contains("' + tag + '")').remove();
    });

    $('.addTag').click(function() {
      console.log('add tag', $(this).data('filename'));
      var tag = prompt("Please enter a tag", "");
      if (tag != null) {
        $.post('/add_tag/' + $(this).data('filename'), {tag: tag});
        
        // update tag list
        $('div.tags[data-filename="' + $(this).data('filename')  + '"]').append('<span class="tag">' + tag + '</span>');
      }
    });

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
