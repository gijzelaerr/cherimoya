FROM stackbrew/ubuntu:saucy
MAINTAINER gijs@pythonic.nl

# basic system bootstrap
RUN echo "deb http://nl.archive.ubuntu.com/ubuntu/ saucy main universe multiverse\ndeb http://nl.archive.ubuntu.com/ubuntu/ saucy-updates main universe multiverse\ndeb http://security.ubuntu.com/ubuntu saucy-security main universe multiverse" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get -y upgrade

# install dependencies
RUN apt-get -y install graphite-carbon graphite-web libapache2-mod-wsgi apache2 supervisor

# replace the graphite django password with something random
RUN sed -i "s/^[#]*SECRET_KEY = .*$/SECRET_KEY = '$(< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c${1:-32})'/g" /etc/graphite/local_settings.py

# bootstrap graphite
ADD docker/carbon.conf /etc/carbon/carbon.conf
RUN graphite-manage syncdb --noinput
RUN chown _graphite:_graphite /var/lib/graphite/graphite.db

# install cherimoya
ADD . /cherimoya
RUN cd cherimoya; python ./setup.py install
#ENTRYPOINT ["/usr/local/bin/aartfaac-translator"]
EXPOSE 2003

# configure apache
ADD docker/apache.conf /etc/apache2/sites-available/cherimoya.conf
RUN a2dissite 000-default
RUN a2ensite cherimoya
EXPOSE 80

# configure supervisor
ADD docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/supervisord"]
