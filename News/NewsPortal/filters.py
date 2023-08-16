from django_filters import FilterSet, ModelChoiceFilter, ModelMultipleChoiceFilter, DateFilter
from .models import Post, Category
from django.forms import DateTimeInput
import datetime


class PostFilter(FilterSet):
    categoryType = ModelMultipleChoiceFilter(
        field_name="postCategory",
        queryset=Category.objects.all(),
        label='Category',
        conjoined=True,
        # to_field_name='categoryType',
    )

    class Meta:
        model = Post
        fields = {
            # 'author': ['exact'],
            'categoryType': ['exact'],
            # 'dateCreation': ['gte'],
            'title': ['icontains'],
            # 'text': ['icontains'],
        }

    datePost = DateFilter(
        field_name='dateCreation',
        lookup_expr='gte',
        label='Later then',
        widget=DateTimeInput(
            attrs={
                'type': 'date',
                'value': (datetime.date.today())
            },

        ),
    )
