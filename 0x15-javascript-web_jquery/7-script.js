const getDiv = $('DIV#character');
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

$.getJSON(url, function (data) {
    const addTag = $('<p></p>').text(data.name);
    getDiv.append(addTag);
});