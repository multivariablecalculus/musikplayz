from django import forms
from django.core.exceptions import ValidationError
from .models import Song, Request

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist', 'file']

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file  and not file.name.endswith('.mp3'):
            raise ValidationError("Only MP3 files are allowed.")
        return file

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['username', 'request_text']
