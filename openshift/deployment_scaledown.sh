#!/bin/bash
#usage /bin/sh deployment_scaledown.sh 15      where 15 is the days

oc get pods --all-namespaces | grep sbx  | grep Running | grep -v jenkins  > cleanpods.out

while read line
do
    stringd=$( echo ${line} | awk '{ print $6 }' )
    if [[ $stringd == *"d"* ]]; then
       numdays=$( echo $stringd | tr -d 'd')
       if [ "$numdays" -gt "$1" ]; then
           #echo $numdays
           #echo $line
           podname=$( echo ${line} | awk '{ print $2 }' )
           namespacename=$( echo ${line} | awk '{ print $1 }' )
           dcname=$(oc get pod ${podname} -n ${namespacename} -o=jsonpath='{.metadata.annotations.openshift\.io/deployment-config\.name}')
           if [[ -z $dcname ]]; then
              echo "pod not exist"
           else
              echo "namespace: $namespacename dcname:  $dcname  podname:  $podname daysrunning: $numdays"
              #oc scale dc $dcname -n $namespacename--replicas=0
           fi

           #sleep 2
       fi
    fi
done < cleanpods.out
