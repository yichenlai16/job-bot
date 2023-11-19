from .models import Jobs
import django_filters as filters

class CharInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class JobFilter(filters.FilterSet):
    search = filters.CharFilter(field_name='name',lookup_expr='icontains')
    area = filters.CharFilter(field_name='area',lookup_expr='icontains')
    cat = CharInFilter(field_name='category',lookup_expr='overlap')
    period = filters.CharFilter(field_name='workPeriod',lookup_expr='icontains')
    exp = filters.CharFilter(field_name='workExp',lookup_expr='iexact')
    class Meta:
        model= Jobs
        fields = ['name','area','cat','workPeriod','workExp']
