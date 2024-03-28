from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def analyze(request):
    #get the text
    djtext=request.GET.get('text','default')
    #chekbox value
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charactercount = request.GET.get('charactercount', 'off')


    if removepunc == "on":#punctuations
         punctuations='''!@#$%^&*()_+~<>?:"{}|/-'''
         analyzed=""
         for char in djtext:
            if char not in punctuations:
                analyzed=analyzed + char
                params={'purpose':'remove punctuations','analyzed_text':analyzed}
         return render(request,'analyze.html',params)
    elif(fullcaps=="on"):#fullcaps
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
            params={'purpose':'change to uppercase','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)
    elif(charactercount=="on"):
        analyzed=""
        for char in djtext:
            analyzed=len(djtext)
        params = {'purpose': 'counted characters', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

            
    else:
        return HttpResponse("Error")
        
    