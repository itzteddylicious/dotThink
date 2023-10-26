from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('', views.diary_list, name='diary_list'),
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path('create/', views.create_diary_entry, name='create_diary_entry'),
    path('edit/<int:pk>/', views.edit_diary_entry, name='edit_diary_entry'),
    path('delete/<int:pk>/', views.delete_diary_entry, name='delete_diary_entry'),
    path("favorites/", views.favorite_list, name="favorite_list"),
    path("fav/<int:pk>/", views.favorite_add, name="favorite_add"),
]