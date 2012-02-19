kdbcounter - a program for counting keyboard activity
-----------------------------------------------------

This program will count the number of keypresses you make on your
keyboard and mouse, on any X Window System environment, for example
Linux. 

The results, divided by hour, are stored in a commaseparated file, by
default ~/.kbdcounter.csv. For hours where there's no activity, no
line is added to the file. 

Installation
------------

Run bootstrap, then buildout. This will retrieve the dependencies of
the project (python-xlib), or use an existing one if you have it
installed already (i.e. via *apt-get install python-xlib*) and
generate the binary.

::

   python bootstrap.py
   bin/buildout

Run *bin/kbdcounter*. After 5 minutes, verify that it's working by
inspecting ~/.kbdcounter.csv.

The program should be started automatically when your desktop session
is started. 

Is this a silly program?
------------------------

Yes. I wrote it because I was curious on how many keystrokes I was
making on a regular working day.

Known bugs
----------

* The program will not save the last 5 minutes of stats if it's
  killed. Killing it with Ctrl-C will however save state.

   



