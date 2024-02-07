const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.get(url, function (data) {
  const moviesList = data.results;
  moviesList.forEach(function (movie) {
    $('UL#list_movies').append('<li>' + movie.title + '</li>');
  });
});
