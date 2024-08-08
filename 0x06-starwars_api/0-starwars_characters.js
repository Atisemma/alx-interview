#!/usr/bin/node

const request = require('request');

// Get the Movie ID from the command line argument
const movieId = process.argv[2];

// Make a request to the Star Wars API to get the movie data
request(`https://swapi.dev/api/films/${movieId}/`, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the movie data
  const movieData = JSON.parse(body);

  // Get the list of character IDs from the movie data
  const characterIds = movieData.characters.map(url => url.split('/').slice(-2, -1)[0]);

  // Make requests to the Star Wars API to get the character names
  characterIds.forEach(id => {
    request(`https://swapi.dev/api/people/${id}/`, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      // Print the character name
      console.log(JSON.parse(body).name);
    });
  });
});
