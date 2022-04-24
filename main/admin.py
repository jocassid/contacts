
from django.contrib.admin import ModelAdmin, register
from main.models import Contact


@register(Contact)
class ContactAdmin(ModelAdmin):
    list_display = (
        'pk',
        'first_name',
        'last_name',
        'mobile',
        'email',
    )
