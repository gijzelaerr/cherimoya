cherimoya
=========

A monitor for the [AARTFAAC imaging pipeline](https://github.com/aartfaac/imaging),
part of the [AARTFAAC project](http://www.aartfaac.org/).

[![Build Status](https://travis-ci.org/gijzelaerr/cherimoya.png)](https://travis-ci.org/gijzelaerr/cherimoya)

Documentation
-------------

[source for the technical design document](https://github.com/aartfaac/docs/tree/master/reports/imaging/monitoring).


Usage
-----

Install the required python modules:

```Shell
$ pip install -r requirements.txt
```

Configure your AARTFAAC imaging pipeline nodes in *cherimoya/settings.cfg*.

Now start the log collector:
```Shell
$ python cherimoya/client.py
```

You can also start a fake log emulator:
```Shell
$ python cherimoya/emulator.py
```

Now configure your favorite webserver to start serving this Flask project!
If you just want to have a quick lock you can run a Flask development server
from the cherimoya project folder:

```Shell
$ python cherimoya
```

and point your browser to [](http://127.0.0.1:5000/)

testing
-------

to test cherimoya:

```Shell
$ ./cherimoya_test.py
```

credits
-------

 * John Swinbank
 * Folkert Huizinga
 * Peeyush Prasad
 * Gijs Molenaar

