from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import Profile, Experience, Skill, Education
from django.utils.translation import gettext_lazy as _



User = get_user_model()



class ProfileInLine(admin.StackedInline):
    model = Profile


class SkillInLine(admin.TabularInline):
    model = Skill
    extra = 0
    
class EducationInLine(admin.TabularInline):
    model = Education
    extra = 0
    
class ExperienceInLine(admin.TabularInline):
    model = Experience
    extra = 0
class UserAdmin(DjangoUserAdmin):
    inlines = [ProfileInLine , EducationInLine , ExperienceInLine , SkillInLine]
    
    def get_fieldsets(self, request, obj = None):
        fieldsets = super().get_fieldsets(request, obj)
        normal_user_fieldset = (
            (None , {"fields":("username" , "password")}),
            (_("Personal info"), {"fields": (("first_name", "last_name"), "email")}),
        )
        return fieldsets if request.user.is_superuser else normal_user_fieldset



    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs if request.user.is_superuser else qs.filter(id=request.user.id)

# Unregister the default User model admin and register our custom UserAdmin

admin.site.unregister(User)
admin.site.register(User , UserAdmin)

# admin.site.register(Profile)
# admin.site.register(Experience)
# admin.site.register(Skill)
# admin.site.register(Education)
