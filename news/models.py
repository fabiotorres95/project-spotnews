from django.db import models
from django.core.exceptions import ValidationError


def validate_title(value):
    if ' ' in value:
        return value
    else:
        raise ValidationError(
            ('O título deve conter pelo menos 2 palavras.'),
            params={'value': value},
        )


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    role = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(
        max_length=200,
        error_messages={'title': ['este campo não pode estar vazio']},
        validators=[validate_title]
    )
    content = models.TextField(
        error_messages={'content': ['este campo não pode estar vazio']}
    )
    author = models.ForeignKey(User, max_length=200, on_delete=models.CASCADE)
    created_at = models.DateField()
    image = models.ImageField(blank=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
