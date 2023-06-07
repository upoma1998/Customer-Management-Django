from django.forms import ModelMultipleChoiceField
import django_filters
from django_filters import DateFilter, CharFilter, NumberFilter
from .models import *


class OrderFilter (django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr="gte")
    end_date = DateFilter(field_name="date_created", lookup_expr="gte")
    note = CharFilter(field_name='note', lookup_expr='icontains')

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']


class ProductFilter(django_filters.FilterSet):
    name = CharFilter(field_name="name", lookup_expr='iexact')

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['category', 'description']
