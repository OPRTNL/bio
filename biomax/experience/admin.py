from django.contrib import admin
from .models import Experience, Mission

# Register your models here.

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('poste','created','start','end')

class MissionAdmin(admin.ModelAdmin):
    list_display = ('titre', 'description', 'Experience')

admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Mission, MissionAdmin)