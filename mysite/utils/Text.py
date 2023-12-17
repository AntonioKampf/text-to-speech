import pyttsx3


class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.name_voices = {'female': None, 'male': None}

    def set_engine_properties(self, rate, volume, voice):
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)

        print(voice)
        male_voice = self.name_voices.get('male')
        
        if voice == "Voice 1":
            self.engine.setProperty('voice', 'english+f1')
        elif voice == "Voice 4":
            self.engine.setProperty('voice', 'english+f4')
        elif voice == "Male":
            self.engine.setProperty('voice', male_voice)
        else:
            print("No voice")
