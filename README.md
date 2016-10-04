# cfb-predictor (WiP)

Written in php and python, this tool takes an input of two college football teams and attempts to "guess" the winner. NOTE, that the rankings on the site often take a day or so to update, so running the tool right after a game will give outdated statistics.

Status
---
As of right now, the working parts include the dataset creator, and the php-python communication.

Running
---
The first thing you must do is create a directory called `sets` in the root folder:

    mkdir sets

You can run the predictor without installing apache, or any other web server by using php itself to run a server:

    php -S localhost:8000
    
Afterwards, just navigate to localhost:8000 in your browser to access the web interface.

Requirements
---
- PHP 5+
- python 
