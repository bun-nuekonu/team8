import random
from django.shortcuts import render
from .models import Quizzes

#index用
def index(request):

    data = {}
    data["quizHide"] = "hidden"

    if request.method == "POST":
        if "quizAppear" in request.POST:
            data["quizHide"] = ""

        if "choice" in request.POST:
            quizId = request.POST["quizId"]
            recordCpy = Quizzes.objects.get(id=quizId)
            ans = recordCpy.choice1_answer
            if request.POST["choice1"] == ans:
                data["quizHide"] = "hidden"
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
