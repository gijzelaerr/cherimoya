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

$ sudo docker build -t cherimoya .
$ sudo docker run -p 80:80 -p 2003:2003 -t -i cherimoya
$ cat data/SB002-data.dat | netcat -l 9999
$ cherimoya/bin/aartfaac-translator
$ brower http://localhost/cherimoya/


credits
-------

 * John Swinbank
 * Folkert Huizinga
 * Peeyush Prasad
 * Gijs Molenaar

