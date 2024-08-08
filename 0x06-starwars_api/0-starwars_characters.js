#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command line argument
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// Make a request to the Star Wars API to get the movie details
request(`https://swapi-api.com/api/films/${movieId}`, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
    return;
  }

  const movie = JSON.parse(body);

  // Print the character names one by one
  movie.characters.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
