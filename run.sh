#!/bin/bash
cd /root/TFLAnnouncer/
mkdir tmp
mount -t ramfs none /root/TFLAnnouncer/tmp
python reader.py