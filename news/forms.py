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
    content = forms.CharField(label='Conteúdo', widget=forms.Textarea)
    author = forms.ModelChoiceField(
        label="Autoria",
        queryset=User.objects.all())
    created_at = forms.DateField(
        label='Criado em',
        widget=forms.DateInput(attrs={'type': 'date'}))
    image = forms.ImageField(label='URL da Imagem')

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
