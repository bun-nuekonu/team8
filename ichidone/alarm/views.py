import random
from pygame import mixer
from django.shortcuts import render
from .models import Quizzes

#index用
def index(request):

    data = {}
    data["quizHide"] = "hidden"

    if request.method == "POST":
        if "quizAppear" in request.POST:
            data["quizHide"] = ""

        # もし、選択肢1が押されたら
        if "choice1" in request.POST:
            quizId = request.POST["quizId"]
            recordCpy = Quizzes.objects.get(id=quizId)
            ans = recordCpy.choice1_answer
            if request.POST["choice1"] == ans:
                data["quizHide"] = "hidden"
            else:
                data["quizHide"] = ""

        # もし、選択肢2が押されたら
        elif "choice2" in request.POST:
            quizId = request.POST["quizId"]
            recordCpy = Quizzes.objects.get(id=quizId)
            ans = recordCpy.choice1_answer
            if request.POST["choice2"] == ans:
                data["quizHide"] = "hidden"
            else:
                data["quizHide"] = ""

        # もし、選択肢3が押されたら
        elif "choice3" in request.POST:
            quizId = request.POST["quizId"]
            recordCpy = Quizzes.objects.get(id=quizId)
            ans = recordCpy.choice1_answer
            if request.POST["choice3"] == ans:
                data["quizHide"] = "hidden"
            else:
                data["quizHide"] = ""

        # もし、選択肢4が押されたら
        elif "choice4" in request.POST:
            quizId = request.POST["quizId"]
            recordCpy = Quizzes.objects.get(id=quizId)
            ans = recordCpy.choice1_answer
            if request.POST["choice4"] == ans:
                data["quizHide"] = "hidden"
            else:
                data["quizHide"] = ""

        else:
            data["quizHide"] = ""


    #問題の表示 (data : HTMLに返すデータ(問題), record : 表示用問題レコード)
    records = Quizzes.objects.all()
    numbers = len(records)

    display_record_id = random.randint(1, numbers)

    for record in records:
        if record.id == display_record_id:
            data["quizId"] = record.id
            data["quizText"] = record.quiz
            choiceList = [record.choice1_answer, record.choice2, record.choice3, record.choice4]
            random.shuffle(choiceList)
            data["quizChoices"] = choiceList
            break

    return render(request, "alarm/index.html", data)
    
def time_register(request):
    if request.method == "POST":
        hour = request.POST["hour"]
        print(hour)
        minute = request.POST["minute"]
        print(minute)

        time = hour + minute
        print(time)

        #DBに数値を挿入する必要あり
        #time = Times.objects.create(user_id="#ユーザーIDを取り出す#", time=time)
        return render(request, "alarm/index.html")
    else:

        return render(request, "alarm/time_register.html")
        #DBからUSERを検索する必要
        #検索したものをHTMLに送る
        #HTMLを編集する
        #button機能ごとの関数を作成する必要ある
        
def time_list(request):
    if request.method == "POST":
        time = db.execute("SELECT time FROM times")[0]["time"]
        return render(request, "alarm/time_list.html")
    else:
        return render(request, "alarm/time_list.html")


      
def login(request):
    if request.method == "POST":

        return render(request, "alarm/index")
    else:
        return render(request, "alarm/signup")

