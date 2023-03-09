dateFunction = function () {
  let currentYear = new Date().getFullYear();
  let earliestYear = 1970;
  let yearArr = [];
  while (currentYear >= earliestYear) {
    yearArr.push(currentYear);
    currentYear -= 1;
  }
  return yearArr;
};
console.log(dateFunction());

var subjectObject = {
  Matic: {
    BeAT: dateFunction(),
    "BeAT Street": dateFunction(),
    Genio: dateFunction(),
    Scoopy: dateFunction(),
    "Vario 125": dateFunction(),
    "Vario 160": dateFunction(),
    PCX: dateFunction(),
    "ADV 160": dateFunction(),
    "PCX e:HEV": dateFunction(),
    Forza: dateFunction(),
  },
  Sport: {
    "CB150 Verza": dateFunction(),
    "Sonic 150R": dateFunction(),
    "CB150R Streetfire": dateFunction(),
    CB150X: dateFunction(),
    CRF150L: dateFunction(),
    CBR150R: dateFunction(),
    CBR250RR: dateFunction(),
    "ST125 Dax": dateFunction(),
    Monkey: dateFunction(),
    "CRF250 RALLY": dateFunction(),
  },
  Cub: {
    Revo: dateFunction(),
    "Supra X 125 FI": dateFunction(),
    "GTR 150": dateFunction(),
    "Supercub C125": dateFunction(),
    CT125: dateFunction(),
  },
  "Big Bike": {
    CB500F: dateFunction(),
    CB650R: dateFunction(),
    CBR500R: dateFunction(),
    "CBR1000RR-R": dateFunction(),
    "X-ADV": dateFunction(),
    CB500X: dateFunction(),
    "Honda CRF1100L Africa Twin Adventure Sports": dateFunction(),
    "Gold Wing 1800": dateFunction(),
    "Honda Rebel": dateFunction(),
  },
  "Tidak Memiliki Motor": { "Tidak Memiliki Motor": ["Tidak Memiliki Motor"] },
  "Lain-lain": { "Lain-lain": ["Lain-lain"] },
};

window.onload = function () {
  var subjectSel = document.getElementById("unit-category");
  var topicSel = document.getElementById("unit-variant");
  var chapterSel = document.getElementById("dropdown-year");
  for (var x in subjectObject) {
    subjectSel.options[subjectSel.options.length] = new Option(x, x);
  }
  subjectSel.onchange = function () {
    // if (subjectSel == Object.values(subjectSel[4])) {
    //   document.getElementById("unit-variant").style.display = "none";
    //   document.getElementById("dropdown-year").style.display = "none";
    // }
    // console.log(Object.values(subjectSel[4]));
    //empty Chapters- and Topics- dropdowns
    chapterSel.length = 1;
    topicSel.length = 1;
    //display correct values
    for (var y in subjectObject[this.value]) {
      topicSel.options[topicSel.options.length] = new Option(y, y);
    }
  };
  topicSel.onchange = function () {
    //empty Chapters dropdown
    chapterSel.length = 1;
    //display correct values
    var z = subjectObject[subjectSel.value][this.value];
    for (var i = 0; i < z.length; i++) {
      chapterSel.options[chapterSel.options.length] = new Option(z[i], z[i]);
    }
  };
};

// console.log(subjectObject);
