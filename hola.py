import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
Builder.load_string(
                    
                        Button:
                        font-size:40
                        text:'Uno'
                        size_hint:0.1,0.1
                        pos_hint:{"x":0,'y':0}
                    )
class Flotante(FloatLayout):
    pass
class DemoApp(App):
    def build(self):
        return Flotante()
if __name__=='__main__':
    DemoApp.run()