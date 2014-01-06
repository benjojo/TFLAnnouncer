TFLAnnouncer
============

A program that will announce when the next train to work is


This is designed to work on a raspberrypi!

You will need `sox` and `aplay` to make this work, to install them run

`sudo apt-get install sox aplay`

Then install it as a crontab similar to

`41,44,47,50,53,56,59	7	*	*	1,2,3,4,5	python /root/TFLAnnouncer/run.sh`
