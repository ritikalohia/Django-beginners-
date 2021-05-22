#created
from django.http import HttpResponse 
from django.shortcuts import render

def index(request):
    #params = {'name' : 'Ritika', 'place' : 'Mars'}
    return render(request, 'index.html')
    #return HttpResponse("Home")

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about_us.html')

def analyze(request):
    #get the text in head
    djtext = request.POST.get('text', 'default' )

    #check checkbox values 
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off'),
    charcount = request.POST.get('charcount', 'off')


    if removepunc == "on":
        #analyzed = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_'''

        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params ={'purpose':'removed punctuations', 'analyzed_text': analyzed}
        #analyze the text
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if(fullcaps == "on"):
        analyzed =""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params ={'purpose':'changed to UPPERCASE', 'analyzed_text': analyzed}
        #analyze the text
        djtext = analyzed
        #return render(request, 'analyze.html', params)    

    if(newlineremover== "on"):
        analyzed =""
        for char in djtext:
            if char != '\n' and char !="\r":
                analyzed = analyzed + char
        params ={'purpose':'Removed new lines', 'analyzed_text': analyzed}
        #analyze the text
        djtext = analyzed
        #return render(request, 'analyze.html', params)   

    if(spaceremover== "on"):
        analyzed =""
        for index, char in enumerate(djtext):
            if not djtext[index] == " " and djtext[index+1]==" ":
                analyzed = analyzed + char
        params ={'purpose':'extra space removed', 'analyzed_text': analyzed}
        #analyze the text
        djtext = analyzed
        #return render(request, 'analyze.html', params)   

    if(charcount== "on"):
        a=0
        for char in djtext:
            a = a + 1
        params ={'purpose':'extra space removed', 'analyzed_text': a}
        #analyze the text
        djtext = analyzed
        #return render(request, 'analyze.html', params)            

    if(removepunc != "on" and newlineremover != "on" and spaceremover !="on" and fullcaps != "on"):
        return HttpResponse("Please select any opera tion!!")


    return render(request, 'analyze.html', params)

# def capfirst(request):
#     return HttpResponse("capitalize first")    