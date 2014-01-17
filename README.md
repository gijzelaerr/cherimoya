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


Example usage (using docker)
----------------------------


```Shell
$ sudo docker build -t gijzelaerr/cherimoya .
```

or

```Shell
$ docker pull  gijzelaerr/cherimoya
```

now run the docker instance

```Shell
$ sudo docker run -p 80:80 -p 2003:2003 -t -i gijzelaerr/cherimoya
```

This will forward port 80 and 2003 to your local system. Please change (read
the doc) if you already have a service running there. You can run a fake server
to test if everything is working:

```Shell
$ cat data/SB002-data.dat | netcat -l 9999
````

Now start the translator

```Shell
$ cherimoya/bin/aartfaac-translator
```

and point your browser to http://localhost/cherimoya/ .
you can also run the aartfaac-translator from the docker container itself, but
since there are no 3rd party requirements for running it this is probably
easier. Run the translator with -h to see the options (hostname, port).

```Shell
$ cherimoya/bin/aartfaac-translator
```

