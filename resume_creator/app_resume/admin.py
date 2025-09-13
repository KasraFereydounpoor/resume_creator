from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import Profile, Experience, Skill, Education

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
    


admin.site.unregister(User)
admin.site.register(User , UserAdmin)

admin.site.register(Profile)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Education)
