from django.http import HttpResponse
from django.shortcuts import render, redirect

from imageshop.models import *




def show_home_page(request):

    cats = Category.objects.all()
    images = Image.objects.all()



    data={'images':images, 'cats':cats}
    return render(request , "home.html",data)





