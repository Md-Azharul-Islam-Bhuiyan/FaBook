from django import forms
from .models import News, NewsCategory

class NewsCategoryForm(forms.ModelForm):
    class Meta:
        model = NewsCategory
        fields = '__all__'


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ['posted_user']
    
        labels = {
                'image':'🖼'
            }

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs['class'] = 'img-label'