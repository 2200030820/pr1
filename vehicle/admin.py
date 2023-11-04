from django.contrib import admin

from .models import Customer,Mechanic,Request,Attendance,Feedback



admin.site.register(Customer)
admin.site.register(Request)
admin.site.register(Attendance)
admin.site.register(Feedback)

admin.site.register(Mechanic)

