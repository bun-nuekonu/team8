import random
from django.shortcuts import render
from .models import Quizzes

#index用
def index(request):


    #問題の表示 (data : HTMLに返すデータ(問題), record : 表示用問題レコード)
    data = {}

    records = Quizzes.objects.all()
    numbers = len(records)

    display_record_id = random.randint(1, numbers)

    for record in records:
        if record.id == display_record_id:
            data["quiz"] = record
            break

    return render(request, "alarm/index.html", data)

def login(request):
    return render(request,)
    
def logout(request):
    return render(request,)
