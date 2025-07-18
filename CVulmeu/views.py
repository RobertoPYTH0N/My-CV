from django.shortcuts import render
from django.http import HttpResponse
from .forms import FormularMesaj
from django.contrib import messages

def pagina_efectiva(request):
    form = FormularMesaj()
    return render(request, "paginaefectiva.html", {'form': form})

def confirmare_mesaj(request):
    if request.method == 'POST':
        form = FormularMesaj(request.POST)
        if form.is_valid():
            messages.success(request, "Your message has been sent successfully!")
            form.save()
    return render(request, 'afosttrimis.html')