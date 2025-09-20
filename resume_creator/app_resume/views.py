from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app_resume.forms import ResumeForm

def index(request):
    return render(request , 'index.html')

@login_required
def resume(request):
    return render(request , 'resume.html' )


@login_required
def edit(request):
    form = ResumeForm()
    return render(request , 'edit.html' , {'form': form})


