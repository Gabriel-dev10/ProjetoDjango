from django.shortcuts import render

def index(request):
    return render(request, 'eng_software/index.html')