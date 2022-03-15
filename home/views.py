from django.shortcuts import render
from .models import *
from subjects.models import *
from blog.models import *

def home(request):
	modificate = Modificate.objects.last()
	request.session['title'] = modificate.title
	request.session['logo'] = modificate.logo.url
	about = About.objects.last()
	category = Category.objects.all()
	courses = Subject.objects.filter(new = True)
	post = Post.objects.filter(new=True)
	return render(request,'index.html',{'m':modificate,'a':about,'categories':category,'courses':courses,'post':post})

def about(request):
	return render(request,'about.html')

def contact(request):
	return render(request,'contact.html')