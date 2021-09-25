from django.urls import path
from blog import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('new-post/', views.PostCreate, name='new_post'),
    path('post-delete/<int:pk>', views.PostDelete, name='delete'),
    path('post/<slug:slug>/<int:year>/<int:month>/<int:day>/<int:hour>/<int:minut>/<int:second>/', views.PostDetail, name='detail'),
    path('user/<slug:username>/', views.profile, name='profile'),
    path('users/', views.users, name='users'),
]