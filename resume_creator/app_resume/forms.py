from django import forms, froms

class ResumeForm(forms.Form):
    about_me = forms.CharField(label='About_Me' , max_length=1000 , help_text = 'Write a brief description about yourself.')