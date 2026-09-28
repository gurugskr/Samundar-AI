# Bulldozer Spec App - main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.15, 0.13, 0.08, 1) # Bulldozer yellow-black theme

class BulldozerSpecApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)

        title = Label(text='BULLDOZER SPEC', font_size=32, bold=True, color=(1, 0.8, 0.2, 1), size_hint_y=0.2)
        
        specs = [
            "Model: CAT D6 / BEML BD155",
            "Engine: 215 HP @ 1900 RPM",
            "Operating Weight: 22,000 kg",
            "Blade Type: Semi-U / Straight",
            "Blade Capacity: 5.7 Cu.m",
            "Ground Pressure: 0.64 kg/cm2",
            "Fuel Tank: 400 L",
            "Transmission: Powershift 3F/3R"
        ]

        layout.add_widget(title)
        
        for s in specs:
            lbl = Label(text=s, font_size=16, halign='left', size_hint_y=0.1, color=(1,1,1,1))
            layout.add_widget(lbl)

        btn = Button(text='Download Full Spec PDF (Free)', background_color=(1, 0.6, 0, 1), size_hint_y=0.15)
        layout.add_widget(btn)

        return layout

if __name__ == '__main__':
    BulldozerSpecApp().run()
