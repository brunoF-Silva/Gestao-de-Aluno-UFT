from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
  print('home')
  return render(
    request,
    'home/index.html'
  )

def cadastrar(request):
  print('cadastro')
  return HttpResponse('cadastrar')