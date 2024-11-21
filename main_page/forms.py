from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 50}))

    class Meta:
        model = Comment
        fields = ['text', 'rate']
        labels = {'text': 'Комментарий',
                  'rate': 'Оценка'}