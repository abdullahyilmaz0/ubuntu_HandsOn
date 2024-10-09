#!/bin/bash

# Directory where reports are saved
report_dir="/path/to/reports"
# Date format for today's reports
today=$(date +'%Y%m%d')

# Find reports generated today
reports=$(find "$report_dir" -name "delays_report_${today}*.xlsx")

if [ -z "$reports" ]; then
    # No reports found, send error to syslog server
    logger -n www.syfco.be -P 514 -T "ERROR: No reports generated for today"
else
    # Reports found, send success to syslog server
    logger -n www.syfco.be -P 514 -T "SUCCESS: Reports generated for today"
fi
