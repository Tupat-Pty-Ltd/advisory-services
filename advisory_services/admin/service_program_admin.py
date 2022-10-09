from django.contrib import admin

from ..forms import ServiceProgrameForm
from ..models import ServicePrograme


@admin.register(ServicePrograme, site=wallet_merchant_integration_admin)
class ServiceProgrameAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = CustomerForm

    search_fields = ['merchant_name', 'MSISDN', 'identity', 'first_name', 'last_name']

    fieldsets = (
        (None, {
            'fields': (
                'merchant_name',
                'first_name',
                'last_name',
                'identity',
                'MSISDN')},
         ),
        audit_fieldset_tuple
    )

    list_display = (
        'merchant_name', 'first_name', 'last_name', 'identity', 'MSISDN')