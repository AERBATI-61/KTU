from django.db import models
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
# from easy_pdf.views import PDFTemplateResponseMixin
from django.views.generic import DetailView
from django.views import View
from .forms import *
import random
from .models import *
from django.core.paginator import Paginator, EmptyPage

# **************** csv and excel ***********
import csv
from django.http import HttpResponse
import datetime
import xlwt

# **************** pdf ***********
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A3

from .deneme import *


def home(request):
    students = Student.objects.all()
    lessons = Lesson.objects.all()
    supports = Support_for_Students.objects.all()
    activities = Activity.objects.all()




    selected_students = []
    selected_activities = []
    while len(selected_students) < 3:
        student = random.choice(students)
        if student not in selected_students:
            selected_students.append(student)


    while len(selected_activities) < 3:
        activity = random.choice(activities)
        if activity not in selected_activities:
            selected_activities.append(activity)

    context = {
        'students': students,
        'selected_students': selected_students,
        'selected_activities': selected_activities,
        'lessons': lessons,
        'suppprts': supports,
        'activities': activities,


    }
    return render(request, 'home.html', context)




def StudentsList(request):
    keyword = request.GET.get("keyword")
    if keyword:
        students = Student.objects.filter(name__contains=keyword)
        return render(request, "students.html", {'students': students})

    context = {}

    ogrenciler = Student.objects.all()
    page_n = request.GET.get('page', 1)
    p = Paginator(ogrenciler, 7)
    try:
        page = p.page(page_n)
    except EmptyPage:
        page = p.page(1)

    students = Student.objects.all()
    context['students'] = students
    context['students'] = page

    return render(request, "students.html", context)


class StudentDetail(DetailView):
    model = Student
    context_object_name = 'student'
    template_name = 'student_detail.html'





class ExecutivesList(ListView):
    model = Executive
    context_object_name = 'executives'
    template_name = 'executives.html'

class ExecutiveDetail(DetailView):
    model = Executive
    context_object_name = 'executive'
    template_name = 'executive_detail.html'







class ActivitiesList(ListView):
    model = Activity
    context_object_name = 'activities'
    template_name = 'activity.html'

class ActivityDetail(DetailView):
    model = Activity
    context_object_name = 'activity'
    template_name = 'activity_detail.html'






class LessonsList(ListView):
    model = Lesson
    context_object_name = 'lessons'
    template_name = 'lessons.html'

class LessonDetail(DetailView):
    model = Lesson
    context_object_name = 'lesson'
    template_name = 'lesson_detail.html'






def support_for_students(request):
    context = {
        'supports': Support_for_Students.objects.all()
    }
    return render(request, 'supports.html', context)

class Support_for_StudentsDetail(DetailView):
    model = Support_for_Students
    context_object_name = 'support'
    template_name = 'support_detail.html'







def aboutview(request):
    context = {
        'aboutus': AboutUs.objects.all()[1:2]
    }
    return render(request, 'aboutus.html', context)






class Contactview(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contact.html', context={'form': ContactForm()})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST or None)
        if form.is_valid():
            c_form = form.save(commit=False)
            c_form.save()
            return render(request, 'contact.html', context={'form': ContactForm()})










def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Conten-Disposition'] = 'attachment; filename = Student' + str(datetime.datetime.now()) + '.csv'
    writer = csv.writer(response)
    writer.writerow(['name', 'studentID', 'email', 'nationality', 'department', 'degree_level'])
    students = Student.objects.all()
    for student in students:
        writer.writerow([student.name, student.studentID,
                         student.email, student.nationality, student.department, student.degree_level])
    return response



def export_excel(request):
    response = HttpResponse(content_type='application/ms_excel')
    response['Conten-Disposition'] = 'attachment; filename = Student' + str(datetime.datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Student')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['name', 'studentID', 'email', 'nationality', 'department', 'degree_level']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    rows = Student.objects.filter(name=request.user).values_list(
        'name', 'studentID', 'email', 'nationality', 'department', 'degree_level')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response



# def venue_pdf(request):
#     buf = io.BytesIO()
#     c = canvas.Canvas(buf, pagesize=A3, bottomup=0)
#     textob = c.beginText()
#     textob.setTextOrigin(inch, inch)
#     textob.setFont("Helvetica", 12)
#     space = "   "
#     venues = Student.objects.all()
#     lines = []
#     for venue in venues:
#         lines.append(
#                     venue.name + space + venue.phone + space + venue.email
#                     + space + str(venue.university) + space + venue.department
#                     + space + venue.degree_level
#                      )
#         lines.append(" ")
#     for line in lines:
#         textob.textLine(line)
#
#     c.drawText(textob)
#     c.showPage()
#     c.save()
#     buf.seek(0)
#
#     return FileResponse(buf, as_attachment=True, filename='kayitli_ogrenciler.pdf')



