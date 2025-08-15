from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render
from .form import *

def home(request):

    data = {
        "Programmer_Name":"Faizan Liaqat",
        "Age" : "16",
        "Languages" : ['Python' , 'Html' , 'CSS' ],
        "Contacts" : {
            "Whatsapp" : "+923064073681",
            "Email_1" : "legendslegecy1@gmail.com" , 
            "Email_2" : "legendslegecy2@gmail.com" , 
        },
        "Numbers" : [33 , 65 , 2 , 90 ,0,0],
    }
    return render(request , 'home.html' , data)


def Course_Name(request , CourseName):
    return HttpResponse(f"<center><h1>{CourseName}</h1></center>")


def Happy_Birthday(request):
    return render (request,"HappyBirthday.html")

def Happy_Birthday2(request):
    return render (request,"HappyBirthday2.html")


def aboutus(request):
    return render(request , 'about-us.html')

def contact(request):
    return render(request , 'contact.html')

def offers(request):
    return render(request , 'offers.html')

def dashboard(request):
    username = request.POST.get("username")
    data = {'username' : username,}
    
    return render (request,"dashboard.html",data)


def login(request ):
    try:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        if username != None and password != None:
            # return HttpResponseRedirect("/dashboard/")
            return HttpResponseRedirect(f"/dashboard/?username={username}")

    except:
        pass
    
    form = CreateForm()
    data = {'form': form,}
    return render(request , 'login.html',data)





def calculator(request):
    result = 0
    try:
        value1 = int(request.GET.get('value1'))
        value2 = int(request.GET.get('value2'))
        operator = request.GET.get("operator")
        match operator:
            case '+':
                result = value1 + value2
            case '-':
                result = value1 - value2
            case '*':
                result = value1 * value2
            case '/':
                result = value1 / value2

        # if value1 != None and value2 != None:
        #     return HttpResponseRedirect("/calculator/")

    except:
        pass
    
    form = Calculator()
    data = {'form': form,'result':result}

    return render(request , 'calculator.html',data)


def even_odd(request,methods=['GET','POST']):
    Value = ''
    try:
        Value = int(request.GET.get('Value'))
        if Value %2 == 0:
            Value = 'Even'
        else:
            Value = 'Odd'
        
    except:
        pass

    form = Even_Odd()
    data = {
        'form' : form,
        'Value':Value,
    }
    return render(request , 'even-odd.html',data)


def marksheet(request):
    total = ''
    perc = ''
    div = ''

    try:
        s1 = int( request.GET.get("Subject1") )
        s2 = int( request.GET.get("Subject2") )
        s3 = int( request.GET.get("Subject3") )
        s4 = int( request.GET.get("Subject4") )
        s5 = int( request.GET.get("Subject5") )

        total = s1 + s2 + s3 + s4 + s5
        perc = round((total / 500)*100 , 2)
        
        if perc >= 60 :
            div = 'First Division'
        elif perc >= 48 :
            div = 'Second Division'
        elif perc >= 35 :
            div = 'Third Division'
        else :
            div = 'Fail'

    except:
        pass
    
    form = Worksheet()
    data = {
        'form':form,
        'Total':f"Total : {total}",
        'Percentage': f"Percentage : {perc}%",
        'Division':f"Division : {div}",
    }
    return render( request , 'marksheet.html' , data)
