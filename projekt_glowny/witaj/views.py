from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def hello(request):
    return HttpResponse("Witaj w Django!")

def hello_name(request, name):
    return HttpResponse(f"Witaj, {name}!")

def hello_template(request, name):
    return render(request, "witaj/hello.html", {"name": name})

def show_time(request):
    now = datetime.now() 
    formatted_time = now.strftime("Dzisiaj jest: %d.%m.%Y, godzina: %H:%M") 

    context = {
        'time_info': formatted_time
    }

    return render(request, "witaj/time.html", context)