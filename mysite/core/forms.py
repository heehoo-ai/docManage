from django import forms

from .models import Doc


class DocForm(forms.ModelForm):
    # title = forms.CharField(
    #     label='标题',
    #     max_length=50,
    #     widget=forms.widgets.Input(
    #         attrs={'class': 'form-control', 'style': "width: 100%;"}
    #     )
    # )
    # category = forms.ChoiceField(
    #     label="分类",
    #     widget=forms.widgets.Select(
    #         attrs={'class': 'form-control', 'style': "width: 100%;"}
    #     )
    # )

    class Meta:
        model = Doc
        fields = ('title', 'category', 'pdf', )
