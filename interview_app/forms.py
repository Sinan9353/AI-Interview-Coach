from django import forms

class ResumeForm(forms.Form):

    resume = forms.FileField()

    ROLE_CHOICES = [
        ('Frontend Developer', 'Frontend Developer'),
        ('Backend Developer', 'Backend Developer'),
        ('Data Analyst', 'Data Analyst'),
    ]

    role = forms.ChoiceField(choices=ROLE_CHOICES)