# AUTHOR : FAIZAN

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1> <center> Hello </center> </h1>")


def about(request):
    return HttpResponse("<h1> <center> About Me . . . </center> </h1>")


def PersonalNagivator(request):
    return HttpResponse("""
                        <a href= "https://www.youtube.com"> <h1> <center> Youtube </center> </h1> </a>
                        <a href= "https://www.replit.com"> <h1> <center> Replit </center> </h1> </a>
                        <a href= "https://www.github.com"> <h1> <center> Github </center> </h1> </a>
                        <a href= "https://www.web.whatsapp.com"> <h1> <center> Whatsapp </center> </h1> </a>
                        <a href= "https://www.wikipedia.com"> <h1> <center> Wikipedia </center> </h1> </a>
                        """)


def home(request):
    return HttpResponse("<h1> <center> Home </center> </h1> <br> <a href = 'analyze'> Next </a>")


def analyze(request):
    return HttpResponse("<h1> <center> Analyzing </center> </h1> <br> <a href = 'home'> Back </a> <br> <a href = 'result'> Next </a>")


def result(request):
    return HttpResponse("<h1> <center> No Result Present </center> </h1> <br> <a href = 'analyze'> Back </a> ")


def template(request):
    variables = {'name' : 'Faizan' , 'place' : 'Mars'}
    return render(request, 'template.html' , variables)


def text_analyzer(request):
    return render(request, 'text-analyzer.html')


def about_us(request):
    return render(request , 'about-us.html')


def contact_us(request):
    return render(request , 'contact-us.html')

def analyzed(request):
    # Make empty list that saves us from throwing error if user doesn't check box , the value will be empty
    AnalyzedText = ['','','','']
    # Take text
    text_to_analyze = request.POST.get('text','No Text Given . . .')
    print(text_to_analyze)
    # Take response of check boxes
    IsCapitalize= request . POST.get('capitalize', 'off')
    IsUpper= request . POST.get('uppercase', 'off')
    IsLower= request . POST.get('lowercase', 'off')
    IsTitle= request . POST.get('title', 'off')
    
    # Checking for checkboxes and apply changes like .capitalize() or .upper e.t.c and append it on their corresponding positions
    if IsCapitalize == 'on':
        AnalyzedText[0]="Capitalize case : "+text_to_analyze.capitalize()
    if IsUpper == 'on':
        AnalyzedText[1]="UPPERCASE : "+text_to_analyze.upper()
    if IsLower == 'on':
        AnalyzedText[2]="lowercase : "+text_to_analyze.lower()
    if IsTitle == 'on':
        AnalyzedText[3]="Title Case : "+text_to_analyze.title()
    
    # Make variable list of corresponding values 
    print(AnalyzedText)
    Variables = {'text1':AnalyzedText[0] , 'text2':AnalyzedText[1] , 'text3':AnalyzedText[2] , 'text4':AnalyzedText[3]}
    return render(request, 'text-analyzer-result.html', Variables)
