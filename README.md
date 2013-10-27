TripLog
=======

Sublime Text plugin which automatically adds relative timestamp to every paragraph. 
An output file will be like this:
    
    Triplog: starting new trip at 28.10.2013 03:30
    Dose: a cup of green tee
    Age: 20 years
    Body weight: 65 kg
    
    
    T+0:00 A nice hot feeling in the stomach.
    
    T+0:00 First minute of example for TripLog.
    Press Enter two times to start a new paragraph.
    
    T+0:03 A certain will to go and code some cool stuff!
    
    T+0:06 Six minutes are already over.
    Look, you can have subsequent two lines in a file.
    
    T+0:22 But every two subsequent Enters will result in a new timestamp insertion.
    
    T+0:34 You can close this file and open it again.  Just run the launching command, 
    and the plugin will restore the start time from the first line.

Tested with Sublime Text 3.


How to install and use
======================

1. Copy `triplog.py` to `Packages/User` directory.
2. To create the trip log, open a new file, press ``Ctrl+` `` and run 
    `view.run_command("into_trip")`.
3. To return editing the trip file, open it and repeat the step 2.
