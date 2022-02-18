from django.shortcuts import render

def hello(request):
    response = 'Uma string qualquer'
    return render(request, 'hello/index.html',{
      'name': 'Diogo' 
    })
