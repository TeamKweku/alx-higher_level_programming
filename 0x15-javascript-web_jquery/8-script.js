$(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    $.each(data.results, function (index, movie) {
      const listItem = $('<li>' + movie.title + '</li>');
      $('#list_movies').append(listItem);
    });
  });
});
