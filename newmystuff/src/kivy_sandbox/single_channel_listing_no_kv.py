from kivy.app import App
from kivy.uix.button import Button
import kivy.uix.label 
import kivy.uix.gridlayout
import kivy.uix.boxlayout

"""
top line - channel icon in top left, current time in top right
under that a box containing 
    date and time of current program hard left against the margin. time since start/time left hard agaist the right margin
    a paragrap of description of the show
under that a grid containing on each row:
    the time the program starts, the title of the program, start of the description (cut off at the right edge)
under that a bottom line containing
    4 buttons - +1 day, -1 day, << page up, >> page down
    
    
the box with current program description should match the program line selected in the grid layout
a popup can be opened to show more extensive program info.
clicking on the selected program will start viewing it
alternative click to record it (right mouse button or something)

 
"""

def generate_show_details_label(shows, show_id):
    """ format the show details to appear in the details box
    
    Whichever show is currently selected, a box with details is displayed near the
    top of the app showing details of that show incuding start time, name of the programme,
    a detailed description of the show etc
    
    """
    print shows[show_id]
    return "{starttime:<4}: {name: >40}\n{details}".format(**shows[show_id])

def select_show_event(obj):
    """ when a show is selected, update the details box """
    new_text=generate_show_details_label(obj.parent.parent.shows,obj.show_id)
    print new_text
    obj.parent.parent.show_details_label.text=new_text


class SingleChannelGuideApp(App):
    def build(self):
        
        listing=[("0900","First show","The first show in the morning"),
                 ("0930","Second show","Something else to watch"),
                 ("1030","Movie 1","Best film of all time"),
                 ("1300","News at lunch","Did you miss it this yesterday?"),
                 ("1400","Movie 2","A real tear-jerker"),
                 ("1700","Train reks","For the kids")]
        
        outer_layout=kivy.uix.boxlayout.BoxLayout(orientation='vertical')
        selected_program_box=kivy.uix.gridlayout.GridLayout(rows=2)
        channel_box=kivy.uix.anchorlayout.AnchorLayout(anchor_x='left',anchor_y='top')
        channel_box.add_widget(kivy.uix.label.Label(text="BBC One"))
        selected_program_box.add_widget(channel_box)
        
        outer_layout.create_property("shows")  
        outer_layout.shows={}
        [outer_layout.shows.update({show_id:{'name':entry[1],'starttime':entry[0],'details':entry[2]}}) for show_id,entry in enumerate(listing)]
         
        outer_layout.create_property("show_details_label")
        outer_layout.show_details_label=kivy.uix.label.Label(text=generate_show_details_label(outer_layout.shows,0),size_hint=(1.0,0.2))
        
        outer_layout.add_widget(outer_layout.show_details_label)
        
        middle_layout=kivy.uix.gridlayout.GridLayout(cols=1,row_force_default=True, row_default_height=40)
        for i,l in enumerate(listing):
            b=Button(text="%4s   %s"%(l[0],l[1]))
            b.bind(on_press=select_show_event)
            b.create_property("show_id")
            b.show_id=i
            middle_layout.add_widget(b)
            
        outer_layout.add_widget(middle_layout)
        return outer_layout
    
if __name__ == '__main__':
    SingleChannelGuideApp().run()