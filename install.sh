#!/bin/bash

mkdir -p /usr/lib/cgi-bin/
cp *.py /usr/lib/cgi-bin/.
#cp fuellog.db /var/www/.
chmod 777 /usr/lib/cgi-bin/*
chmod 777 /usr/lib/cgi-bin
chown www-data:www-data /usr/lib/cgi-bin/*
chown www-data:www-data /usr/lib/cgi-bin
