#!/bin/bash

mkdir -p /usr/lib/cgi-bin/
cp monitor.py /usr/lib/cgi-bin/.
cp webgui.py /usr/lib/cgi-bin/.
cp fuellog.db /usr/lib/cgi-bin/.
chmod +x /usr/lib/cgi-bin/monitor.py
chmod +x /usr/lib/cgi-bin/fuellog.db
chmod +x /usr/lib/cgi-bin/webgui.py
chown www-data:www-data /usr/lib/cgi-bin/monitor.py
chown www-data:www-data /usr/lib/cgi-bin/fuellog.db
chown www-data:www-data /usr/lib/cgi-bin/webgui.py
