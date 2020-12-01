from django import forms
from .models import Post


#choices = [('coding', 'coding'),('sports', 'sports'),('entertainment', 'entertainment')]




class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'title_intro', 'title_tag', 'author', 'quote', 'body', 'header_image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'' , 'id':'elder', 'type':'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            #'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'title_intro':forms.TextInput(attrs={'class':'form-control'}),
            'quote':forms.Textarea(attrs={'class':'form-control'}),
            }




class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_intro', 'quote', 'body', 'header_image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'title_intro':forms.TextInput(attrs={'class':'form-control'}),
            'quote':forms.Textarea(attrs={'class':'form-control'}),
            #'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            }
