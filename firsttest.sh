#!/bin/bash

#preparation phase
accounts="acc.txt"
sleep 5
echo 'retreiving account'
while IFS=':' read -r line1; do
    echo "email and password is: $line1"
    arrIN=(${line1//:/ })
    echo ${arrIN[0]}
    FLOOR=1;
    CEILING=5;
    RANGE=$(($CEILING-$FLOOR+1));
    RESULT=$RANDOM;
    let "RESULT %= $RANGE";
    prof=$(($RESULT+$FLOOR));
    echo $prof

	firefox -P $prof --private-window https://accounts.google.com/ServiceLogin/identifier?service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin &
	while [ 1 ]; do
	  sleep 10
	  xdotool type ${arrIN[0]}
	  sleep 10
	  xdotool key Return
	  sleep 10
	  xdotool type ${arrIN[1]}
	  sleep 10
	  xdotool key Return
	  sleep 10
	  # entering recovvery email
	  xdotool mousemove 1912 1189 click 1 &
	  sleep 10
	  xdotool type ${arrIN[2]}
	  sleep 5
	  xdotool key Return
	  sleep 15
	  #completing gmail signin
	  xdotool mousemove 1790 1310 click 1 &
	  sleep 10
	  #redirecting to Hi5
	  xdotool mousemove 243 76 click 1 &
	  sleep 2
	  xdotool type --delay 100 'https://secure.hi5.com/'
	  sleep 2
	  xdotool key Return
	  sleep 20 
	  #Signing in with google
	  xdotool mousemove 1576 553 click 1 &
	  sleep 10
	  #clicking the account in the pop up
	  xdotool mousemove 1928 1041 click 1 &
	  sleep 10
	  #clicking the allow button
	  xdotool mousemove 2046 1321 click 1 &
	  sleep 10
	  #retreiving the S session from inspector
	  # xdotool key ctrl+shift+i
	  # sleep 5
	  # #selecting the right session
	  # xdotool mousemove 718 802 click 1 &
	  # sleep 2
	  # xdotool type 'session'
	  # sleep 2
	  # #copying 3rd session
	  # xdotool mousemove 461 890 click 1 &
	  # #1st session
	  # #xdotool mousemove 710 891 click 1 &
	  # sleep 3
	  # xdotool click 1; xdotool click 1
	  # sleep 3
	  # xdotool key ctrl+c
	  # sleep 2
	  # xsel -b > sessions.txt
	  # sleep 2
	  # cat sessions.txt
	  python3 updater.py
	  sleep 15
	  echo 'this is when the sleep is done'
	  pkill -f firefox

	  #re-signing in for updating password and adding profile
	  firefox -P $prof --private-window https://accounts.google.com/ServiceLogin/identifier?service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin &

	  sleep 10
	  xdotool type ${arrIN[0]}
	  sleep 5
	  xdotool key Return
	  sleep 5
	  xdotool type ${arrIN[1]}
	  sleep 5
	  xdotool key Return
	  sleep 10
	  #redirecting to Hi5
	  xdotool mousemove 243 72 click 1 &
	  sleep 2
	  xdotool type --delay 100 'https://secure.hi5.com/'
	  sleep 2
	  xdotool key Return
	  sleep 10 
	  #Signing in with google
	  xdotool mousemove 1576 553 click 1 &
	  sleep 10
	  #clicking the account in the pop up
	  xdotool mousemove 1928 1041 click 1 &
	  sleep 10
	  #Redirecting To Settings page
	  xdotool mousemove 683 111 click 1 &
	  xdotool  type --delay 100 'https://secure.hi5.com/account_info.html?dataSource=Settings&ll=nav'
	  sleep 2
	  xdotool key Return
	  sleep 10
	  #editing the password within browser
	  xdotool mousemove 1029 359 click 1 &
	  sleep 5
	  xdotool mousemove 749 431 click 1 &
	  sleep 2
	  xdotool type 'NewPassword456'
	  sleep 2
	  xdotool key Tab
	  sleep 2
	  xdotool type 'NewPassword456'
	  sleep 2
	  xdotool key Tab
	  sleep 2
	  xdotool type 'NewPassword456'
	  sleep 2
	  xdotool mousemove 893 582 click 1 &
	  sleep 5
	  #Redirecting To Profile Editing page
	  xdotool mousemove 683 111 click 1 &
	  xdotool type --delay 100 'http://www.hi5.com/edit_profile.html?dataSource=profileEditProfile&ll=1'
	  sleep 2
	  xdotool key Return
	  sleep 20
	  #adding profile picture
	  xdotool mousemove 1843 423 click 1 &
	  sleep 2
	  xdotool mousemove 1840 375 click 1 &
	  sleep 2
	  piclink=$(shuf -n 1 piclinks.txt)
	  xdotool type $piclink
	  sleep 2
	  xdotool mousemove 1841 421 click 1 &
	  sleep 5
	  pkill -f firefox
	  echo "account done!"
	  sleep 400
	done
	sleep 6000
done < acc.txt
echo "Script Is Done"
