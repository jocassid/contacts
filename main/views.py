
from json import loads, JSONDecodeError
from random import randint

from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

from main.models import *


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

    ERROR_INVALID_JSON = 1
    ERROR_PK_ALREADY_SET = 2

    FIELDS_AND_LABELS = {
        'first_name': 'First Name',
        'last_name': 'Last Name',
        'mobile_phone': 'Mobile Phone',
        'email': 'Email',
    }

    @staticmethod
    def generic_error_message(error_code):
        return f"Invalid request.  Error code {error_code}"

    @staticmethod
    def error_response(errors):
        """
        param errors:  A list of strings
        """
        return JsonResponse(
            {'errors': errors},
            status=400,
        )

    def validate_contact_json(self, contact_json):
        errors = []
        for field, label in self.FIELDS_AND_LABELS.items():
            value = contact_json.get(field)
            if value:
                if not isinstance(value, str):
                    errors.append(f"{value!r} is not a string")
            else:
                errors.append(f"Missing {label}")
        return errors


class ContactNewRestView(ContactRestView):

    def post(self, request, *args, **kwargs):
        try:
            contact_json = loads(request.body)
        except JSONDecodeError:
            return self.error_response(
                [self.generic_error_message(self.ERROR_INVALID_JSON)],
            )

        if contact_json.get('pk'):
            return self.error_response(
                [self.generic_error_message(self.ERROR_PK_ALREADY_SET)],
            )

        errors = self.validate_contact_json(contact_json)
        if errors:
            return self.error_response(errors)

        # Create Contact record

        # update contact_json with pk of new record.  For now I'm just using
        # a random number
        contact_json['pk'] = randint(1, 999999)

        return JsonResponse(contact_json, status=201)


class ContactUpdateRestView(ContactRestView):
    """Django REST framework is better for this sort of thing."""

    def put(self, request, *args, **kwargs):
        """Update a Contact"""
        return JsonResponse({}, status=200)
