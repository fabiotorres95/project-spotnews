from django.shortcuts import render
from news.models import News


def index(request):
    news_data = News.objects.all()
    news_list = []
    for data in news_data:
        news_list.append(
            {
                "title": data.title,
                "content": data.content,
                "author": data.author,
                "created_at": data.created_at,
                "image": data.image,
                "categories": data.categories,
            }
        )

    data = {
        "news_list": news_list,
    }

    return render(request, 'home.html', data)
