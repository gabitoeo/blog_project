from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from post import views as post_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='post/login.html'), name='login'),
    path('', auth_views.LoginView.as_view(template_name='post/login.html'), name='login'),  # Página principal es login
    path('register/', post_views.register, name='register'),
    path('posts/', include('post.urls')),  # Las URLs de los posteos van aquí
    path('logout/', auth_views.LogoutView.as_view(template_name='post/login.html'), name='logout'),
]
