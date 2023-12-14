from django import forms

class TextToSpeechForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, initial='Mono Liza')
    rate = forms.IntegerField(max_value=200, min_value=1, initial=125, required=True)
    volume = forms.FloatField(min_value=0, max_value=1, initial=0.8, required=True)
    dictor = ('male', 'Мужчина')
