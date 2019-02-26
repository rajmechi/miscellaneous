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


Examples:
# curl -kH "Authorization: Bearer zzzz" -X GET "https://XXXX:8443/api/v1/proxy/namespaces/openshift-infra/services/https:heapster:/api/v1/model/namespaces/PROJECT-NAME/pods/POD-NAME/metrics/memory-usage" | grep "value" | tail -4
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2347    0  2347    0     0  25480      0 --:--:-- --:--:-- --:--:-- 25791
    "value": 2493902848
    "value": 2493915136
    "value": 2489217024
    "value": 2489217024
# curl -kH "Authorization: Bearer zzzz" -X GET "https://XXXX:8443/api/v1/proxy/namespaces/openshift-infra/services/https:heapster:/api/v1/model/namespaces/PROJECT-NAME/pods/POD-NAME/metrics/memory-usage" | grep "value" | tail -4
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2347    0  2347    0     0  20610      0 --:--:-- --:--:-- --:--:-- 20769
    "value": 1024651264
    "value": 1024651264
    "value": 1024651264
    "value": 1024651264
# curl -kH "Authorization: Bearer zzzz" -X GET "https://XXXX:8443/api/v1/proxy/namespaces/openshift-infra/services/https:heapster:/api/v1/model/namespaces/PROJECT-NAME/metrics/memory-usage" | grep "value" | tail -4
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2347    0  2347    0     0  20069      0 --:--:-- --:--:-- --:--:-- 20232
    "value": 3518566400
    "value": 3513868288
    "value": 3513868288
    "value": 3514368000
