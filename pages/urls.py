from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.base_index, name='base_index'),
    path('blog', views.base_posts, name='base_posts'),
    path('test', views.base_test, name='base_test'),
    path('about', views.base_about, name='base_about'),
    path('blog/post/<int:pk>/', views.base_post, name='base_post'),
    path('blog/post/add', views.base_post_add, name='base_post_add'),
    path('blog/post/<int:pk>/edit/', views.base_post_edit, name='base_post_edit'),
    path('blog/post/(<int:pk>/comment/', views.base_comment, name='base_comment'),
    path('accounts/register', views.base_auth_reg, name='base_auth_reg'),
    path('', include('social_django.urls', namespace='social')),

]
