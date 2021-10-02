from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

    #리퀘스트가 들어왔을때 home.html 갖다줘!