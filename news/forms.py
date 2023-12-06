from django import forms
from news.models import Category, News, User


class CategoriesForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=200)

    def save(self):
        data = self.cleaned_data
        category = Category.objects.create(
            name=data['name']
        )
        category.save()


class NewsForm(forms.Form):
    title = forms.CharField(label='Título')
    content = forms.CharField(label='Conteúdo')
    author = forms.ModelChoiceField(queryset=User.objects.all())
    created_at = forms.DateField(label='Data de criação')
    image = forms.ImageField(label='Imagem')

    def save(self):
        data = self.cleaned_data
        news = News.objects.create(
            title=data['title'],
            content=data['content'],
            author=data['author'],
            created_at=data['created_at'],
            image=data['image'],
        )
        news.save()
