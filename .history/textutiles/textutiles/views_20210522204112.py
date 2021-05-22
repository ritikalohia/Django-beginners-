#created
from django.http import HttpResponse 
from django.shortcuts import render

def index(request):
    #params = {'name' : 'Ritika', 'place' : 'Mars'}
    return render(request, 'index.html')
    #return HttpResponse("Home")

def contact(request):
    return render(request, 'contact')
    

def analyze(request):
    #get the text in head
    djtext = request.GET.get('text', 'default' )

    #check checkbox values 
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    spaceremover = request.GET.get('spaceremover', 'off'),
    charcount = request.GET.get('charcount', 'off')


    if removepunc == "on":
        #analyzed = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_'''

        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params ={'purpose':'removed punctuations', 'analyzed_text': analyzed}
        #analyze the text
        return render(request, 'analyze.html', params)

    elif(fullcaps == "on"):
        analyzed =""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params ={'purpose':'changed to UPPERCASE', 'analyzed_text': analyzed}
        #analyze the text
        return render(request, 'analyze.html', params)    

    elif(newlineremover== "on"):
        analyzed =""
        for char in djtext:
            if char != '\n':
                analyzed = analyzed + char
        params ={'purpose':'Removed new lines', 'analyzed_text': analyzed}
        #analyze the text
        return render(request, 'analyze.html', params)   

    elif(spaceremover== "on"):
        analyzed =""
        for index, char in enumerate(djtext):
            if not djtext[index] == " " and djtext[index+1]==" ":
                analyzed = analyzed + char
        params ={'purpose':'extra space removed', 'analyzed_text': analyzed}
        #analyze the text
        return render(request, 'analyze.html', params)   

    elif(charcount== "on"):
        a=0
        for char in djtext:
            a = a + 1
        params ={'purpose':'extra space removed', 'analyzed_text': a}
        #analyze the text
        return render(request, 'analyze.html', params)            

    else:
        return HttpResponse("Error")


  

# def capfirst(request):
#     return HttpResponse("capitalize first")    