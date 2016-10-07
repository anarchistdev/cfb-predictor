# cfb-predictor (WiP)

Written in php and python, this tool takes an input of two college football teams and attempts to "guess" the winner. NOTE, that the rankings on the site often take a day or so to update, so running the tool right after a game will give outdated statistics.

Note that the tool was written for semi-accurate simulations, and was not written to be used for gambling purposes.

Status
---
Keep in mind that the simulator at this stage is very crude, and the results are often skewed and inaccurate. The game simulation is run approx. 1,000 times and the average scores for each team are taken into the final result.

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
