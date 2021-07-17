from django import forms
from .models import Activity


class NewActivityForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    description = forms.CharField(required=True, max_length=200,
                                  widget=forms.Textarea(attrs={'placeholder': 'Activity Description'}))
    cost_estimation = forms.IntegerField(required=True)

    class Meta:
        model = Activity
        fields = ["title", "description", "picture", "cost_estimation"]
