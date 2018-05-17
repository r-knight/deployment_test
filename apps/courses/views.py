from django.shortcuts import render, redirect, HttpResponse
from .models import *

def index(request):
    response = "placeholder for index page"
    if 'to_delete' in request.session:
        request.session.pop('to_delete')
    courses = Course.objects.all()
    return render(request, 'courses/index.html', {'courses': courses})

def destroy(request, uid):
    response = "placeholder for delete confirmation page for course " + str(uid)
    request.session['to_delete'] = uid
    course = Course.objects.get(id=uid)
    return render(request, 'courses/delete.html', {'course': course})

def delete_process(request):
    if request.method == 'POST':
        response = "placeholder for delete processing"
        deleted = Course.objects.get(id=request.session['to_delete'])
        deleted.delete()
        request.session.pop('to_delete')
        return redirect('/')
    else:
        return redirect('/')

def submit_course(request):
    response = "placeholder for submitting a course"
    errorCount = 0
    if request.POST['name']:
        request.session['name'] = request.POST['name']
        if len(request.session['name']) < 5:
            errorCount +=1
    else:
        errorCount +=1
    if request.POST['description']:
        request.session['description'] = request.POST['description']
        if len(request.session['description']) < 15:
            errorCount +=1
    else:
        errorCount +=1
    if errorCount == 0:
        newCourse = Course(name=request.session['name'])
        newCourse.save()
        description = Description(course=newCourse, text=request.session['description'])
        description.save()
        request.session.pop('description')
        request.session.pop('name')
        return redirect('/')
    else:
        return redirect('/')
    return HttpResponse(response)
