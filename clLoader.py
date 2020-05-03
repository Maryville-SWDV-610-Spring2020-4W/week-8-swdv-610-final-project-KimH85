import itertools
import threading
import time
import sys

class Loader:

    def __init__(self):
        self.done = False
        self.t = None

    #shows a spinner
    def animatedLoader(self):
        
        #each loop positions the line in a different angle to make appearance
        #line is spinning
        #for c in itertools.cycle(['|', '/', '-', '\\']):
        for c in itertools.cycle(["    ",".   ", "..       ", "...      ", "....     ", ".....    ","......   ",".......  ","........ ","........."]):
            #this stops the spinner
            if self.done:
                break
            
            #shows the spinner
            sys.stdout.write('\r\rI am thinking ' + c)
            sys.stdout.flush() #resets the console
            time.sleep(0.1) #time between loops
        
        
    def start(self):
        self.t = threading.Thread(target=self.animatedLoader)
        self.t.start()
        
    def stop(self):
        self.done = True

