from django import forms
from rango.models import Page,Category

class CategoryForm(forms.ModelForm):
    name= forms.CharField(max_length=128,help_text="please enter what do you want?")
    views= forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    likes =forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    slug =forms.CharField(widget=forms.HiddenInput(),required=False)

    class Meta:
        model = Category
        fileds = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128,help_text="please enter the title of the page")
    url = forms.URLField(max_length=200,help_text="pleas enter the url of the page")
    views =forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model =Page
        exclude=('catogory',)



