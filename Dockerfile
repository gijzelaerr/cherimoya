FROM stackbrew/ubuntu:saucy
RUN echo "deb http://nl.archive.ubuntu.com/ubuntu/ saucy main universe multiverse\ndeb http://nl.archive.ubuntu.com/ubuntu/ saucy-updates main universe multiverse\ndeb http://security.ubuntu.com/ubuntu saucy-security main universe multiverse" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install graphite-carbon graphite-web libapache2-mod-wsgi apache2
RUN echo "CARBON_CACHE_ENABLED=true\n" > /etc/default/graphite-carbon
RUN service carbon-cache start

# replace the graphite django password with something random
RUN sed -i "s/^[#]*SECRET_KEY = .*$/SECRET_KEY = '$(< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c${1:-32})'/g" /etc/graphite/local_settings.py
RUN graphite-manage syncdb --noinput
RUN chown _graphite:_graphite /var/lib/graphite/graphite.db
RUN cp /usr/share/graphite-web/apache2-graphite.conf /etc/apache2/sites-available/graphite-web.conf
RUN a2ensite graphite-web

#RUN /etc/init.d/apache2 restart
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENTRYPOINT ["/usr/sbin/apache2"]
CMD ["-D", "FOREGROUND"]
EXPOSE 80 8088
