
from json import loads, JSONDecodeError

from django.core.exceptions import ObjectDoesNotExist
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

        return {
            'contacts': Contact.objects.all()
        }


class ContactRestView(View):
    """Django REST framework is better for this sort of thing."""

    ERROR_INVALID_JSON = 1
    ERROR_PK_ALREADY_SET = 2
    ERROR_MISSING_INVALID_PK = 3

    FIELDS_AND_LABELS = {
        'first_name': 'First Name',
        'last_name': 'Last Name',
        'mobile': 'Mobile Phone',
        'email': 'Email',
    }

    @staticmethod
    def generic_error_message(error_code):
        return f"Invalid request.  Error code {error_code}"

    @staticmethod
    def error_response(errors, status=400):
        """
        param errors:  A list of strings
        """
        return JsonResponse(
            {'errors': errors},
            status=status,
        )

    def validate_contact_json(self, contact_json):
        errors = []
        contact_kwargs = {}
        for field, label in self.FIELDS_AND_LABELS.items():
            value = contact_json.get(field)
            if value:
                if isinstance(value, str):
                    contact_kwargs[field] = value
                else:
                    errors.append(f"{value!r} is not a string")
            else:
                errors.append(f"Missing {label}")
        return errors, contact_kwargs


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

        errors, contact_kwargs = self.validate_contact_json(contact_json)
        if errors:
            return self.error_response(errors)

        contact = Contact.objects.create(**contact_kwargs)
        contact_json['pk'] = contact.pk
        return JsonResponse(contact_json, status=201)


class ContactUpdateRestView(ContactRestView):
    """Django REST framework is better for this sort of thing."""

    def put(self, request, *args, **kwargs):
        try:
            contact_json = loads(request.body)
        except JSONDecodeError:
            return self.error_response(
                [self.generic_error_message(self.ERROR_INVALID_JSON)],
            )

        try:
            pk = int(contact_json['pk'])
            if pk < 1:
                raise ValueError('pk must be greater than 0')
        except (KeyError, TypeError, ValueError):
            return self.error_response(
                [self.generic_error_message(self.ERROR_MISSING_INVALID_PK)]
            )

        errors, contact_kwargs = self.validate_contact_json(contact_json)
        if errors:
            return self.error_response(errors)

        try:
            contact = Contact.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return self.error_response(
                ['Contact not found'],
                status=404,
            )

        for field in self.FIELDS_AND_LABELS.keys():
            setattr(contact, field, contact_json.get(field))
        contact.save()

        return JsonResponse(contact_json, status=200)
