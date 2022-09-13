from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

KV = """
MyBL:
    Label:
        font_size: "30sp"
        text: root.data_label
"""

class MyBL(BoxLayout):
    data_label = StringProperty("Треугольник!")
    
class MyApp(App):
    running = True
    def build(self):
        return Builder.load_string(KV)
        
MyApp().run()