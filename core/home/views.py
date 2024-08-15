from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    peoples =[
        {'name': 'Name1','age' : 20},
        {'name': 'Name2','age' : 21},
        {'name': 'Name3','age' : 22},
        {'name': 'Name4','age' : 23},
        {'name': 'Name5','age' : 16}
    ]
    vegetables = ["Tomato","Potato","Onion"]
    return render(request,"home/index.html",context={'page':'Django 2024','peoples':peoples,'vegetables':vegetables})


def about(request):
    page = "About Page"
    return render(request,"home/about.html",context={'page':page})


def contact(request):
    page = "Contact Page"
    return render(request,"home/contact.html",context={'page':page})


def success(request):
    return HttpResponse("<h1>This is a Success Page</h1>")