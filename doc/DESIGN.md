Graphite
--------

The core of the design is graphite. Graphite is a log collecting and aggregation
tool. It is really flexible and perfect for collect time series (only). You can
easily add new metrics by just sending them to graphite in the correct format.
It also has very flexible retention configuration.

http://graphite.readthedocs.org/en/latest/


Installation
------------

I wrote some ubuntu instructions about how to set it up here:

https://github.com/gijzelaerr/cherimoya/doc

 it is not 100% tested, and may not work for your setup.


Log translation
---------------

I wrote an AARTFAAC monitoring format to Graphite log format converter, which
will connect to the AARTFAAC imager and the graphite log collector and pass the
message between these two ports:

 https://github.com/gijzelaerr/cherimoya/blob/master/cherimoya/graphite.py

stuff should configured in setup.py. Cherimoya doesn't have any dependencies
on 3rd party libraries so you should be able to run in on any system.



Accessing the data
------------------

When Graphite is set up and you are dumping logging into it, you can access the
data through the included webserver that you configured in the steps above. It
includes a GUI for building graphs which is a bit clunky, you can also do it
manually using the API:

 http://graphite.readthedocs.org/en/latest/render_api.html

Note that you can also use JSON format outputting, that can be used in for
example highcarts to build dynamic charts. Also this can be a single time stap,
which we can use for plotting complex numbers in a 2d plane.


The web frontend
----------------

My plan is to build a set of static HTML/javascript files containing a set of
these graphs represting the data that peeyush described in his logging document.
This is what i'm currently working on and is located here:

 https://github.com/gijzelaerr/cherimoya/tree/master/static

For now it will be a single page, which has a range selector (start and end
date) and all the graphs which will automagically update given the start and
end range.


Overview
--------

As you can see this is also in the Cherimoya tree. Cherimoya is now:

 * an AARTFAAC log to Graphite log translator
 * an AARTFAAC log simulator
 * a set of html and javascript which can be used as a frontend for the Graphite
   web API.


Docker
------

This is all a bit hard to setup, so if I have time left I want to make a docker
or vagrant file for the project. If that is finished setting up the enviroment
would be as simple as:

 * Install docker or vagrant
 * run docker up or vagrant up in the project folder
 * configure Cherimoya (set AARTFAAC imaging log port)
 * run cherimoya in docker/vagrant
 * point your browser to port 8080
 * profit.
