from django.urls import path

from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('post/<int:pk>', views.get_post_view, name='post'),
    path('create', views.create_post_view, name='create'),
    path('post/edit/<int:pk>', views.post_edit_view, name='edit'),
]
