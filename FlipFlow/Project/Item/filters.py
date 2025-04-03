import django_filters
from .models import Item

class ItemFilter(django_filters.FilterSet):
    # Search filter for item name (case-insensitive)
    name = django_filters.CharFilter(field_name='Item_name', lookup_expr='icontains', label='Search by name')

    # Filter by price range (min_price, max_price)
    min_price = django_filters.NumberFilter(field_name='Item_price', lookup_expr='gte', label='Min Price')
    max_price = django_filters.NumberFilter(field_name='Item_price', lookup_expr='lte', label='Max Price')


    # Sort by item price
    price_sort = django_filters.ChoiceFilter(
        choices=[('asc', 'Price: Low to High'), ('desc', 'Price: High to Low')],
        method='filter_by_price',
        label='Sort by Price'
    )

    # Custom method for sorting
    def filter_by_price(self, queryset, name, value):
        if value == 'asc':
            return queryset.order_by('Item_price')
        elif value == 'desc':
            return queryset.order_by('-Item_price')
        return queryset

    class Meta:
        model = Item
        fields = ['name', 'min_price', 'max_price', 'price_sort']
