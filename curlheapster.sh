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

Example Response:
{
  "metrics": [
   {
    "timestamp": "2019-02-26T20:52:30Z",
    "value": 3655204864
   },
   {
    "timestamp": "2019-02-26T20:53:00Z",
    "value": 3633487872
   },
   {
    "timestamp": "2019-02-26T20:53:30Z",
    "value": 3634749440
   },
   {
    "timestamp": "2019-02-26T20:54:00Z",
    "value": 3634827264
   },
   {
    "timestamp": "2019-02-26T20:54:30Z",
    "value": 3634700288
   },
   {
    "timestamp": "2019-02-26T20:55:00Z",
    "value": 3634757632
   },
   {
    "timestamp": "2019-02-26T20:55:30Z",
    "value": 3635040256
   },
   {
    "timestamp": "2019-02-26T20:56:00Z",
    "value": 3634778112
   },
   {
    "timestamp": "2019-02-26T20:56:30Z",
    "value": 3634786304
   },
   {
    "timestamp": "2019-02-26T20:57:00Z",
    "value": 3634978816
   },
   {
    "timestamp": "2019-02-26T20:57:30Z",
    "value": 3634860032
   },
   {
    "timestamp": "2019-02-26T20:58:00Z",
    "value": 3635105792
   },
   {
    "timestamp": "2019-02-26T20:58:30Z",
    "value": 3634941952
   },
   {
    "timestamp": "2019-02-26T20:59:00Z",
    "value": 3634978816
   },
   {
    "timestamp": "2019-02-26T20:59:30Z",
    "value": 3634982912
   },
   {
    "timestamp": "2019-02-26T21:00:00Z",
    "value": 3635003392
   },
   {
    "timestamp": "2019-02-26T21:00:30Z",
    "value": 3635306496
   },
   {
    "timestamp": "2019-02-26T21:01:00Z",
    "value": 3635314688
   },
   {
    "timestamp": "2019-02-26T21:01:30Z",
    "value": 3506556928
   },
   {
    "timestamp": "2019-02-26T21:02:00Z",
    "value": 3506569216
   },
   {
    "timestamp": "2019-02-26T21:02:30Z",
    "value": 3506577408
   },
   {
    "timestamp": "2019-02-26T21:03:00Z",
    "value": 3506581504
   },
   {
    "timestamp": "2019-02-26T21:03:30Z",
    "value": 3506696192
   },
   {
    "timestamp": "2019-02-26T21:04:00Z",
    "value": 3506987008
   },
   {
    "timestamp": "2019-02-26T21:04:30Z",
    "value": 3506597888
   },
   {
    "timestamp": "2019-02-26T21:05:00Z",
    "value": 3506606080
   },
   {
    "timestamp": "2019-02-26T21:05:30Z",
    "value": 3506610176
   },
   {
    "timestamp": "2019-02-26T21:06:00Z",
    "value": 3506704384
   },
   {
    "timestamp": "2019-02-26T21:06:30Z",
    "value": 3506622464
   },
   {
    "timestamp": "2019-02-26T21:07:00Z",
    "value": 3506634752
   }
  ],
  "latestTimestamp": "2019-02-26T21:07:00Z"
  }

