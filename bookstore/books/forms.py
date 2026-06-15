from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'rate']  # views is auto-tracked, not user input
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'rate': forms.NumberInput(attrs={'min': 0, 'max': 5, 'step': 0.1}),
        }