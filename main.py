# Samundar-AI / Ocean Safety App - main.py

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.clearcolor = (0.02, 0.12, 0.25, 1)

class SamundarAIApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        title = Label(text='Samundar-AI', font_size=38, bold=True, color=(0, 0.8, 1, 1), size_hint_y=0.3)
        subtitle = Label(text='Ocean Safety & Fisherman Help App', font_size=18, size_hint_y=0.2)
        
        btn1 = Button(text='1. Mausam Ki Jankari - Weather', size_hint_y=0.15, background_color=(0, 0.5, 0.9, 1))
        btn2 = Button(text='2. Safe Location - GPS', size_hint_y=0.15, background_color=(0, 0.7, 0.5, 1))
        btn3 = Button(text='3. AI Madad - Fish Finder', size_hint_y=0.15, background_color=(0.9, 0.4, 0.1, 1))
        btn4 = Button(text='4. Emergency SOS', size_hint_y=0.15, background_color=(0.9, 0.1, 0.1, 1))

        layout.add_widget(title)
        layout.add_widget(subtitle)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        return layout

if __name__ == '__main__':
    SamundarAIApp().run()
