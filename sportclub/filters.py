from sportclub.models import SportClubModel
import django_filters


class SportClubFilter(django_filters.FilterSet):
    sportclub_name = django_filters.CharFilter(field_name='sportclub_name', lookup_expr='icontains')
    region = django_filters.CharFilter(field_name='region', lookup_expr='icontains')

    class Meta:
        model = SportClubModel
        fields = ['user']
