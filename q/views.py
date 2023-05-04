from django.shortcuts import render




def index(req):
    return render(req, 'q/index.html')

def takeQuiz(req):
    return render(req, 'q/take-quiz.html')
