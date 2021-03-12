from django import forms
containers = [
        ("Container 1","Container 1"),
        ("Container 2","Container 2"),
        ("Container 3","Container 3"),
    ]
class MonFormulaire(forms.Form):
    nom             = forms.CharField(label='Nom de l image', max_length=100)
    email           = forms.CharField(label='Nom de l image', max_length=100)
    nom_image       = forms.CharField(label='Nom de l image', max_length=100)
    git_url         = forms.CharField(label='Nom de l image', max_length=1500)
    comment         = forms.CharField(label='Commentaire', widget=forms.Textarea)
    username        = forms.CharField(label='username', max_length=150)
    password        = forms.CharField(label='password', max_length=200)