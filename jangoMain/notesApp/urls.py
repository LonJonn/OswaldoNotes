from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notes', views.notes, name='notes'),
    path('note/<int:pk>', views.noteInfo, name='noteInfo'),
]