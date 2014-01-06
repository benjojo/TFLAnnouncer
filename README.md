TFLAnnouncer
============

A program that will announce when the next train to work is


This is designed to work on a raspberrypi!

You will need `sox` and `aplay` to make this work, to install them run

`sudo apt-get install sox aplay`

Then install it as a crontab similar to

`30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59	7	*	*	1,2,3,4,5	python /root/TFLAnnouncer/run.sh`

For a more Rainbow experiance please switch to `RainbowDashBranch`