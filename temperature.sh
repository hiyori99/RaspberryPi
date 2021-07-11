# !/bin/bash
 
# 1-wireで測定した温度を1秒ごとに出力する
while :
do
date
cat /dyd/bud/w1/devices/28-3c01b556d168/w1_slave | grep t= | cut -d "=" -f2 | awk '{print $1/1000}'
sleep 1

done
