#!/usr/bin/python
import requests, os, json, sys, time
from subprocess import Popen, PIPE
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import csv

cmd = ["oc", "get", "pods", "--all-namespaces"]

token = "xxxxxxxx"
hawkular_hostname = "xxxxx"
metrics_url='https://{}/hawkular/metrics/gauges/data'.format(hawkular_hostname)

proc = Popen(cmd, stdout=PIPE)

if 'CA_CERT' in os.environ:
    ca_cert = os.environ['CA_CERT']
else:
    print "WARNING: Disabling SSL Verification. This should not be done in Production."
    print "To get rid of this message, export CA_CERT=/path/to/ca-certificate"
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    ca_cert = False

def get_pod_usage(pod_name, namespace, token):
    params = {
        'tags': 'descriptor_name:memory/usage,pod_name:{}'.format(pod_name),
        'bucketDuration' : '60000ms',
        #'stacked' : 'true',
        'start' : '-1mn'
    }

    headers = {
        'Content-Type' : 'application/json',
        'Hawkular-Tenant': namespace,
        'Authorization' : 'Bearer {}'.format(token)
    }

    req = requests.Request(
        'GET',
        metrics_url,
        params=params,
        headers=headers
        )
    prepared = req.prepare()
    s = requests.Session()
    r = s.send(prepared,verify=ca_cert)
    usage=r.json()[0]
    #return usage

    if usage["empty"] == False:
        if usage["min"] == 0:
            return "N/A"
        else:
            return usage["min"]/1.049e+6
    else:
       return "N/A1"


for line in proc.stdout.readlines():
    total_usage = 0
    sxn = line.split()[0]
    sxn2 = line.split()[1]
    sxn1 = line.split()[2]
    if sxn.find("NAMESPACE") == -1:
        if sxn1.find("0") == -1:
              #pod_name = "checkinprocess-api-591-29c22"
              #namespace = "cki-process-api-dvl"
              pod_name = line.split()[1]
              namespace =  line.split()[0]
              #print ("namespace is: ",namespace ,"pod is: ", pod_name)
              #print ("namespace is: ",sxn ,"pod is: ", sxn2)
              total_usage = get_pod_usage(pod_name, namespace, token)
              with open('cluster_usage_dvl.csv', mode='a') as employee_file:
                   employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                   employee_writer.writerow([sxn, sxn2, total_usage])
              #print sxn"," sxn2"," total_usage
              #print total_usage
        else:
           test = "hello"
    else:
       test = "hello"
