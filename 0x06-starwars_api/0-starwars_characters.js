#!/usr/bin/node
const axios = require('axios');

const API_URL = 'https://swapi.dev/api';

if (process.argv.length > 2) {
  axios.get(`${API_URL}/films/${process.argv[2]}/`)
    .then(response => {
      const charactersURL = response.data.characters;
      const charactersNamePromises = charactersURL.map(url =>
        axios.get(url).then(characterResponse => characterResponse.data.name)
      );

      return Promise.all(charactersNamePromises);
    })
    .then(names => {
      console.log(names.join('\n'));
    })
    .catch(error => {
      console.error(error.message);
    });
} else {
  console.error('Usage: ./script.js <movie_id>');
  process.exit(1);
}
