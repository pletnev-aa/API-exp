import django_filters
from django_filters import rest_framework as filters
from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Billing
from .serializers import BillingSerializer, UploadSerializer


class BillingInfoFilter(django_filters.FilterSet):
    customer = django_filters.CharFilter(
        field_name='customer__name', lookup_expr='iexact'
    )
    company = django_filters.CharFilter(
        field_name='company__name', lookup_expr='iexact'
    )

    class Meta:
        model = Billing
        fields = [
            'customer', 'company'
        ]


class BillingViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BillingInfoFilter


class UploadFile(mixins.CreateModelMixin, GenericViewSet):

    serializer_class = UploadSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
        except Exception as e:
            return Response(
                {'error': f'File error: {str(e)}'},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            {'message': 'File download and processing completed successfully'},
            status=status.HTTP_200_OK
        )
