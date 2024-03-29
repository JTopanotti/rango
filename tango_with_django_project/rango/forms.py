from django import forms
from .models import Page, Category, UserProfile
from django.contrib.auth.models import User


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=Category.char_length,
                           help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=Category.default_integer)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=Category.default_integer)
    slug = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name', 'views',)


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=Page.char_length,
                            help_text="Plase enter the title of the page.")
    url = forms.URLField(max_length=Page.url_length,
                         help_text="Plase enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=Page.default_integer)

    class Meta:
        model = Page
        exclude = ('category',)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

            return cleaned_data


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    website = forms.URLField(required=False)
    picture = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        exclude = ('user',)