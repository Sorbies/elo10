// Team javabean -- Pak Ming Lau, Eric Lo
// SoftDev pd1
// K28 -- Bubble Bubble Toil Trouble
// 2021-05-11

var tds = document.getElementsByTagName('td');

var clicky = function(e) {
  alert( this.innerHTML ); //gives a dialog box
};

// Since there are multiple elements, each one is assigned an EventListener
for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky);
}
