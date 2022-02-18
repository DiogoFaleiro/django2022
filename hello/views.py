from django.shortcuts import render

def hello(request):
    response = 'Uma string'
    return render(request, 'hello/index.html',{
      'name': 'Diogo' 
    })
