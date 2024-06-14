$(document).ready(function() {
    $.ajax({
      url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
      type: 'GET',
      success: function(data) {
        const movies = data.results;
        $.each(movies, function(index, movie) {
          $("#list_movies").append("<li>" + movie.title + "</li>");
        });
      },
      error: function(error) {
        console.error('Error fetching data:', error);
      }
});
});