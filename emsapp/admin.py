from django.contrib import admin

# Register your models here.
from .models import Employee, LatestNews, Calendar

admin.site.register(Employee)
admin.site.register(LatestNews)
admin.site.register(Calendar)