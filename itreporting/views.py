from django.shortcuts import render
from django.http import HttpResponse
from . import views
# Create your views here.

app_name = 'itreporting' 

def home(request):
    return HttpResponse('IT service App - Home')

def about(request):
    return render(request, 'itreporting/home.html')