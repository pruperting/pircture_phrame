#!/bin/bash
#hdmi_off.sh - shell script to turn HDMI off - should work universially
exec 1> >(logger -s -t $(basename $0)) 2>&1
kill_pics ()
{
echo "killing fim - getting pid"
echo "killing fim" >> /home/pi/moff.log
VPID=( $(ps -e | grep fim | awk '{print $1;}')) >> /home/pi/moff.log
if [ $? = 1 ];then >> /home/pi/moff.log
        echo "error getting pid" >> /home/pi/moff.log
fi
while [ -n "$VPID" ];do >> /home/pi/moff.log
        echo "killing fim $VPID"
        sudo kill $VPID >> /home/pi/moff.log
        VPID=( $(ps -e | grep fim | awk '{print $1;}')) >> /home/pi/moff.log
done >> /home/pi/moff.log
}


kill_pics >> /home/pi/killpics.log
sudo killall /usr/bin/conky
#sudo xkill -a
sudo killall /usr/bin/X
tvservice -o
echo "standby 0" | cec-client -s -d 1
#echo "standby 0" | cec-client -s -d 1
#echo "standby 0" | cec-client -s -d 1
#hyperion-remote --clear
#hyperion-remote --clearall
#sudo /usr/sbin/service hyperion stop

exit



