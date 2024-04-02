from django.contrib import admin
from .models import Carlist,Showroomlist,Review

# Register your models here.
admin.site.register(Carlist)
admin.site.register(Showroomlist)
admin.site.register(Review)