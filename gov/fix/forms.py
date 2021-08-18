from django import forms
from models import Issue

class IssueForm(forms.ModelForm):
    title = forms.CharField(label="Title")
    description = forms.CharField(label="Description")
    latitude = forms.FloatField(label="Latitude")
    longitude = forms.FloatField(label="Longitude")

    class Meta:
        model = Issue
        fields = ('title', 'image')