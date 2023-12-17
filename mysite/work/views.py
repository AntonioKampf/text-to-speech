from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from mysite import settings
from work.forms import TextToSpeechForm
from utils.Text import TextToSpeech


tts = TextToSpeech()


class TextToSpeechView(View):
    template_name = 'work/text_speech.html'

    def get(self, request):
        form = TextToSpeechForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = TextToSpeechForm(request.POST)

        if form.is_valid():
            text = form.cleaned_data['text']
            rate = form.cleaned_data['rate']
            volume = form.cleaned_data['volume']
            dictor = form.cleaned_data['dictor']

            text_to_speech = TextToSpeech()
            text_to_speech.set_engine_properties(rate, volume, dictor)
            text_to_speech.engine.say(text)
            text_to_speech.engine.runAndWait()

        return render(request, self.template_name, {'form': form})


class AudioView(TemplateView):
    template_name = 'work/work_result.html'
    extra_context = {'audio': settings.MEDIA_URL + 'audio.mp3'}
