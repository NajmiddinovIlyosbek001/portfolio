from django import forms
from blog.models import Post, Category

class PostForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(
            queryset=Category.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            required=True)
    class Meta:
        model = Post
        fields = ['title', 'category', 'file', 'body']