#!/bin/bash

#Variables
FILE="curl-format.txt"
STRING=`ls ${FILE}`
WEB="https://mauricio-271700.appspot.com/"
HTTPS=`curl -I ${WEB} | grep -i http | awk '{print $2}'`

#functions

evaluate_connectivity() {
    if [[ ${TIME_NAMELOOKUP} > 0.5 ]]; then 
        MESSAGE="WARNING DNS resolution slow: ${TIME_NAMELOOKUP} seconds"
        echo ${MESSAGE}
        notify_slack
    fi
    if [[ ${TIME_REDIRECT} > 0.5 ]]; then
       echo "WARNING stuck in redirections: ${TIME_REDIRECT} seconds"
       echo ${MESSAGE}
       notify_slack       
    fi
    if [[ ${TIME_TOTAL} > 1 ]]; then
       MESSAGE="WARNING latency: ${TIME_TOTAL} seconds"
       echo ${MESSAGE}
       notify_slack
       MESSAGE=`cat ${time}.txt`
       notify_slack
    fi
}

notify_slack() {
    webhook="REPLACE ME with a Jenkin's variable that contains and Slack's webhook'"
    curl -X POST --data-urlencode "payload={\"channel\": \"#random\", \"username\": \"webhookbot\", \"text\": \"${MESSAGE}\", \"icon_emoji\": \":ghost:\"}" ${webhook}
   }

#Script
#Make sure you have @curl-format.txt
if [[ -n ${STRING} ]]; then
   echo "There is ${FILE} here"
else
   echo "there is nothing here, creating ${FILE}"
   echo "time_namelookup:  %{time_namelookup}\n" >> ${FILE}
   echo "time_connect:  %{time_connect}\n" >> ${FILE}  
   echo "time_appconnect:  %{time_appconnect}\n" >> ${FILE}
   echo "time_pretransfer:  %{time_pretransfer}\n" >> ${FILE}
   echo "time_redirect:  %{time_redirect}\n" >> ${FILE}
   echo "time_starttransfer:  %{time_starttransfer}\n" >> ${FILE}
   echo "----------\n" >> ${FILE}
   echo "time_total:  %{time_total}\n" >> ${FILE}
fi

echo "Evaluating basic connectivity"

if [[ ${HTTPS} -eq 200 ]]; then
   echo "O.K."
elif [[ ${HTTPS} -eq 500 ]]; then
   MESSAGE="ALERT: Your App is DOWN!!!"
   echo ${MESSAGE}
   notify_slack  
elif [[ ${HTTPS} -eq 400 ]]; then
   MESSAGE="ALERT: Your App is DOWN!!!"
   echo ${MESSAGE}
   notify_slack
elif [[ ${HTTPS} -eq 401 ]]; then
   MESSAGE="WARNING: Yoou are UNAUTHORIZED!!!"
   echo ${MESSAGE}
   notify_slack 
elif [[ ${HTTPS} -eq 403 ]]; then
   MESSAGE="WARNING: You are FORBIDDEN!!!" 
   echo ${MESSAGE}
   notify_slack
else 
    time=`date --rfc-3339=seconds | sed 's/ /T/'`
    curl -w "@${FILE}" -o /dev/null -s ${WEB} > ${time}.txt
    TIME_NAMELOOKUP=`cat ${time}.txt | grep time_namelookup | awk '{print $2}'`
    TIME_CONNECT=`cat ${time}.txt | grep time_connect | awk '{print $2}'`
    TIME_APPCONNECT=`cat ${time}.txt | grep time_appconnect | awk '{print $2}'`
    TIME_PRETRANSFER=`cat ${time}.txt | grep time_pretransfer | awk '{print $2}'`
    TIME_REDIRECT=`cat ${time}.txt | grep time_redirect | awk '{print $2}'`
    TIME_STARTTRANSFER=`cat ${time}.txt | grep time_starttransfer | awk '{print $2}'`
    TIME_TOTAL=`cat ${time}.txt | grep time_total | awk '{print $2}'`
    evaluate_connectivity
fi    


