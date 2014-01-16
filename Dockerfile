FROM stackbrew/ubuntu:saucy
RUN echo "deb http://nl.archive.ubuntu.com/ubuntu/ saucy main universe multiverse\ndeb http://nl.archive.ubuntu.com/ubuntu/ saucy-updates main universe multiverse\ndeb http://security.ubuntu.com/ubuntu saucy-security main universe multiverse" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install graphite-carbon graphite-web libapache2-mod-wsgi apache2 curl
RUN echo "CARBON_CACHE_ENABLED=true\n" > /etc/default/graphite-carbon
RUN service carbon-cache start

# replace the graphite django password with something random
RUN sed -i "s/^[#]*SECRET_KEY = .*$/SECRET_KEY = '$(< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c${1:-32})'/g" /etc/graphite/local_settings.py
RUN graphite-manage syncdb --noinput
RUN chown _graphite:_graphite /var/lib/graphite/graphite.db

RUN curl -L https://github.com/gijzelaerr/cherimoya/archive/master.tar.gz -o master.tar.gz
RUN tar zxvf master.tar.gz
RUN cd cherimoya-master; python ./setup.py install

RUN a2dissite 000-default
RUN curl -L https://raw2.github.com/gijzelaerr/cherimoya/master/apache.conf -o /etc/apache2/sites-available/cherimoya.conf
RUN a2ensite cherimoya
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_PID_FILE /var/run/apache2/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
# Only /var/log/apache2 is handled by /etc/logrotate
ENTRYPOINT ["/usr/sbin/apache2"]
CMD ["-D", "FOREGROUND"]
EXPOSE 80
