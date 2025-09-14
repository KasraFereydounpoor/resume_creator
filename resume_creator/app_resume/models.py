from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _





User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("User"), on_delete=models.CASCADE)
    experience_count = models.IntegerField(_("Experience count"), default=0)
    project_count = models.IntegerField(_("Project count"), default=0)
    position = models.CharField(_("Position"), max_length=50 , help_text=_('Current position at the company or project you are working now'))
    title = models.CharField(_("Title"), max_length=50 , help_text=_('Your job title'))
    phone_number = models.CharField(_("Phone number"), max_length=12 , help_text=_('Your phone number'))
    about_me = models.TextField(_("About me"), null=True , max_length=10000 , help_text=_('A brief description about yourself'))
    facebook = models.URLField(_("Facebook"), null=True , help_text=_('Link to your Facebook profile'))
    twitter = models.URLField(_("Twitter"), null=True , help_text=_('Link to your Twitter profile'))
    google_plus = models.URLField(_("Google Plus"), null=True)
    linkedin = models.URLField(_("LinkedIn"), null=True)
    github = models.URLField(_("GitHub"), null=True)


    
class Experience(models.Model):
    user = models.ForeignKey(User ,verbose_name=_("User"), on_delete=models.CASCADE)
    title  = models.CharField(_("Title"), null=True , max_length=50)
    description = models.TextField(_("Description"), null=True , max_length=200)
    employer = models.CharField(_("Employer"), null=True , max_length=50)
    employee_start_date = models.DateField(_("Employee start date"), null=True)
    employee_end_date = models.DateField(_("Employee end date"), null=True)
    
    
    
class Skill(models.Model):
    user = models.ForeignKey(User ,verbose_name=_("User"), on_delete=models.CASCADE)
    title = models.CharField(_("Title"), null=True , max_length=50)
    description = models.TextField(_("Description"), null=True , max_length=200)
    image = models.ImageField(_("Image"), upload_to='skills' , null=True)

class Education(models.Model):
    user = models.ForeignKey(User ,verbose_name=_("User"), on_delete=models.CASCADE)
    title = models.CharField(_("Title"), null=True , max_length=50)
    description = models.TextField(_("Description"), null=True , max_length=200)
    academy_title = models.CharField(_("Academy title"), null=True , max_length=50)
    start_date = models.DateField(_("Start date"), null=True)
    end_date = models.DateField(_("End date"), null=True)