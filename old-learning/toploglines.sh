#!/bin/bash
#New file created
for logfile in /private/var/log/*.log; do
    echo "Processing: $logfile"
    cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -15
done
