# Oil-Tank-Meter
Measures and logs home heating oil level.

Uses an ultrasonic range sensor to measure tank fuel level and logs to a database. 

Current Featureds
- Log to a database
- Have web GUI to plot level over time

Planned Features:
- Evaluate trend
- Evaluate projected runout date
- Alarm feature

Initial Setup
- Enable ssh through raspi-config
- Through locale setting, set time zone


- sudo apt-get install
- git
- sqlite3
- sudo apt-get install apache2 ; sudo a2enmod cgid


- sqlite> BEGIN;
- sqlite> CREATE TABLE level (timestamp DATETIME, level NUMERIC);
- sqlite> COMMIT;

- crontab -e (not www-data user)
- 0 * * * * /usr/lib/cgi-bin/monitor.py >> /usr/lib/cgi-bin/log.txt 2>&1

Sensor interface code from:
https://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi

Test notes:
inital measure of tank level 22.3 inches. 

old gauge measures 120-130 gal prior to removal, 130-140 gal after reinstall

275 gal tank capacity.  Height 44 inches. 

44 - 22.3 = 21.5 inch from bottom

21.5 inch from bottom is 129-136 gal. Accurate to guage level to nearest 10 gal.

12/23/17
- installed
- gauge level 120-130 gal
- reading 18.4 inch from bottom ~110 gal

12/28/17
- monitor level 17.17 inch ~ est 103.5gal . Charted ~101 gal
- actual level measured with tape ~15 inch. Charted ~86 gal

webgui and monitor from:
https://github.com/Pyplate/rpi_temp_logger/


