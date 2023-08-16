

from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    # path — означает путь.
    # В данном случае путь ко всем товарам у нас останется пустым.
    # Т.к. наше объявленное представление является классом,
    # а Django ожидает функцию, нам надо представить этот класс в виде view.
    # Для этого вызываем метод as_view.
    path('', PostView.as_view(), name="list_of_news"),
    # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    # int — указывает на то, что принимаются только целочисленные значения
    path('<int:pk>', PostDetailView.as_view(), name='one_news'),
    # path('pages/', include('django.contrib.flatpages.urls')),
    path('search/', PostSearchView.as_view()),
    path('create/', PostCreate.as_view(), name='news_create'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit_view'),
    # path('search/<int:pk>/edit/', views.post_edit, name='post_edit_view'),
    path('<int:pk>/delete/', views.PostDelete, name='delete_view'),
    path('search/<int:pk>/delete/', views.PostDelete, name='delete_search_view'),

]
