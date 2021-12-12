from django.contrib import admin
from .models import *
# Register your models here.
class StudentSlug(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class ArticleSlug(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class SupportSlug(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class ExecutiveSlug(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class LessonSlug(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Activity, ArticleSlug),
admin.site.register(Support_for_Students, SupportSlug),
admin.site.register(Contact),
admin.site.register(Executive, ExecutiveSlug),
admin.site.register(AboutUs),
admin.site.register(Student, StudentSlug),
admin.site.register(Lesson, LessonSlug),




