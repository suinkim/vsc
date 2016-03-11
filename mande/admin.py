from django.contrib import admin
from .models import Job, Volunteer

class VolunteerInline(admin.TabularInline):
    model = Volunteer
    extra = 0

class JobAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'date', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['job_title']
    inlines = [VolunteerInline]

admin.site.register(Job, JobAdmin)
