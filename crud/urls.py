from django.urls import path
from .views import (TodoPageViev, TodoEditView, TodoListView, TodoCreateView, TodoDeleteView, TodoDetailView)

urlpatterns = [
    path('', TodoPageViev.as_view(), name='home'),
    path('create/', TodoCreateView.as_view(), name='create'),
    path('todo/', TodoListView.as_view(), name='todo'),
    path('<int:pk>/', TodoDetailView.as_view(), name='detail'),
    path('<int:pk>/delete/', TodoDeleteView.as_view(), name='delete'),
    path('<int:pk>/update/', TodoEditView.as_view(), name='update'),
]
