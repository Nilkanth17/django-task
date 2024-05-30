from django.contrib import admin
from app.models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(item)
admin.site.register(login_ragister)

#.site.register(student)
class studentadmin(admin.ModelAdmin):  
    list_display=['id','name','roll_number','city',]

admin.site.register(Student, studentadmin)

