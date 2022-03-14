from django.shortcuts import render

def Blog(request):
	return render(request,'blog/blog.html')

def Single(request):
	return render(request,'blog/single.html')
