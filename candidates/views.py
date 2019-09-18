from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
#from .forms import SearchForm
from .models import Candidate, Job, User
from django.views import View
from django.views.generic import ListView, DetailView
# Create your views here.
    
class CandidateList(ListView):
    template_name = 'candidates/candidates.html'
    model = Candidate

def candidate_detail(request,candidate_id):
	candidate = get_object_or_404(Candidate,pk=candidate_id)
	return render(request,'candidates/candidate_detail.html',{'candidate':candidate})


class JobList(ListView):
    template_name = 'candidates/jobs.html'
    model = Job

def jobs_detail(request,job_id):
	job = get_object_or_404(Job,pk=job_id)
	return render(request,'candidates/job_detail.html',{'job':job})

    
    
def home(request):
    # form = SearchForm()
    return render(request,'candidates/home.html')