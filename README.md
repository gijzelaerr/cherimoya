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

preperations - setting up graphite
----------------------------------

If are using Debian/Ubuntu you prefab packages:

```Shell
$ sudo apt-get install graphite-carbon graphite-web
$ less /usr/share/doc/graphite-web/README.Debian
````

Alternativly you can install Graphite [manually](http://graphite.readthedocs.org/).

Usage
-----

Install the required python modules:

```Shell
$ pip install -r requirements.txt
```

Now configure your cherimoya:
```Shell
$ cp cherimoya/settings_example.py cherimoya/settings.py
$ editor cherimoya/settings.py
```

If you don't have a AARTFAAC imaging pipeline, you can start a emulator:
```Shell
$ python cherimoya/emulator.py
```

To start translating AARTFAAC monitoring events to Graphite events run:
```Shell
$ python cherimoya/graphite.py
```

and then point your browser to your graphite instance.


credits
-------

 * John Swinbank
 * Folkert Huizinga
 * Peeyush Prasad
 * Gijs Molenaar

