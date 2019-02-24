
APIPROXY=${MASTERURL}/api/v1/proxy/namespaces/openshift-infra/services
HEAPSTERAPI=https:heapster:/api/v1/model
TOKEN=$(oc whoami -t)
curl -k -H "Authorization: Bearer $TOKEN" -X GET $APIPROXY/$HEAPSTER/$NODE/metrics/memory/working_set?start=$START

https://github.com/kubernetes-retired/heapster/blob/master/docs/storage-schema.md
