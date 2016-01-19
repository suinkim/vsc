from django.contrib import admin
from .models import Job, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

class JobAdmin(admin.ModelAdmin):
    list_display = ('job_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['job_text']
    inlines = [ChoiceInline]

admin.site.register(Job, JobAdmin)
