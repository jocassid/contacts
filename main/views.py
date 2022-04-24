from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .models import *


class ListView(TemplateView):

    template_name = 'main/list.html'

    def get_context_data(self):
        """The Web 2.0/REST way would be to load a page with an empty table
        and then have the JavaScript perform a request to get a list of
        Contacts"""

        contacts = Contact.objects.__dict__
        return contacts


class ContactRestView(View):
    """Django REST framework is better for this sort of thing."""

    def post(self, request, *args, **kwargs):
        """create a new Contact"""
        return JsonResponse({}, status=201)

    def put(self, request, *args, **kwargs):
        """Update a Contact"""
        return JsonResponse({}, status=200)
