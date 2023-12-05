from django import forms
from news.models import Category


class CategoriesForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=200)

    def save(self):
        data = self.cleaned_data
        category = Category.objects.create(
            name=data['name']
        )
        category.save()
