from django.http import HttpResponse , HttpResponseRedirect , HttpResponseBadRequest
from django.shortcuts import render , redirect
from .forms import *
from credentials.models import Credential , Product
from django.core.paginator import Paginator
from django.core.mail import send_mail
from functools import wraps

# Email Feedback
def feedback(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.method == 'POST':
            email = request.POST.get("email")
            subject = request.POST.get("subject")
            body = request.POST.get("body")
            
            if email and subject and body:
                try:
                    send_mail(
                        subject=subject,
                        message=f"{body}",
                        from_email='legendslegecy1@gmail.com',  # MUST match EMAIL_HOST_USER
                        recipient_list=['legendslegecy2@gmail.com'],
                        fail_silently=False
                    )
                    print("Mail sent")
                    request.feedbackstatus = 'success'
                except Exception as e:
                    print(e)
                    request.feekbackstatus = 'error'
            else:
                request.feedbackstatus = 'fail'
        
        return view_func(request, *args, **kwargs)
    return wrapper




# Introduction
def home (request):
    return HttpResponse("<br><br><br><br><br><br><br><br><br><br><br><br><br><center><h1><big><hr>Hello, world! This is the home page.<hr></big></center></h1>")
def course (request):
    return HttpResponse("<br><br><br><br><br><br><br><br><br><br><br><br><br><center><h1><big><hr>Which course are you seeking for? <hr></big></center></h1>")


# Dynamic url
def coursedetails (request,coursename):
    return HttpResponse(f"<br><br><br><br><br><br><br><br><br><br><br><br><br><center><h1><big><hr>{coursename} isn't available right now.<hr></big></center></h1>")


# Templates
@feedback
def index(request):
    feedbackstatus = getattr(request, 'feedbackstatus', None)
    return render(request, 'index.html', {'feedbackstatus': feedbackstatus})


# Data parsing
def calculator(request):
    result = None
    if request.method == 'POST':
        num1 = request.POST.get("num1")
        num2 = request.POST.get("num2")
        operation = request.POST.get("operation")
        
        if num1 and num2 and operation:
            try:
                num1 = float(num1)
                num2 = float(num2)
                
                if operation == '+':
                    result = num1 + num2
                elif operation == '-':
                    result = num1 - num2
                elif operation == '*':
                    result = num1 * num2
                elif operation == '/':
                    if num2 != 0:
                        result = num1 / num2
                    else:
                        result = "Cannot divide by zero"
                else:
                    result = "Invalid operation"
            except ValueError:
                result = "Please enter valid numbers"
    
    return render(request, 'calculator.html', {'result': result})


# for loop and if statement   
def table(request):
    data={}
    if request.method=='POST':
        num=int(request.POST.get("number"))
        results = [num * i for i in range(1, 11)]
        data = {'number':num , "results":results}
        
    return render(request, 'table.html',data)


# Static files
def happybirthday(request):
    return render(request, 'HappyBirthday.html')
def happybirthday2(request):
    return render(request, 'HappyBirthday2.html')


# Extend and include
# Models Practice 
# Filters
# tinymce module : give access to word options like bold,italic...(description)
# Marquee tag: slider like in which news are running BREAKING NEWS or NEWS EXCLUSIVE
# AUTOSLUGFIELD FROM auto-slug
# PAGINATION
@feedback
def productlist(request):
    feedbackstatus = getattr(request, 'feedbackstatus', None)
    page_number = request.GET.get('page')
    if not page_number:
        page_number = '1'
    product = Product.objects.all().order_by("-price")
    paginator = Paginator(product, 3)
    finaldata =  paginator.get_page(page_number) 
    totalpages = finaldata.paginator.num_pages
        
    return render(request,'product_list.html',{'products': finaldata,'current_page':int(page_number),'lastpage':totalpages,'feedbackstaus':feedbackstatus})

@feedback
def productdetails(request,title_slug):
    feedbackstatus = getattr(request, 'feedbackstatus', None)
    product = Product.objects.get(slug=title_slug)
    return render(request,'product_detail.html',{'products':product,'feedbackstatus': feedbackstatus})



# url in Django
@feedback
def aboutus(request):
    feedbackstatus = getattr(request, 'feedbackstatus', None)
    return render(request,'aboutus.html',{'feedbackstatus': feedbackstatus})
@feedback
def contactus(request):
    if request.method == 'GET':
            email = request.GET.get("email")
            subject = request.GET.get("subject")
            body = request.GET.get("body")
            
            if email and subject and body:
                try:
                    send_mail(
                        subject=subject,
                        message=f"{body}",
                        from_email='legendslegecy1@gmail.com',  
                        recipient_list=['legendslegecy2@gmail.com'],
                        fail_silently=False
                    )
                    print("Mail sent")
                    request.feedbackstatus = 'success'
                except Exception as e:
                    print(e)
                    request.feekbackstatus = 'error'
            else:
                request.feedbackstatus = 'fail'
        
    feedbackstatus = getattr(request, 'feedbackstatus', None)
    return render(request,'contactus.html',{'feedbackstatus': feedbackstatus})


# Django Forms
def samplelogin(request):
    data ={}
    form = sampleloginform()
    data['form'] = form
    try:
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")
            if username and password:
                return HttpResponseRedirect("/")
    except:
        pass
    
    return render (request,'samplelogin.html',data)


# Models in database
def signup(request):
    if request.method == 'POST':
        signup_username = request.POST.get("signup-email")
        signup_password = request.POST.get("signup-password")
        signup_confirm = request.POST.get("signup-confirm")
        
        login_username = request.POST.get("login-email")
        login_password = request.POST.get("login-password")

        if signup_username and signup_password and signup_confirm==signup_password:
            model = Credential(username=signup_username, password=signup_password)
            model.save()
        elif signup_username and signup_password and signup_confirm!=signup_password:
            return render(request,'signup.html',{"error":"Password and Confirm Password do not match."})
        
        
        if login_username and login_password:
            try:
                model= Credential.objects.get(username=login_username, password=login_password)
                return HttpResponseRedirect("/dashboard/")
            except Credential.DoesNotExist:
                return render(request,'signup.html',{"error":"Invalid Credentials"})

            
    return render (request,'signup.html')



# use of filter and __icontains
@feedback
def search(request):
    if request.method == 'GET':
        search_query = request.GET.get("q")
        if search_query:
            products = Product.objects.filter(name__icontains=search_query)
            if not products:
                products = Product.objects.filter(description__icontains=search_query)
                if not products:
                    products = Product.objects.filter(price__icontains=search_query)
                    if not products:
                        return render(request, 'search.html', {'products': [], 'query': search_query, 'error': 'Oops! No products found.'})

            return render(request, 'search.html', {'products': products, 'query': search_query})
    return redirect("/dashboard")