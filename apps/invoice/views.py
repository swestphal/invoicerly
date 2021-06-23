from rest_framework import viewsets
from .serializers import InvoiceSerializer
from .models import Invoice, Item

from django.core.exceptions import PermissionDenied


class InvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        team = self.request.user.team.first()
        serializer.save(created_by=self.request.user, team=team)

    def perform_update(self, serializer):
        obj = self.get_object()

        if self.request.user != obj.created_by:
            raise PermissionDenied('Wrong object owner')

        serializer.save()