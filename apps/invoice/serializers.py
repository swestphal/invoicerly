from rest_framework import serializers

from .models import Invoice, Item


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        read_only_fields = (
            'team',
            'created_at',
            'created_by',
            'modified_at',
            'modified_by'
        ),
        fields = (
            "id",
            "client",
            "client_name",
            "client_email",
            "client_org_number",
            "client_address1",
            "client_address2",
            "client_zipcode",
            "client_place",
            "client_country",
            "client_contact_person",
            "client_contact_reference",
            "sender_reference",
            "invoice_type",
            "due_days",
            "is_sent",
            "gross_amount",
            "vat_amount",
            "net_amount",
            "discount_amount",
        )
