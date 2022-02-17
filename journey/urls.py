from django.contrib.auth import views as auth_views
from django.urls import path, include
from journey import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'journey'

urlpatterns = [
        path('', views.post_list, name='post_list'),
        path('post_list', views.post_list, name='post_list'),
        path('signup', views.signup, name='signup'),
        path('post_detail', views.post_detail, name='post_detail'),
        path('post/create/', views.post_new, name='post_new'),
        path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
        path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
        path('comment_list', views.comment_list, name='comment_list'),
        path('comment/<int:pk>/edit/', views.comment_edit, name='comment_edit'),
        path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
        path('travelblog_post/<int:post_id>', views.travelblog_post, name='travelblog_post'),
]
