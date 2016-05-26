Services
=============

Dev    : 1.0.0
Master : 1.0.0

This folder contains the services of each node of the application demo-led.

1. Instructions for the .services files :
------------------------------------------
There are four .services files : One for the camera Raspberry, one for the Piface, one for the cloud machine and one for the docker machine, using the systemd
functionnality.

In order to make these four nodes boot automatically on the system boot you have
to put the .service file in the /etc/systemd/system/ folder of the Rasperry
or the machine filesystem.
Next, you need to enable the service at the boot. You can do that by typing the
next command in the terminal :

```
sudo systemctl enable <name of the .service file>.
Ex: sudo systemctl enable led-raspberry-piface-uno.service
```

2. Instructions for led-raspberry-gpio :
----------------------------------------
This is the old way to run a program at startup with init.d.
You have to copy the entire file and then execute these commands :

```
sudo cp <your file> /etc/init.d/
sudo chmod +x /etc/init.d/<your file>
sudo update-rc.d <your file> defaults
```

3. Instructions for led-arduino-yun_rc.local file :
---------------------------------------------------
This file is to launch programs at startup on the Arduino YUN.
You have to rename this file 'rc.local' and put it into '/etc/' folder.
If you have made any changes in this file before, copy/paste the difference.
