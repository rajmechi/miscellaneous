#!/bin/bash
oc login -u admin -p xxxx
TOKEN=$(oc whoami -t)
APIPROXY=https://<master-fqdn>>/api/v1/proxy/namespaces/openshift-infra/
services
HEAPSTER=https:heapster:/api/v1/model
NODE=nodes/<node-fqdn>
START=$(date -d '1 minute ago' -u '+%FT%TZ')
curl -kH "Authorization: Bearer $TOKEN" \
-X GET $APIPROXY/$HEAPSTER/$NODE/metrics/memory/working_set?start=$START
curl -kH "Authorization: Bearer $TOKEN" \
-X GET $APIPROXY/$HEAPSTER/$NODE/metrics/cpu/usage_rate?start=$START
