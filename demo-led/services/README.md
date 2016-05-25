services
=============

Dev    : 1.0.0
Master : 1.0.0

This folder contains the services of each node of the application demo-led.

1) Instructions for the .services files :
There is two .services files, there are for two Raspberry Pi using the systemd
functionnality.
One file for the camera Raspberry and one for the Piface one.

In order to make these two nodes boot automatically on the system boot you have
to put the .service file in the /etc/systemd/system/ folder of the Rasperry
filesystem.
Next, you need to enable the service at the boot. You can do that by typing the
next command in the terminal : sudo systemctl enable [name of the .service file].

Example : sudo systemctl enable led-raspberry-piface-uno.service

2) Instructions for led-raspberry-gpio :


3) Instructions for .local file :
