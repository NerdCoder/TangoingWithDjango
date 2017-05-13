from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context_dict = {'boldmessage': "Django, Tango, Rango, Mango!!"}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return HttpResponse(
        """
        Rango is real thirsty!
        </br>
        <a href='/'> Home </a>
        </br>
        <a href='/rango'> Rango </a>
        """
    )
