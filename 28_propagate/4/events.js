// Team javabean -- Pak Ming Lau, Eric Lo
// SoftDev pd1
// K28 -- Bubble Bubble Toil Trouble
// 2021-05-11

// Name the collections of TDs, TRs, and overall table
var tds = document.getElementsByTagName('td');
var trs = document.getElementsByTagName('tr');
var table = document.getElementsByTagName('table')[0];


var clicky = function(e) {
  alert( this.innerHTML );
  //Q: What will happen when next line is uncommented?
  //only the first even happens (the table gets alerted and nothing else afterward)
  //e.stopPropagation();
};


//Q: Does the order in which the event listeners are attached matter?
//no, the order does not matter in which the even listeners are attached

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky, true);
}

for (x=0; x < trs.length; x++) {
  trs[x].addEventListener('click', clicky, true);
}

table.addEventListener('click', clicky, true);

