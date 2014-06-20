from kivy.app import App
from kivy.uix.button import Button
import kivy.uix.label 
import kivy.uix.gridlayout
import kivy.uix.relativelayout

class TestApp(App):
    def build(self):
        listing=[("0900","First show","The first show in the morning"),
                 ("0930","Second show","Something else to watch"),
                 ("1030","Movie 1","Best film of all time"),
                 ("1300","News at lunch","Did you miss it this yesterday?")]
        outer_layout=kivy.uix.relativelayout.RelativeLayout()
        middle_layout=kivy.uix.gridlayout.GridLayout(cols=2,row_force_default=True, row_default_height=40)
        for l in listing:
            middle_layout.add_widget(Button(text=l[0],size_hint_x=None))
            middle_layout.add_widget(Button(text=l[1]))
        outer_layout.add_widget(middle_layout)
        outer_layout.add_widget(kivy.uix.label.Label(text="0900: First show.\nThe first show in the morning"))
        return outer_layout
    
if __name__ == '__main__':
    TestApp().run()