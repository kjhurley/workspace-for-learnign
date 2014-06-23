#install_twisted_rector must be called before importing the reactor
from kivy.support import install_twisted_reactor
install_twisted_reactor()


#A simple Client that send messages to the echo server
from twisted.internet import reactor, protocol

class EchoClient(protocol.Protocol):
    def connectionMade(self):
        self.factory.app.on_connection(self.transport)

    def dataReceived(self, data):
        self.factory.app.print_message(data)

class EchoFactory(protocol.ClientFactory):
    protocol = EchoClient
    def __init__(self, app):
        self.app = app

    def clientConnectionLost(self, conn, reason):
        self.app.print_message("connection lost")

    def clientConnectionFailed(self, conn, reason):
        self.app.print_message("connection failed")


def connect_gui_and_client(gui):
    reactor.connectTCP('localhost', 8000, EchoFactory(gui))
    

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

# A simple kivy App, with a textbox to enter messages, and
# a large label to display all the messages received from
# the server
class TwistedClientApp(App):
    connection = None

    def build(self):
        root = self.setup_gui()
        connect_gui_and_client(self)
        return root

    def setup_gui(self):
        self.textbox = TextInput(size_hint_y=.1, multiline=False)
        self.textbox.bind(on_text_validate=self.send_message)
        self.label = Label(text='connecting...\n')
        self.layout = GridLayout(cols=1,orientation='vertical', size_hint_y=1)
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.textbox)
        bottom_row=GridLayout(cols=4, row_force_default=True, row_default_height=40)
        self.start_button = Button(text='start')
        self.start_button.bind(on_press=self.start_timer)
        self.stop_button = Button(text='stop')
        self.stop_button.bind(on_press=self.stop_timer)
        self.play_button = Button(text='>')
        self.play_button.bind(on_press=self.play)
        self.pause_button = Button(text='||')
        self.play_button.bind(on_press=self.pause)
        bottom_row.add_widget(self.start_button)
        bottom_row.add_widget(self.stop_button)
        bottom_row.add_widget(self.play_button)
        bottom_row.add_widget(self.pause_button)
        self.layout.add_widget(bottom_row)
        return self.layout

    def on_connection(self, connection):
        self.print_message("connected succesfully!")
        self.connection = connection

    def send_message(self, *args):
        msg = self.textbox.text
        if msg and self.connection:
            self.connection.write(str(self.textbox.text))
            self.textbox.text = ""

    def start_timer(self, *args):
        self.connection.write("start")
        
    def stop_timer(self, *args):
        self.connection.write("stop")
        
    def play(self, *args):
        self.connection.write("play")
        
    def pause(self, *args):
        self.connection.write("pause")
        
    def print_message(self, msg):
        self.label.text += msg + "\n"


if __name__ == '__main__':
    TwistedClientApp().run()
