#!/bin/bash

sh fix/RHEL_6_STIG/sysctl_key_value.sh 'net.ipv4.conf.all.accept_redirects' 0 || exit 1