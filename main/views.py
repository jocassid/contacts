from django.shortcuts import render
from django.views.generic import TemplateView


class ListView(TemplateView):

    template_name = 'main/list.html'

    def get_context_data(self):
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
