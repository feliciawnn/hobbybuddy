from django import forms
from .models import Activity, Category


class NewActivityForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    description = forms.CharField(required=True,
                                  widget=forms.Textarea(attrs={'placeholder': 'Activity Description'}))
    cost_estimation = forms.IntegerField(required=True)

    class Meta:
        model = Activity
        fields = ["title", "description", "picture", "cost_estimation"]


class NewCategoryForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Name'}))

    class Meta:
        model = Category
        fields = ["name"]


class CategoryChooser(forms.Form):
    def __init__(self, *args, **kwargs):
        categories = kwargs.pop('categories')
        super(CategoryChooser, self).__init__(*args, **kwargs)

        for i, category in enumerate(categories):
            self.fields["cat%s"%i] = forms.BooleanField(label=category, required=False)


class ActivityCategoryForm(forms.Form):
    def __init__(self, *args, **kwargs):
        categories = kwargs.pop('categories')
        super(ActivityCategoryForm, self).__init__(*args, **kwargs)

        for i, category in enumerate(categories):
            self.fields["cat%s" % i] = forms.BooleanField(label=category, required=False)