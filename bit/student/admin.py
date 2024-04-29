from django.contrib import admin
from .models import Student, Group, Mark

class StudentInline(admin.TabularInline):
    model = Student

class GroupAdmin(admin.ModelAdmin):
    inlines = [StudentInline]

class MarkInline(admin.TabularInline):
    model = Mark

class StudentAdmin(admin.ModelAdmin):
    inlines = [MarkInline]


admin.site.register(Group, GroupAdmin)
admin.site.register(Student, StudentAdmin)

