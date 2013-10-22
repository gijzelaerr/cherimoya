cherimoya
=========

A monitor for the [AARTFAAC imaging pipeline](https://github.com/aartfaac/imaging),
part of the [AARTFAAC project](http://www.aartfaac.org/).

[![Build Status](https://travis-ci.org/gijzelaerr/cherimoya.png)](https://travis-ci.org/gijzelaerr/cherimoya)

Documentation
-------------

[source for the technical design document](https://github.com/aartfaac/docs/tree/master/reports/imaging/monitoring).


Usage
------------

Install the required python modules:

```Shell
$ pip install -r requirements.txt
$ python setup.py install
```

Configure your AARTFAAC imaging pipeline nodes in *cherimoya/settings.py*.

Now start the log collector:
```Shell
$ python ./manage.py aartfaacclient
```

You can also start a fake log server:
```Shell
$ python ./manage.py aartfaacserver
```

Now configure your favorite webserver to start serving this Django project!
If you do don't know how to do that you should read the [Django deployment
documentation](https://docs.djangoproject.com/en/1.5/howto/deployment/). If
you just want to have a quick lock you can run a Django development server:

```Shell
$ python ./manage.py runserver
```

and point your browser to [](http://127.0.0.1:8000/)

testing
-------

to test cherimoya:

```Shell
$ pip install -r requirements_dev.txt
$ nosetests
```

credits
-------

 * John Swinbank
 * Folkert Huizinga
 * Peeyush Prasad
 * Gijs Molenaar

