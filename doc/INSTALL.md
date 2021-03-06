Manual installation instruction
===============================

for if you don't use docker.

preperations - setting up graphite
----------------------------------

If are using Debian/Ubuntu you prefab packages:

```Shell
$ sudo apt-get install graphite-carbon graphite-web libapache2-mod-wsgi
$ sudo sh -c "echo 'CARBON_CACHE_ENABLED=true\n' > /etc/default/graphite-carbon"
$ sudo service carbon-cache start
$ sudo graphite-manage syncdb
$ sudo chown _graphite:_graphite /var/lib/graphite/graphite.db
$ sudo cp /usr/share/graphite-web/apache2-graphite.conf /etc/apache2/sites-available/graphite-web.conf
$ sudo a2ensite graphite-web
$ sudo /etc/init.d/apache2 restart
````

You can edit your data retention policy in `/etc/carbon/storage-schemas.conf`.
For AARTFAAC storing 1 hour with 1 second resolution takes up about 520MB
(50KB/metric/second). For more info read the doc in
`/usr/share/doc/graphite-web/README.Debian`.

Alternatively you can install Graphite [manually](http://graphite.readthedocs.org/).

cherimoya
---------

```Shell
$ sudo python setup.py install
```

See the aartfaac-translator help for more information.
```Shell
$ /usr/local/bin/aartfaac-translator -h
```

server static content
---------------------

Configure your apache webserver to serve to content of the static folder.
You can use docker/apache.conf as an example.