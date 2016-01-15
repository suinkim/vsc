from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Job


def index(request):
    latest_job_list = Job.objects.order_by('-pub_date')[:5]
    context = {'latest_job_list': latest_job_list}
    return render(request, 'mande/index.html', context)

def detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'mande/detail.html', {'job': job})

def results(request, job_id):
    response = "You're looking at the results of job %s."
    return HttpResponse(response % job_id)

def vote(request, job_id):
    return HttpResponse("You're voting on job %s." % job_id)
