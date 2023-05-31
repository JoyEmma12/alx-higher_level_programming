#!/usr/bin/node

const request = require("request");

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const movie = JSON.parse(body).results;
  const wedge = movie.filter((movie) =>
    movie.characters.includes("https://swapi-api.alx-tools.com/api/people/14/")
  );
  console.log(wedge.length);
});
