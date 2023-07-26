from django.shortcuts import render

# Create your views here.
def course_detail(request, course_name):
    return render(request, 'course_detail.html', {'course_name': course_name})