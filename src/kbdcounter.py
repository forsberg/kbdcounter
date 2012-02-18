#!/usr/bin/env python

import os
import time
from datetime import datetime, timedelta
import csv
from xlib import XEvents



class KbdCounter(object):
    def __init__(self):
        self.storepath=os.path.expanduser("~/.kbdcounter.csv")

        self.set_thishour()
        self.set_nextsave()
        self.read_existing()

    def set_thishour(self):
        self.thishour = datetime.now().replace(minute=0, second=0, microsecond=0)
        self.nexthour = self.thishour + timedelta(hours=1)
        self.thishour_count = 0

    def set_nextsave(self):
        now = time.time()
        self.nextsave = now + min((self.nexthour - datetime.now()).seconds+1, 300)        

    def read_existing(self):

        if os.path.exists(self.storepath):
            thishour_repr = self.thishour.strftime("%Y-%m-%dT%H")
            for (hour, value) in csv.reader(open(self.storepath)):
                if hour == thishour_repr:
                    self.thishour_count = int(value)
                    break
        

    def save(self):
        tmpout = csv.writer(open("%s.tmp" % self.storepath, 'w'))
        thishour_repr = self.thishour.strftime("%Y-%m-%dT%H")        

        if os.path.exists(self.storepath):
            for (hour, value) in csv.reader(open(self.storepath)):
                if hour != thishour_repr:
                    tmpout.writerow([hour, value])

        tmpout.writerow([thishour_repr, self.thishour_count])
        os.rename("%s.tmp" % self.storepath, self.storepath)

    def run(self):
        events = XEvents()
        events.start()
        while not events.listening():
            time.sleep(1)
            print "Waiting for initializationg"

        print "Listening for events"

        try:
            while events.listening():
                evt = events.next_event()
                if not evt:
                    time.sleep(0.5)
                    continue
                
                if evt.type != "EV_KEY" or evt.value != 1: # Only count key down, not up.
                    continue
            
                self.thishour_count+=1
            
                if time.time() > self.nextsave:
                    self.save()
            
                    if datetime.now().hour != self.thishour.hour:
                        self.set_thishour()
            
        except KeyboardInterrupt:
            events.stop_listening()
            self.save()

            
                    

if __name__ == "__main__":
    kc = KbdCounter()
    kc.run()

    

    

    
    
    
