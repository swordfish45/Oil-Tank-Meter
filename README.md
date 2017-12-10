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

