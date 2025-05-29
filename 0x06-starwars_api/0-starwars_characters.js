#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) return console.error(error);

  const film = JSON.parse(body);
  const characters = film.characters;

  const fetchCharacters = characters.map(charUrl => {
    return new Promise((resolve, reject) => {
      request(charUrl, (err, res, data) => {
        if (err) reject(err);
        else resolve(JSON.parse(data).name);
      });
    });
  });

  Promise.all(fetchCharacters)
    .then(names => names.forEach(name => console.log(name)))
    .catch(err => console.error(err));
});
