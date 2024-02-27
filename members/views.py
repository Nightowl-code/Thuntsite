from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import SubmittedData
from django.utils import timezone
import pytz
import collections

# Create your views here.

curr_indian_timezone=0
start_indian_timezone=0
correct_answer_list=["n","n","n","n","n","n","n","n"]

def validate_text(text):
    md_text=str(text).lower().strip()
    return md_text

def login_user(request):
    global start_indian_timezone
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            start=timezone.now()
            start_indian_timezone = start.astimezone(pytz.timezone('Asia/Kolkata')).replace(hour=12, minute=0, second=0, microsecond=0)
            # start_indian_timezone = start.astimezone(pytz.timezone('Asia/Kolkata'))
            print(start_indian_timezone,"start timer")
            login(request,user)
            messages.success(request,("Logged in successfully. Your time has started!"))
            return redirect(f"/question1/{request.user}")
        else:
            messages.success(request,("please enter given id and password"))
            # return render(request,"login.html")# render to see message
            return redirect("/")
    else:
        return render(request,"login.html")
    
def question1(request,name):
    global correct_answer_list
    if request.user.is_authenticated:
        if request.method=="POST":
            answer=validate_text(request.POST["answer"])
            correct_answer="answer1"
            if answer==correct_answer:
                correct_answer_list[0]="y"
                messages.success(request,'Correct answer')
                return redirect(f'/question2/{request.user}')
            else:
                messages.success(request,'The answer is incorrect')
                return render(request,'question1.html')
        else:
            return render(request,'question1.html')        
    else:
        return redirect('/')
    
def question2(request,name):
    global correct_answer_list
    if request.user.is_authenticated:
        if request.method=="POST":
            answer=validate_text(request.POST["answer"])
            correct_answer="answer2"
            if answer==correct_answer:
                correct_answer_list[1]="y"
                messages.success(request,'Correct answer. You have successfully completed the quiz.')
                return redirect(f'/complete/{request.user}')
            else:
                messages.success(request,'The answer is incorrect')
                return render(request,'question2.html')
        else:
            return render(request,'question2.html')         
    else:
        return redirect('/')
    
def complete(request,name):
    if request.user.is_authenticated:
        return render(request,'complete.html')
    else:
        return redirect('/')

def logout_user(request):
    global curr_indian_timezone
    global correct_answer_list
    
    print(collections.Counter(correct_answer_list))
    print(correct_answer_list," list of questions solved")
    curr=timezone.now()
    curr_indian_timezone=curr.astimezone(pytz.timezone('Asia/Kolkata'))
    print(curr_indian_timezone,"current time")
    resTime=str(curr_indian_timezone-start_indian_timezone).split(":")
    print(f"{resTime[0]} hr | {resTime[1]} min | {resTime[2]} sec")
    logout(request)
    return redirect("login")