triplog
=======

Sublime Text plugin which automatically adds relative timestamp to every paragraph. 
An output file will be like this:
    
    Triplog: starting new trip at 03.07.2013 19:03

    00:00
    First minute of example for TripLog.
    Press Enter two times to start a new paragraph.

    00:06
    Six minutes are already over.
    Look, you can have subsequent two lines in a file.

    00:22
    But every two subsequent Enters will result in a new timestamp insertion.
    
    00:34
    You can close this file and open it again: just run the launching command, 
    and the plugin will restore the start time from the first line.

Tested with Sublime Text 3.


How to install and use
======================

1. Copy `triplog.py` to `Packages/User` directory.
2. To create or resume trip session in some file, press ``Ctrl+` ``, then type 
    `view.run_command("into_trip")`
