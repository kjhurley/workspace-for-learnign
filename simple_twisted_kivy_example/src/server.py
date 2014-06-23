# install_twisted_rector must be called before importing  and using the reactor
from kivy.support import install_twisted_reactor
install_twisted_reactor()


from twisted.internet import reactor
from twisted.internet import protocol


class MyServer:
    def __init__(self):
        self.counter=0
        self.msg=""
        self.state="started"
        
    def handle_message(self, msg, gui=None):
        if self.state == "started":
            self.state = "communicating"
        if msg  == "ping":
            self.msg =  "pong"
        elif msg == "plop":
            self.msg = "kivy rocks"
        elif msg == "start":
            self.state = "counting"
        elif msg == "stop":
            self.state = "communicating"
        elif msg == "pause":
            self.pause(gui)
        elif msg == "play":
            self.play(gui)
        else:
            self.msg=msg

        if self.state == "counting":
            self.counter+=1
            
        if gui is not None:
            gui.label.text=self.current_message()

        return self.msg

    def current_message(self):
        return "[%d] %s - %s"%(self.counter, self.state, self.msg)

    def tick(self, gui=None):
        self.counter+=1
        if gui is not None:
            gui.label.text=self.current_message()

    def pause(self, gui):
        gui.suspend_clock()

    def play(self, gui):
        gui.resume_clock()
        

class EchoProtocol(protocol.Protocol):
    def dataReceived(self, data):
        response = self.factory.app.handle_message(data, self.factory.gui)
        if response:
            self.transport.write(response)

class EchoFactory(protocol.Factory):
    protocol = EchoProtocol
    def __init__(self, app, gui):
        self.app = app
        self.gui = gui


from kivy.app import App
from kivy.uix.label import Label
import kivy.clock
import twisted.internet.task

class TwistedServerApp(App):
    def build_gui(self):
        self.label = Label(text="server started\n")
        
    def connect_backend(self):
        self.server=MyServer()
        self.loop=twisted.internet.task.LoopingCall(self.tick)
        self.playing=True
        self.loop.start(1.0)
        reactor.listenTCP(8000, EchoFactory(self.server, self))
        
    def build(self):
        self.build_gui()
        self.connect_backend()
        
        return self.label

    def tick(self):
        self.server.tick(self)


    def suspend_clock(self):
        if self.playing:
            self.loop.stop()
            self.playing=False
        
    def resume_clock(self):
        if not self.playing:
            self.loop.start(1)
            self.playing=True
            

if __name__ == '__main__':
    TwistedServerApp().run()
