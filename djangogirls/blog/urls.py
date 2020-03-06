from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('post/<int:pk>/', views.post_detail, name='post_detail')
]