from django.shortcuts import render
from .models import questions
from.models import user_result_his
from .forms import QuestionForm
import random
from django.http import HttpResponse
 
def index_template(request):
    return render(request, 'index.html')

def words(request):
    questionNum = 1
    score = 0
    #問題、解答取得
    resultList = questions.objects.all()
    #Form取得
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        questionNum = form.cleaned_data["questionNum"]
        score = form.cleaned_data["score"]
        
    #結果ボタン押された場合
    if request.method == 'POST':
        if "result" in request.POST:
            #DBに結果登録
            regist_result(request)
            context = {
                'score':score,
            }
            return render(request, 'ans.html', context)

    #正解番号設定
    correctNum = random.randint(0,len(resultList)-1)
    #リスト設定
    questionList = [questionNum, resultList[correctNum].question]
    #選択肢ランダム設定
    choices = [
        [resultList[correctNum].answer, 1],
        [resultList[random.randint(0,len(resultList)-1)].answer, 0],
        [resultList[random.randint(0,len(resultList)-1)].answer, 0],
        [resultList[random.randint(0,len(resultList)-1)].answer, 0]
    ]
    addedNumList = []
    while True:
        choiceNum = random.randint(0, 3)
        if choiceNum in addedNumList:
            continue
        else:
            questionList.append(choices[choiceNum][0])
            questionList.append(choices[choiceNum][1])
            addedNumList.append(choiceNum)
        if len(addedNumList) == 4:
            break
    questionList.append(score)
    print(questionList)
    #返却値設定
    context = {
    'questionList': questionList,
    'form':form,
    }
    return render(request, 'words.html', context)

#DB結果登録
def regist_result(request):
    #連番
    
    p = user_result_his.objects.create(first_name="Bruce", last_name="Springsteen")
    
    
