from django.contrib import admin

from capp.models import Department, Course, Material

# Register your models
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Material)