from django import forms
from .models import Category

class CategoryForms(forms.ModelFrom):

    class Meta:
        model = Category
        filds = '__all__'