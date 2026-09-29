from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import threading
import os
import speech_recognition as sr
from gtts import gTTS
import playsound

class EMAApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        self.label = Label(text="I am EMA, your AI Assistant", font_size=24)
        self.layout.add_widget(self.label)
        
        self.btn = Button(text="Tap to Speak", font_size=20, background_color=(0.1, 0.5, 0.8, 1))
        self.btn.bind(on_press=self.start_listening_thread)
        self.layout.add_widget(self.btn)
        
        return self.layout

    def speak(self, text):
        self.label.text = f"EMA: {text}"
        try:
            tts = gTTS(text=text, lang='en')
            tts.save("resp.mp3")
            playsound.playsound("resp.mp3")
            os.remove("resp.mp3")
        except Exception as e:
            print(e)

    def start_listening_thread(self, instance):
        threading.Thread(target=self.listen_command).start()

    def listen_command(self):
        self.label.text = "EMA is listening..."
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            try:
                audio = r.listen(source, timeout=5)
                query = r.recognize_google(audio, language='en-US').lower()
                self.label.text = f"You said: {query}"
                
                if 'hello' in query:
                    self.speak("Hello! How can I help you?")
                elif 'your name' in query:
                    self.speak("My name is EMA.")
                else:
                    self.speak(f"You said {query}")
            except:
                self.speak("Sorry, I could not understand.")

if __name__ == '__main__':
    EMAApp().run()
