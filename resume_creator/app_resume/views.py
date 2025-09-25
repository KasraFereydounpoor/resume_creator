from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app_resume.forms import ProfileForm, SocialLinksForm, ExperienceForm
from django.contrib import messages


def index(request):
    return render(request, 'index.html')

@login_required
def resume(request):
    return render(request, 'resume.html')


@login_required
def edit(request):
    if request.method == "POST":
        profile_form = ProfileForm(request.POST)
        social_links_form = SocialLinksForm(request.POST)
        experience_form = ExperienceForm(request.POST)
        if profile_form.is_valid() and social_links_form.is_valid() and experience_form.is_valid():
            request.user.profile.about_me = profile_form.cleaned_data['about_me']
            request.user.profile.facebook = request.POST.get('facebook')
            request.user.profile.twitter = request.POST.get('twitter')
            request.user.profile.google_plus = request.POST.get('google_plus')
            request.user.profile.linkedin = request.POST.get('linkedin')
            request.user.profile.github = request.POST.get('github')
            request.user.profile.save()

            experience_exists = request.user.experience_set.exists()
            if experience_exists:
                experience = request.user.experience_set.first()
                experience.title = request.POST.get('title')
                experience.description = request.POST.get('description')
                experience.employer = request.POST.get('employer')
                experience.employee_start_date = request.POST.get('employee_start_date')
                experience.employee_end_date = request.POST.get('employee_end_date')
                experience.save()
            else:
                request.user.experience_set.create(
                    title=request.POST.get('title'),
                    description=request.POST.get('description'),
                    employer=request.POST.get('employer'),
                    employee_start_date=request.POST.get('employee_start_date'),
                    employee_end_date=request.POST.get('employee_end_date'),
                )

            messages.add_message(request, messages.SUCCESS, "Saved successfully")
        else:
            messages.add_message(request, messages.ERROR, "Fill the form")
    else:
        profile_form = ProfileForm(initial=request.user.profile.__dict__)
        social_links_form = SocialLinksForm(initial=request.user.profile.__dict__)
        experience_form = ExperienceForm(initial={
            'title': request.user.experience_set.first().title,
            'description': request.user.experience_set.first().description,
            'employer': request.user.experience_set.first().employer,
            'employee_start_date': request.user.experience_set.first().employee_start_date,
            'employee_end_date': request.user.experience_set.first().employee_end_date,
        })
    return render(request, 'edit.html', {
        'profile_form': profile_form,
        'social_links_form': social_links_form,
        'experience_form': experience_form
    })