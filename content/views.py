from django.shortcuts import render

def home(request):
    return render(request,'content/home.html',{})

def backgd(request):
    return render(request,'content/backgd.html',{})

def projs(request):
    return render(request,'content/projs.html',{})

def contact(request):
    return render(request,'content/contact.html',{})
