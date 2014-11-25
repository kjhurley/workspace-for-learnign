'''
Created on 10 Jun 2014

@author: khurley
'''
from kivy.app import App
from kivy.uix.button import Button
import kivy.uix.image

class ShowImage(kivy.uix.image.Image):
    pass

class TestApp(App):
    def build(self):
        if False:
            return ShowImage(source="rango.jpg",pos=(0,0),size=(256,256))
        else:
            return Button(text='Hello World')
    
if __name__ == '__main__':
    TestApp().run()