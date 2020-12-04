from django import forms
from .models import Post, Category


#choices = [('coding', 'coding'),('sports', 'sports'),('entertainment', 'entertainment')]
choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'title_intro', 'category', 'title_tag', 'author', 'quote', 'body', 'header_image', 'video_file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'' , 'id':'elder', 'type':'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            #'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'title_intro':forms.TextInput(attrs={'class':'form-control'}),
            'quote':forms.Textarea(attrs={'class':'form-control'}),
            }


class CatForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }



class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_intro', 'quote', 'body', 'header_image', 'video_file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'title_intro':forms.TextInput(attrs={'class':'form-control'}),
            'quote':forms.Textarea(attrs={'class':'form-control'}),
            #'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            }
