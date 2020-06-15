from django import forms

from .models import Doc, Category


class DocForm(forms.ModelForm):
    # title = forms.CharField(
    #     label='标题',
    #     max_length=50,
    #     widget=forms.widgets.Input(
    #         attrs={'class': 'form-control', 'style': "width: 100%;", 'placeholder': "选填"}
    #     )
    # )

    # category = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Doc
        fields = ('title', 'category', 'file', )
