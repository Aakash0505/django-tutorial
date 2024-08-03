from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"home/index.html")


def success(request):
    return HttpResponse("<h1>This is a Success Page</h1>")