$(document).ready(function() {
    $('#search-input').on('input', function() {
        var query = $(this).val();

    $.ajax({
      url: '/search/',  // URL to the search view
        data: {
        'query': query
        },
        success: function(data) {
            $('#search-results').html(data);
        }
    });
    });
});
