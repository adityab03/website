from django.http import HttpResponse
from django.shortcuts import render
from .models import Clothes

def index(request):
    all_clothess = Clothes.objects.all()
    context = {
        'all-clothess': all_clothess,
    }
    return render(request, 'pakaian')

def detail(request, clothes_id):
    return HttpResponse("<h2>Details for Clothes id: " + str(clothes_id) + "</h2>")