from django.shortcuts import render
from .models import School_info, Latest_Post
# Create your views here.

def index(request):

    schls = School_info.objects.all()

    return render(request, 'index.html', {'schls':schls})

def contact(request,):

    return render(request, 'contact.html')

def about(request,):

    return render(request, 'about.html')

def news(request):

    news = Latest_Post.objects.all()
    return render(request, 'news.html', {'news':news})

