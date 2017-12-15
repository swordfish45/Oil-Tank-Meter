#!/bin/bash

mkdir -p /usr/lib/cgi-bin/
cp *.py /usr/lib/cgi-bin/.
cp fuellog.db /var/www/.
chmod +x /usr/lib/cgi-bin/*.py
chmod +x /var/www/fuellog.db
chown www-data:www-data /usr/lib/cgi-bin/*.py
chown www-data:www-data /var/www/fuellog.db
