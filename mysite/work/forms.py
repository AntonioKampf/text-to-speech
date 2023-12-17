from django import forms


class TextToSpeechForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, initial="The title of the painting, which is known in English as Mona Lisa, is based")
    rate = forms.IntegerField(max_value=200, min_value=1, initial=125, required=True)
    volume = forms.FloatField(min_value=0, max_value=1, initial=0.8, required=True)
    dictor = forms.ChoiceField(
        choices=[
            ('Male', 'Male 1'),
            ("Voice 1", "Female 1"), 
            ('Voice 4', 'Female 4'),
        ]
    )
