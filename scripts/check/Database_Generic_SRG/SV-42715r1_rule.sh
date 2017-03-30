#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	echo '<result>fail</result><message>The DBMS does not provide a real-time alert when organization defined audit failure events occur.</message>'
else
	echo '<result>notchecked</result>'
fi