cherimoya
=========

A monitor service for the
[AARTFAAC imaging pipeline](https://github.com/aartfaac/imaging),
part of the [AARTFAAC project](http://www.aartfaac.org/). It translates the
AARTFAAC imaging log output to [Graphite](http://graphite.readthedocs.org/)
events, which can plot this in pretty graphs.

[![Build Status](https://travis-ci.org/gijzelaerr/cherimoya.png)](https://travis-ci.org/gijzelaerr/cherimoya)

Documentation
-------------

[source for the technical design document](https://github.com/aartfaac/docs/tree/master/reports/imaging/monitoring).

Installation
------------

Please see doc/INSTALL.md

Usage
-----

 $ sudo docker build -t gijzelaerr/cherimoya .

or

 $ docker pull  gijzelaerr/cherimoya

now run the docker instance

 $ sudo docker run -p 80:80 -p 2003:2003 -t -i gijzelaerr/cherimoya

You can run a fake server to test if everything is working

 $ cat data/SB002-data.dat | netcat -l 9999

Now start the translator

 $ cherimoya/bin/aartfaac-translator

and point your browser to http://localhost/cherimoya/ .


credits
-------

 * John Swinbank
 * Folkert Huizinga
 * Peeyush Prasad
 * Gijs Molenaar

