var dateDebutAffichage = new Date('2023-04-07T19:30:00'); // Date à partir de laquelle l'élément sera affiché
var Mashle = document.getElementById('Mashle');

if (new Date() >= dateDebutAffichage) {
  Mashle.style.display = 'block';
}
var dateDebutAffichage = new Date('2023-04-09T19:00:00'); // Date à partir de laquelle l'élément sera affiché
var DemonSlayer = document.getElementById('DemonSlayer');

if (new Date() >= dateDebutAffichage) {
  DemonSlayer.style.display = 'block';
}