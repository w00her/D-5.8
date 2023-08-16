from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = [
            'author',
            'categoryType',
            'postCategory',
            'title',
            'text'
        ]

    # def clean(self):
    #     cleaned_data = super().clean()
    #     description = cleaned_data.get('description')
    #     if description is not None and len(description) < 20:
    #         raise ValidationError({
    #             'description': 'Описание не может быть меньше 20 символов'
    #         })
    #     return cleaned_data

    # def __init__(self, *args, **kwargs):
    #     super(PostForm, self).__init__(*args, **kwargs)
    #     self.initial['categoryType'] = "statya"
    #     self.initial['postCategory'] = "IT"
    #     self.initial['title'] = "Заголовок"
    #     self.initial['text'] = "Текст"
