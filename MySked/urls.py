from django.urls import path
from . import views

urlpatterns = [
    path('', views.showvideo, name='showvideo'),
    path('success', views.success, name='success'),
    path('calendar', views.CalendarView.as_view(), name='calendar'),
    path('<str:path>add', views.add, name='add'),
]