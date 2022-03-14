from django.shortcuts import render

def List_Courses(request):
	return render(request,'courses/list_courses.html')