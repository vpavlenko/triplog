triplog
=======

Sublime Text plugin which automatically adds relative timestamp to every paragraph. 
An output file will be like this:
    
    Triplog: starting new trip at 03.07.2013 19:03

    00:00
    Start writing an example for TripLog

    00:06
    Six minutes are already over.
    Look, you can have subsequent two lines in a file.

    00:22
    But every two subsequent Enters will result in a new timestamp insertion.

Tested with Sublime Text 3.

How to install and use
======================

1. Copy `triplog.py` to `Packages/User directory`.
2. To create or resume trip session in some file, press ``Ctrl+` ``, then type 
    `view.run_command("into_trip")`
