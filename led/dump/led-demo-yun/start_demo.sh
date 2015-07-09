#!/bin/ash

source .bashrc
cd /mnt/sda1/arduino/cohorte/demos/led-arduino-yun
python $COHORTE_HOME/bin/scripts/cohorte-start-node.py -c --base `pwd`
cd -

