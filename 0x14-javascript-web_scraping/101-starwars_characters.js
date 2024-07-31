#!/usr/bin/node

const request = require('request');

const getCharacters = (movieId, callback) => {
  request(`https://swapi.dev/api/films/${movieId}/`, (error, response, body) => {
    if (error) {
      return callback(error);
    }

    if (response.statusCode !== 200) {
      return callback(new Error(`Error fetching film data: ${response.statusCode}`));
    }

    const filmData = JSON.parse(body);
    const characterUrls = filmData.characters;

    const characters = [];
    let count = 0;

    const fetchCharacter = (index) => {
      if (index >= characterUrls.length) {
        return callback(null, characters);
      }

      request(characterUrls[index], (error, response, body) => {
        if (error) {
          return callback(error);
        }

        if (response.statusCode !== 200) {
          return callback(new Error(`Error fetching character data: ${response.statusCode}`));
        }

        const characterData = JSON.parse(body);
        characters.push(characterData.name);
        count++;

        if (count === characterUrls.length) {
          callback(null, characters);
        } else {
          fetchCharacter(index + 1);
        }
      });
    };

    fetchCharacter(0);
  });
};

const movieId = process.argv[2];

getCharacters(movieId, (error, characters) => {
  if (error) {
    console.error(error);
    return;
  }

  characters.forEach(character => console.log(character));
});

