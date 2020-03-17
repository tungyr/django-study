from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_first_simple_view),
    path('power', views.my_second_simple_view),
    path('post/<int:post_id>/', views.my_third_simple_view, name='123_view'),
]