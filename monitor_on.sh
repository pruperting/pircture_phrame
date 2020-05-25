#!/bin/sh
echo $DISPLAY
export DISPLAY=:0
#exec 1> >(logger -s -t $(basename $0)) 2>&1
#sudo /home/pi/pics.sh > /home/pi/pics.log 2>&1 &
#hdmi_on.sh - custom script to turn HDMI on 
#DATE=$(date +"%Y-%m-%d_%H%M")
#get the current tv state
#tvstate=`tvservice -s | grep HDMI | wc -l`

#only turn on if its not already on
#if [ "$tvstate" -eq 0 ] 
#then
#   tvservice -p
   ##tvservice --explicit="DMT 87"
   #fbset -depth 8
   #fbset -depth 16
#   echo "on 0" | cec-client -s
   #echo "on 0" | cec-client -s
#   tvservice -p
#   chvt 2
#   sleep 5
#   chvt 1
   #sudo chvt 7
   #sudo chvt 1
   #vbetool dpms on
   #xset dpms force off
#else
#   echo "HDMI already on";
#fi
#sudo /usr/sbin/service hyperion start 
tvservice -p
echo "on 0" | cec-client -s -d 1
#echo "on 0" | cec-client -s -d 1
/home/pi/conky.sh &
#xinit /usr/bin/conky &
sleep 15
sudo fim -RuwHv -T 2  -d /dev/fb0 --slideshow=15 /home/pi/pics/photophrame >> /home/pi/pics.log 2>&1 &
sleep 10
#exec 1> >(logger -s -t $(basename $0)) 2>&1
sudo killall /usr/bin/conky
#sudo xkill -a
sudo killall /usr/bin/X
#sleep 5
#sudo fim -RuwHv -T 2  -d /dev/fb0 --slideshow=15 /home/pi/pics/photophrame >> /home/pi/pics.log 2>&1 &
#feh -F --zoom max -D 3 --hide-pointer --sort name --version-sort
##sudo mplayer -vo fbdev:/dev/fb0 http://192.168.1.3:8081 &
#cvlc -I rc --vout directfb /dev/fb0 http://192.168.1.3:8081
exit;





# ruperts old one
##tvservice -p
# && fbset -depth 8 && fbset -depth 16
