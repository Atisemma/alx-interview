#!/usr/bin/node
const util = require('util');
const request = util.promisify(require('request'));
const filmID = process.argv[2];

async function starwarsCharacters (filmID) {
  const endpoint = 'https://swapi-api.hbtn.io/api/films/' + filmID;

  try {
    let response = await request(endpoint);
    response = JSON.parse(response.body);
    const characters = response.characters;

    for (let i = 0; i < characters.length; i++) {
      const urlCharacter = characters[i];
      let character = await request(urlCharacter);
      character = JSON.parse(character.body);
      console.log(character.name);
    }
  } catch (error) {
    console.error(error);
  }
}

starwarsCharacters(filmID);
