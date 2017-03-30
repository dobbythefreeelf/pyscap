#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	fail "The DBMS must employ NIST validated cryptography to protect unclassified information: not supported"
else
	notchecked
fi
