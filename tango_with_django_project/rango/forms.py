import django.forms
import rango.models

class CategoryForm(django.forms.ModelForm):
    name = django.forms.CharField(max_length=128, help_text="Please enter the category name.")
    views = django.forms.IntegerField(widget=django.forms.HiddenInput(), initial=0)
    likes = django.forms.IntegerField(widget=django.forms.HiddenInput(), initial=0)
    
    class Meta:
        model = rango.models.Category

class PageForm(django.forms.ModelForm):
    name = django.forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = django.forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = django.forms.IntegerField(widget=django.forms.HiddenInput(), initial=0)
    
    class Meta:
        model = rango.models.Page
        
        fields = ('title','url','views')