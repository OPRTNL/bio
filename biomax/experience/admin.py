from django.contrib import admin
from .models import Experience

# Register your models here.

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('nom','created')

admin.site.register(Experience, ExperienceAdmin)