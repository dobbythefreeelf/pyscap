#!/bin/bash

e=`sysctl net.ipv4.conf.default.send_redirects | grep -P 'net\.ipv4\.conf\.default\.send_redirects\s*=\s*0$'`
if [[ "x$e" == "x" ]]; then
	echo '<result>fail</result><message>net.ipv4.conf.default.send_redirects is not 0</message>'
	exit
fi

echo '<result>pass</result>'


