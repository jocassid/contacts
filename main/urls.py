
from django.urls import path

from main.views import ListView

urlpatterns = [
    path('list/', ListView.as_view(), name='list_contacts'),
    path('', ListView.as_view(), name='home'),
]
