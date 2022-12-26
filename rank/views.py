from django.shortcuts import render
from .models import questions
 
def index_template(request):
    myapp_data = {
    'app': 'Django'
    }
    return render(request, 'index.html', myapp_data)

def words(request):
    results = questions.objects.all()
    context = {
    'results': results
    }
    return render(request, 'words.html', context)