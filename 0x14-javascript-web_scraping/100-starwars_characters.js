#!/usr/bin/node

const https = require('https');

const getCharacters = async (movieId) => {
  try {
    const response = await new Promise((resolve, reject) => {
      https.get(`https://swapi.dev/api/films/${movieId}/`, (res) => {
        let data = '';
        res.on('data', (chunk) => {
          data += chunk;
        });
        res.on('end', () => {
          resolve(JSON.parse(data));
        });
      }).on('error', (error) => {
        reject(error);
      });
    });

    const characterUrls = response.characters;
    const characters = await Promise.all(characterUrls.map(async (url) => {
      const charResponse = await new Promise((resolve, reject) => {
        https.get(url, (res) => {
          let data = '';
          res.on('data', (chunk) => {
            data += chunk;
          });
          res.on('end', () => {
            resolve(JSON.parse(data));
          });
        }).on('error', (error) => {
          reject(error);
        });
      });
      return charResponse.name;
    }));

    characters.forEach(character => console.log(character));
  } catch (error) {
    console.error('Error:', error);
  }
};

const movieId = process.argv[2];
getCharacters(movieId);

