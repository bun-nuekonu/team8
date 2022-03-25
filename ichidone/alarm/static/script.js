const alarm = document.getElementById('alarm')
const quizWindow = document.getElementById('window')
const setTime = document.getElementById('alarmTime')

var audio = new Audio('../../static/clock_bell.mp3')

var h, m, s;

var setH, setM;

function getTime() {
  var now = new Date();
  h = ('0' + now.getHours()).slice(-2);
  m = ('0' + now.getMinutes()).slice(-2);
  s = ('0' + now.getSeconds()).slice(-2);
  nowtime = h + ":" + m + ":" + s;
  var timeDisplay = document.getElementById('timeDisplay');
  timeDisplay.style.fontSize = "220px";
  timeDisplay.style.fontFamily = "arial, sans-serif";
  timeDisplay.innerHTML = nowtime;

  if(h == setH && m == setM && s == '00'){
    // $.ajax({
    //   url: "/alarm/timeAjax/",
    //   type: 'POST',
    //   data: {"quizAppear": true},
    //   dataType: "json",
    // });
    // console.log("OK!");
    quizWindow.classList.remove('hidden');
    audio.play();
  }
}

function strClock() {
  setInterval("getTime();", 1000);

  if(!quizWindow.classList.contains('hidden')){
    audio.play();
  }

  timeSettings();

}

function timeSettings() {
  setH = setTime.textContent.substr(0, 2);
  setM = setTime.textContent.substr(2, 4);
}

