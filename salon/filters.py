from salon.models import SalonModel
import django_filters


class SalonFilter(django_filters.FilterSet):
    is_futsall = django_filters.BooleanFilter(field_name='is_futsall')
    uncategorized = django_filters.BooleanFilter(field_name='is_futsall', lookup_expr='isnull')
    area__gte = django_filters.NumberFilter(field_name='area', lookup_expr='gte')
    area__lte = django_filters.NumberFilter(field_name='area', lookup_expr='lte')
    company_discount_percentage__gte = django_filters.NumberFilter(field_name='company_discount_percentage', lookup_expr='gte')
    company_discount_percentage__lte = django_filters.NumberFilter(field_name='company_discount_percentage', lookup_expr='lte')

    class Meta:
        model = SalonModel
        fields = ['is_football','is_volleyball','is_futsall','is_basketball','is_handball','is_confirmed']
