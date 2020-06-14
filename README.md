# CarControllerReciever
This is one half of my project to have a PC/Mobile controlled RC Car. Pairs with the [Controller](https://github.com/AkasshShah/CarController).

## Overview and Purpose
This project tackles the mundane RC Cars problems. I always loved RC cars but sometimes hated the controls. I would love to have a sidewars RC controller instead of a wheel-style RC controller. I also want to be able to control my car with a computer (desktop, laptop, tablet (Android) or phone (Android)). To do this, this project uses a Raspberry Pi to control the electronics of the car and to recieve signals from the client (computer) that will act as a client. It makes use of TCP socket programming.
## Requirements
This projects requires that you have a Raspberry Pi and its OS installed and ready to go. This project also requires a RC car that is going to be modded. The car's front steering system needs to be controlled by a 3 pin servo and not a 5 pin servo. If there is a 5 pin servo in your car, swap it out for a 3 pin servo or just use a controller board of a 3 pin servo to make the 5 pin servo into a 3 pin servo. I do not recommend the second method.
## Instructions
In the Raspberry Pi, ```cd```  into ```/home/pi/``` and clone this repo by typing the following into the terminal:
```shell
git clone https://github.com/AkasshShah/CarControllerReciever.git
```
Then ```cd``` into the created directory:
```shell
cd CarControllerReciever
```
Copy the .service file into the ```/etc/systemd/system/``` directory:
```shell
sudo cp CarReciever.service /etc/systemd/system/CarReciever.service
```
Then Start and Enable the service:
```shell
sudo systemctl start myscript.service
sudo systemctl enable myscript.service
```
Enabling the the service just means that it will start on boot.
## Resources
- [Raspberry Pi](https://www.raspberrypi.org/)
- [Systemd and services in raspberry pi](https://www.raspberrypi.org/documentation/linux/usage/systemd.md)