from django.shortcuts import render, redirect
from news.models import News, Category
from news.forms import CategoriesForm, NewsForm


def index(request):
    news_data = News.objects.all()
    news_list = []
    for data in news_data:
        parts = str(data.created_at).split('-')
        converted = f"{parts[2]}/{parts[1]}/{parts[0]}"
        news_list.append(
            {
                "title": data.title,
                "content": data.content,
                "author": data.author,
                "created_at": converted,
                "image": data.image,
                "categories": data.categories,
            }
        )

    data = {
        "news_list": news_list,
    }

    return render(request, 'home.html', data)


def details(request, id):
    news_data = News.objects.get(id=id)
    parts = str(news_data.created_at).split('-')
    converted = f"{parts[2]}/{parts[1]}/{parts[0]}"

    news = {
        "title": news_data.title,
        "content": news_data.content,
        "author": news_data.author,
        "created_at": converted,
        "image": news_data.image,
        "categories": news_data.categories
    }

    return render(request, 'news_details.html', news)


def categories(request):
    form = CategoriesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home-page')
    return render(request, 'categories_form.html', {'form': form})


def news_view(request):
    form = NewsForm()
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home-page')

    categories = Category.objects.all()
    data = {
        'form': form,
        'categories': categories,
    }
    return render(request, 'news_form.html', data)
