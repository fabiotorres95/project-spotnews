from django.urls import path
from news.views import index, details, categories, news_view


urlpatterns = [
    path("", index, name="home-page"),
    path("news/<int:id>", details, name="news-details-page"),
    path("categories", categories, name="categories-form"),
    path("news", news_view, name="news-form")
]
