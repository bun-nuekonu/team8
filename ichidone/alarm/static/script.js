function getTime() {
  var now = new Date();
  var h = ('0' + now.getHours()).slice(-2);
  var m = ('0' + now.getMinutes()).slice(-2);
  var s = ('0' + now.getSeconds()).slice(-2);
  nowtime = h + ":" + m + ":" + s;
  var timeDisplay = document.getElementById('timeDisplay');
  timeDisplay.style.fontSize = "220px";
  timeDisplay.style.fontFamily = "arial, sans-serif";
  timeDisplay.innerHTML = nowtime;
}

function strClock() {
  setInterval("getTime();", 1000);
}