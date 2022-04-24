
from django.urls import path

from main.views import \
    ContactNewRestView, \
    ContactUpdateRestView, \
    ListView

urlpatterns = [
    path('list/', ListView.as_view(), name='list_contacts'),
    path('contacts/', ContactNewRestView.as_view(), name='new_contact'),
    path('contacts/<pk>/', ContactUpdateRestView.as_view(),  name='update_contacts'),
    path('', ListView.as_view(), name='home'),
]
