# cfb-predictor (WiP)

Written in php and python, this tool takes an input of two college football teams and attempts to "guess" the winner. 

Status
---
As of right now, the CFBPredictor's working parts include the dataset creator, and the php-python communication.

Running
---
You mainly just need PHP and python 3. You can run without installing apache, or any other web server by using php itself to run a server:

    php -S localhost:8000
    
Afterwards, just navigate to localhost:8000 in your browser to access the web interface.

Requirements
---
- PHP 5+
- python 3
