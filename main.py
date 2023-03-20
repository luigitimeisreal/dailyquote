from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from generate_quote import generate_quote
from kivy.lang import Builder

from kivy.clock import Clock
from kivy.properties import StringProperty
import time
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager

from functools import partial
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
import os
from kivymd.uix.boxlayout import MDBoxLayout
class SavedQuoteContent(MDBoxLayout):
    '''Custom content'''

class Main(MDScreenManager):
    #properties can get updated
    current_time = StringProperty("")
    def __init__(self):
        super(Main, self).__init__()
        #this object calls every 1 second the update function
        self.time_obj = Clock.schedule_interval(self.update_time,1)
    
#dt stands for delta time, and %H, %M, %S for hour, minute and second
    def update_time(self, dt):
        self.current_time = time.strftime("%H"+":"+"%M"+":"+"%S")

class QuoteApp(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Brown"
        self.theme_cls.primary_hue = "200"
        return Main()
    def add_new_widget(self):
        self.root.ids.box.add_widget(
            MDExpansionPanel(
                icon= "star",
                content=SavedQuoteContent(),
                panel_cls=MDExpansionPanelThreeLine(
                    text="Text",
                    secondary_text="Secondary text",
                    tertiary_text="Tertiary text",
                    )))
QuoteApp().run()