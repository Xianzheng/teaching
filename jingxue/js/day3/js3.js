var array = ["Math", "Science", "GYM", "JS", "Java"];
var Ul = document.createElement("ul");
document.body.appendChild(Ul);
array.map((item, index) => {
  var li = document.createElement("li");
  li.innerText = item;

  Ul.appendChild(li);
});

var array = ["100", "95", "85", "95", "90"];
var Ul = document.createElement("ul");
document.body.appendChild(Ul);
array.map((item, index) => {
  var li1 = document.createElement("li");
  li1.innerText = item;

  Ul.appendChild(li1);
});

for (var i = 1; i <= 100; i++) {
  console.log(i);
}
