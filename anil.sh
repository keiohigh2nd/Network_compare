#!/bin/bash
set -xu  

amd_aside=amd_aside
dm_aside=dm_aside
non_aside=non_aside

amd_main=ADN/AMD
dm_main=ADN/DM
non_main=ADN/non

testfit=oph_March.fit
wndchrm=/home/appl/bin/wndchrm-1.31.251-fast
iteration=3
python=/home/appl/bin/python2.7
iteration_test=10

num_repeat_mv=$((RANDOM % 100))
num_repeat_random_image=$num_repeat_mv/2

for i in `seq $num_repeat_ramdom_image`; do
    
   for i in `seq $num_repeat_mv`; do
     num_image_id=$((RANDOM % 100))
     mv $amd_main/$num_image_id'.sig' $am_aside/
     sleep 1
   done
  
   for i in `seq $num_repeat_mv`; do
     num_image_id=$((RANDOM % 100))
     mv $dm_main/$num_image_id'.sig' $dm_aside/
     sleep 1
   done

   for i in `seq $num_repeat_mv`; do
     num_image_id=$((RANDOM % 100))
     mv $non_main/$num_image_id'.sig' $non_aside/
     sleep 1
   done

   for i in `seq $iteration_test` ; do
       $wndchrm test ADN/ oph_March.fit >> tmp1.txt
       sleep 1
   done
   
   mv $amd_aside/'*.sig' $am_main/  
   mv $dm_aside/'*.sig' $dm_main/
   mv $non_aside/'*.sig' $non_main/  

done

grep 'Average accuracy' tmp1.txt |  awk '{print substr($0,30,8)}' > result.txt 
$python num_take.py > average.txt
cost_now=$python num_take.py

while True:
    if $T -gt 0.1; then
      P= $cost_now-$cost_new/T

      if $cost_now -gt $cost_new; then
          if $P -gt $((RANDOM % 100)); then
              $x = $x + 1
          else
              $x = $x - 1
          done
      $T \* 0.95
      done
  
      elif T -lt 0.1
          if $cost_old -gt $cost_now; then
             if $cost_now -lt $cost_new; then
                break
             fi
          elif $cost_now -gt $cost_new
              $x = $x + 1
          else
             $x = $x -1 
          done
      done 
    
    done       
done
echo done

