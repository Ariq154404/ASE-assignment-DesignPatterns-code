class WindowInterface(object):
    def build(self):
        pass
    
class AbstractWindowDecorator(WindowInterface):
    def __init__(self, window):
        self._window = window
    
    def build(self): 
        pass

class Window(WindowInterface):
    def build(self):
        print('Building window')
        
class BorderDecorator(AbstractWindowDecorator):
    def add_border(self):
        print('Adding border')
        
    def build(self):
        self.add_border()
        self._window.build()

class GlassDecorator(AbstractWindowDecorator):
    def add_glass(self):
        print('Adding glass to the window.')
    
    def build(self):
        self.add_glass()
        self._window.build()
        

if __name__ == '__main__':
    w = Window()
    wb = BorderDecorator(w)
    wb.build()
    print("Will build windows with only border")
    wg = GlassDecorator(w)
    wg = BorderDecorator(wg)
    wg.build()
    print("Will build windows with border and glass")