# Oil-Tank-Meter
Measures and logs home heating oil level.

Uses an ultrasonic range sensor to measure tank fuel level and logs to a database. 

Planned Features:
- Log to a database
- Have web GUI to plot level over time
- Evaluate trend
- Evaluate projected runout date
- Alarm feature

Initial Setup
Enable ssh through raspi-config
Through locale setting, set time zone

sudo apt-get install
git
sqlite3

sqlite> BEGIN;
sqlite> CREATE TABLE level (timestamp DATETIME, level NUMERIC);
sqlite> COMMIT;


Sensor interface code from:
https://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi

Test notes:
inital measure of tank level 22.3 inches. 

old gague measures 120-130 gal prior to removal, 130-140 gal after reinstall

275 gal tank capacity.  Height 44 inches. 

44 - 22.3 = 21.5 inch from bottom

21.5 inch from bottom is 129-136 gal. Accurate to guage level to nearest 10 gal.





