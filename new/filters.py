import django_filters
from .models import News

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = News
        fields = '__all__'
        exclude = ['content','img','publish_at','slug']