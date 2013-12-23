FROM stackbrew/ubuntu:saucy
RUN echo "deb http://nl.archive.ubuntu.com/ubuntu/ saucy main universe multiverse\ndeb http://nl.archive.ubuntu.com/ubuntu/ saucy-updates main universe multiverse\ndeb http://security.ubuntu.com/ubuntu saucy-security main universe multiverse" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install graphite-carbon graphite-web libapache2-mod-wsgi
RUN echo "CARBON_CACHE_ENABLED=true\n" > /etc/default/graphite-carbon
RUN service carbon-cache start
RUN graphite-manage syncdb
RUN chown _graphite:_graphite /var/lib/graphite/graphite.db
RUN cp /usr/share/graphite-web/apache2-graphite.conf /etc/apache2/sites-available/graphite-web.conf
RUN a2ensite graphite-web
RUN /etc/init.d/apache2 restart
