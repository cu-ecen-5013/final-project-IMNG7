sudo /sbin/route add default gw 192.168.7.1
sudo tightvncserver
sudo vncserver :1 -geometry 1920x1080 -depth 24 -dpi 96
cd /etc
touch resolv.conf
chmod 777 resolv.conf
echo "nameserver 127.0.0.1" > resolv.conf
echo "nameserver 8.8.8.8" >> resolv.conf
echo "nameserver 8.8.4.4" >> resolv.conf