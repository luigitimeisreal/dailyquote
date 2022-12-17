from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from generate_quote import generate_quote
from kivy.lang import Builder

class QuoteApp(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
QuoteApp().run()