// Team javabean -- Pak Ming Lau, Eric Lo
// SoftDev pd1
// K28 -- Bubble Bubble Toil Trouble
// 2021-05-11

var tds = document.getElementsByTagName('td');
var trs = document.getElementsByTagName('tr');
var table = document.getElementsByTagName('table')[0];

var clicky = function(e) {
  alert( this.innerHTML );
  //Q: What will happen when next line is uncommented?
  //only the first even happens (the table gets alerted and nothing else afterward)
  //e.stopPropagation();
};

//if there is a mix of capturing and bubbling, capturing happens first, then bubbling

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky);
}

for (x=0; x < trs.length; x++) {
  trs[x].addEventListener('click', clicky);
}

table.addEventListener('click', clicky, true); //the third argument tells the Event to use capturing

// Q: When user clicks on a cell, in what order will the pop-ups appear?
// table, cell, row