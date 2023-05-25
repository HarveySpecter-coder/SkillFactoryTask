from django import forms
from .models import Article, Category
from django.core.exceptions import ValidationError

class ArticleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control py-4'}), required=True)
    text = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'style':'resize:none'}), required=True)
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'class':'custom-select'}))
    video = forms.FileField(widget=forms.FileInput(attrs={'class':'custom-file-input'}), required=False)


    # code = forms.IntegerField(widget=forms.NumberInput(attrs={
    #     'class':'secret_code_input',
    #     'type':'number',
    #     'id':'secret_code_input',
    #     'autofocus':'True',
    #     'inputmode':'numeric',
    #     'placeholder':'----'}),
    #     error_messages={'invalid':'Вы ввели неверный код'})

    class Meta:
        model = Article
        fields = ['title', 'text', 'category', 'image', 'video']

    # def clean_code(self):
    #     user_entered_code = self.cleaned_data['code']
    #     if user_entered_code != self.initial['secret_code']:
    #         raise ValidationError('Вы ввели неверный код')
    #     return

