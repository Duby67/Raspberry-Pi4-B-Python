wget -qO - https://raw.githubusercontent.com/tvdsluijs/sh-python-installer/main/python.sh | sudo bash -s 3.11.0 \n
python3.11 –version \n
sudo raspi-config \n
echo "deb http://archive.raspberrypi.org/debian/ buster main" >> /etc/apt/sources.list \n
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 7FA3303E \n
sudo apt-get update \n
sudo apt-get install raspi-config \n
