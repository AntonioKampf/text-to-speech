import pyttsx3


class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.name_voices = {'female': None, 'male': None}

    def set_engine_properties(self, rate, volume, voice):
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)

        if voice == 'male':
            self.engine.setProperty('voice', self.name_voices.get('male'))
        elif voice == 'female':
            self.engine.setProperty('voice', self.name_voices.get('female'))
        else:
            print("No voice")
