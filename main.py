# Samundar-AI / Ocean Safety App - main.py
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.clearcolor = (0.02, 0.12, 0.25, 1)

class SamundarAIApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        title = Label(text='Samundar-AI', font_size=32, bold=True, size_hint=(1, 0.2))
        subtitle = Label(text='Ocean Safety & Fish Finder', font_size=18, size_hint=(1, 0.15))
        
        btn1 = Button(text='1. Mausam Ki Jankari', size_hint=(1, 0.15))
        btn2 = Button(text='2. Safe Location - GPS', size_hint=(1, 0.15))
        btn3 = Button(text='3. AI Madad - Fish Finder', size_hint=(1, 0.15))
        btn4 = Button(text='4. Emergency SOS', size_hint=(1, 0.15), background_color=(1, 0.2, 0.2, 1))

        layout.add_widget(title)
        layout.add_widget(subtitle)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        return layout

if __name__ == '__main__':
    SamundarAIApp().run()
