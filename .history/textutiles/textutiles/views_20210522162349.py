#created
from django.http import HttpResponse 
from django.shortcuts import render

def index(request):
    #params = {'name' : 'Ritika', 'place' : 'Mars'}
    return render(request, 'index.html')
    #return HttpResponse("Home")

# def removepunc(request):
def analyze(request):
    #get the text in head
    djtext = request.GET.get('text', 'default' )
    removepunc = request.GET.get('removepunc', 'off')
    print(removepunc)
    print(djtext)
    analyzed = djtext
    params ={'purpose':'removed punctuations', 'analyzed_text': analyzed}
    #analyze the text
    return render(request, 'analyze.html', params)
    #return HttpResponse("remove punc <a href='/'>back</a>")   

# def capfirst(request):
#     return HttpResponse("capitalize first")    