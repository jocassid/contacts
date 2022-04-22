
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class ListView(TemplateView):

    template_name = 'main/list.html'

    def get_context_data(self):
        """The Web 2.0/REST way would be to load a page with an empty table
        and then have the JavaScript perform a request to get a list of
        Contacts"""

        return {
            # replace this list of dicts with a queryset of
            'contacts': [
                {
                    'pk': 1000000,
                    'first_name': 'aaron',
                    'last_name': 'aaronson',
                    'mobile_phone': '614-555-0001',
                    'email': 'aaaa@example.com'
                },
                {
                    'pk': 1000001,
                    'first_name': 'betty',
                    'last_name': 'bailey',
                    'mobile_phone': '614-555-0001',
                    'email': 'betty.bailey@example.com',
                },
            ]
        }


class ContactRestView(View):
    """Django REST framework is better for this sort of thing."""

    def post(self, request, *args, **kwargs):
        """create a new Contact"""
        return JsonResponse({}, status=201)

    def put(self, request, *args, **kwargs):
        """Update a Contact"""
        return JsonResponse({}, status=200)
