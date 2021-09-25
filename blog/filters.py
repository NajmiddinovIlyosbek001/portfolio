from accounts.models import CustomUser
import django_filters
from blog.models import Post, Category
from django import forms

class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='contains', label='')
    category = django_filters.ModelMultipleChoiceFilter(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
    )
    class Meta:
        model = Post
        fields = ['title', 'category']
class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(field_name='username', lookup_expr='contains', label='')
    class Meta:
        model = CustomUser
        fields = ['username']