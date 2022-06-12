from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),


    path('students/', StudentsList, name='students'),
    path('students/<slug:slug>/', StudentDetail.as_view(), name='student-detail'),
    # path('<int:pk>', pdfDetail.as_view(), name='pdf_detail'),
    path('export-csv/', export_csv, name='export-csv'),
    path('export-excel/', export_excel, name='export-excel'),
    # path('venue-pdf/', venue_pdf, name='venue-pdf'),


    path('executives/', ExecutivesList.as_view(), name='executives'),
    path('executives/<slug:slug>/', ExecutiveDetail.as_view(), name='executive-detail'),

    path('activities/', ActivitiesList.as_view(), name='activities'),
    path('activities/<slug:slug>/', ActivityDetail.as_view(), name='activity-detail'),

    path('lessons/', LessonsList.as_view(), name='lessons'),
    path('lessons/<slug:slug>/', LessonDetail.as_view(), name='lesson-detail'),

    path('support-programs/', support_for_students, name='support-programs'),
    path('supports-programs/<slug:slug>/', Support_for_StudentsDetail.as_view(), name='support-program'),

    path('about-us/', aboutview, name='aboutus'),
    path('contact-us/', Contactview.as_view(), name='contactus'),




]

