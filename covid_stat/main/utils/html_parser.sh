#!/bin/bash

wget -O ./source.html https://стопкоронавирус.рф/information/

parseHTML=`grep -o 'stats-data=.* :charts-data=' ./source.html`

for field in "sick" "healed" "sickChange" "healedChange"; do
  if [ $field == "sick" ] || [ $field == "healed" ]; then
    echo $parseHTML | grep -oE "\"${field}\":\".*?\"" | awk -F ':' '{print $2}' | awk -F '"|"' '{print $2}'
  else
    echo $parseHTML | grep -oE "\"${field}\":\".*?\"" | awk -F ':' '{print $2}' | awk -F '[+:"]' '{print $3}'
  fi
done
