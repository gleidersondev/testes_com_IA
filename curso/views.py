from django.shortcuts import render

def landing_page(request):
    return render(request, 'curso/landing.html')
