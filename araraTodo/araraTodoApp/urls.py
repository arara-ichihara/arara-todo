from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/delete/', views.delete, name='delete'),  # ←削除機能用
]