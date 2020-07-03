from .models import MovieList
import django_filters

class MovieFilter(django_filters.FilterSet):
    class Meta:
        model = MovieList
        fields = {
            'title': ['icontains']
        }
