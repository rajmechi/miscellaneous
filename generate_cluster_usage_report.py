#RUN python3 <scriptname>
#REPLACE <REPLACE TOKEN> AND <REPLACE URL>
# Choose Megabytes or MIB at totalmemusage etc.

import json
import requests
#disable insecure certificate warning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import csv

#initiate CSV
with open('cluster_usage.csv', mode='a') as usage_file:
         usage_writer = csv.writer(usage_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
         usage_writer.writerow(['namespace', 'Memory Usage', 'Memory Request', 'Memory Limit', 'CPU Uaage Rate', 'CPU Request', 'CPU Limit' ])

#change below vars
ocpurl = "https://<replace URL>"
ocpuullistns = ocpurl + ":443/api/v1/namespaces"
headers = {"Authorization": "Bearer <REPLACE TOKEN>"}

test = requests.get(ocpuullistns, headers=headers, verify=False).json()
rtoutjson = json.dumps(test, indent = 4)
rtoutjsonload = json.loads(rtoutjson)
#find the jason array length for list of projects
numprojects = len(rtoutjsonload['items'])
i = 0
#print("Total Number of Projects are  " + str(numprojects))
#loop through all namespaces


while i < numprojects:
    #print(rtoutjsonload['items'][i]['metadata']['name'])
    #'''
    #GET CURRENT MEMORY USAGE
    try:
      urlnew =  ocpurl + ":443/api/v1/namespaces/openshift-infra/services/https:heapster:/proxy/api/v1/model/namespaces/" + rtoutjsonload['items'][i]['metadata']['name'] + "/metrics/memory/usage"
      #print(urlnew)
      getmemusage = requests.get(urlnew, headers=headers, verify=False).json()
      getmemusagetojson = json.dumps(getmemusage,  indent = 4)
      getmemusagetojsonload =  json.loads(getmemusagetojson)
      #print(getmemusagetojsonload)
      lastonelen = len(getmemusagetojsonload['metrics'])-1
      #numtimestamplen = len(getmemusagetojsonload['metrics'])
      #print("Memory usage in Mebibyte of " + rtoutjsonload['items'][i]['metadata']['name'] + " is " + str(getmemusagetojsonload['metrics'][lastonelen]['value']/1.049e+6))
      #print("Memory usage in Megabyte of " + rtoutjsonload['items'][i]['metadata']['name'] + " is " + str(getmemusagetojsonload['metrics'][lastonelen]['value']/1000000))
      #totalmemusage = getmemusagetojsonload['metrics'][lastonelen]['value']/1.049e+6)
      totalmemusage = getmemusagetojsonload['metrics'][lastonelen]['value']/1000000
    except:
      totalmemusage = 0
      #print("Something else went wrong while getting memory/usage for namespace " + rtoutjsonload['items'][i]['metadata']['name'] )
    #'''
    #'''
    #GET TOTAL REQUESTS
    try:
      urlnew =  ocpurl + ":443/api/v1/namespaces/openshift-infra/services/https:heapster:/proxy/api/v1/model/namespaces/" + rtoutjsonload['items'][i]['metadata']['name'] + "/metrics/memory/request"
      #print(urlnew)
      getmemreq = requests.get(urlnew, headers=headers, verify=False).json()
      getmemreqtojson = json.dumps(getmemreq,  indent = 4)
      getmemreqtojsonload =  json.loads(getmemreqtojson)
      #print(getmemreqtojsonload)
      lastonelenmemreq = len(getmemreqtojsonload['metrics'])-1
      #print("Memory request in Megabyte of " + rtoutjsonload['items'][i]['metadata']['name'] + " is " + str(getmemreqtojsonload['metrics'][lastonelenmemreq]['value']/1000000))
      #print("Memory request in Mebibyte of " + rtoutjsonload['items'][i]['metadata']['name'] + " is " + str(getmemreqtojsonload['metrics'][lastonelenmemreq]['value']/1.049e+6))
      #totalmemreq = getmemreqtojsonload['metrics'][lastonelenmemreq]['value']/1.049e+6
      totalmemreq = getmemreqtojsonload['metrics'][lastonelenmemreq]['value']/1000000
    except:
      totalmemreq = 0
      #print("Something else went wrong while getting memory/request for namespace " + rtoutjsonload['items'][i]['metadata']['name'] )
    #'''
    #'''
    #GET MEMORY LIMIT
    try:
      urlnew =  ocpurl + ":443/api/v1/namespaces/openshift-infra/services/https:heapster:/proxy/api/v1/model/namespaces/" + rtoutjsonload['items'][i]['metadata']['name'] + "/metrics/memory/limit"
      #print(urlnew)
      getmemlimit = requests.get(urlnew, headers=headers, verify=False).json()
      getmemlimittojson = json.dumps(getmemlimit,  indent = 4)
      getmemlimittojsonload =  json.loads(getmemlimittojson)
      #print(getmemlimittojsonload)
      lastonelenmemlimit = len(getmemlimittojsonload['metrics'])-1
      #print("Memory Limit in Megabyte of " + rtoutjsonload['items'][i]['metadata']['name'] + " is " + str(getmemlimittojsonload['metrics'][lastonelenmemlimit]['value']/1000000))
      #print("Memory Limit in Mebibyte of " + rtoutjsonload['items'][i]['metadata']['name'] + " is " + str(getmemlimittojsonload['metrics'][lastonelenmemlimit]['value']/1.049e+6))
      totalmemlimit = getmemlimittojsonload['metrics'][lastonelenmemlimit]['value']/1000000
      #totalmemlimit = getmemlimittojsonload['metrics'][lastonelenmemlimit]['value']/1.049e+6)
    except:
      totalmemlimit = 0
      #print("Something else went wrong while getting memory/limit for namespace " + rtoutjsonload['items'][i]['metadata']['name'] )
    #'''
    #'''
    #GET CPU LIMIT
    try:
      urlnew =  ocpurl + ":443/api/v1/namespaces/openshift-infra/services/https:heapster:/proxy/api/v1/model/namespaces/" + rtoutjsonload['items'][i]['metadata']['name'] + "/metrics/cpu/limit"
      getcpulimit = requests.get(urlnew, headers=headers, verify=False).json()
      getcpulimittojson = json.dumps(getcpulimit,  indent = 4)
      getcpulimittojsonload =  json.loads(getcpulimittojson)
      #print(getcpulimittojsonload)
      lastonelencpulimit = len(getcpulimittojsonload['metrics'])-1
      #print("CPU limit of " + rtoutjsonload['items'][i]['metadata']['name'] + " is " + str(getcpulimittojsonload['metrics'][lastonelencpulimit]['value']/1000000))
      #print("CPU limit of " + rtoutjsonload['items'][i]['metadata']['name'] + " is " + str(getcpulimittojsonload['metrics'][lastonelencpulimit]['value']))
      totalcpulimit = getcpulimittojsonload['metrics'][lastonelencpulimit]['value']
    except:
      totalcpulimit = 0
      #print("Something else went wrong while getting cpu/limit for namespace " + rtoutjsonload['items'][i]['metadata']['name'] )
    #'''
    #'''
    #GET CPU REQUEST
    try:
      urlnew =  ocpurl + ":443/api/v1/namespaces/openshift-infra/services/https:heapster:/proxy/api/v1/model/namespaces/" + rtoutjsonload['items'][i]['metadata']['name'] + "/metrics/cpu/request"
      getcpureq = requests.get(urlnew, headers=headers, verify=False).json()
      getcpureqtojson = json.dumps(getcpureq,  indent = 4)
      getcpureqtojsonload =  json.loads(getcpureqtojson)
      #print(getcpureqtojsonload)
      lastonelencpureq = len(getcpureqtojsonload['metrics'])-1
      #print("CPU request of " + rtoutjsonload['items'][i]['metadata']['name'] + " is " + str(getcpureqtojsonload['metrics'][lastonelencpureq]['value']/1000000))
      #print("CPU request of " + rtoutjsonload['items'][i]['metadata']['name'] + " is " + str(getcpureqtojsonload['metrics'][lastonelencpureq]['value']))
      totalcpureq = getcpureqtojsonload['metrics'][lastonelencpureq]['value']
    except:
      totalcpureq = 0
      #print("Something else went wrong while getting cpu/request for namespace " + rtoutjsonload['items'][i]['metadata']['name'] )
    #'''
    #'''
    #GET CPU USAGE RATE
    try:
      urlnew =  ocpurl + ":443/api/v1/namespaces/openshift-infra/services/https:heapster:/proxy/api/v1/model/namespaces/" + rtoutjsonload['items'][i]['metadata']['name'] + "/metrics/cpu/usage_rate"
      getcpuusagerate = requests.get(urlnew, headers=headers, verify=False).json()
      getcpuusageratetojson = json.dumps(getcpuusagerate,  indent = 4)
      getcpuusageratetojsonload =  json.loads(getcpuusageratetojson)
      #print(getcpuusageratetojsonload)
      lastonelencpuusagerate = len(getcpuusageratetojsonload['metrics'])-1
      #print("CPU Usage rate of " + rtoutjsonload['items'][i]['metadata']['name'] + " is " + str(getcpuusageratetojsonload['metrics'][lastonelencpuusagerate]['value']/1000000))
      #print("CPU Usage rate of " + rtoutjsonload['items'][i]['metadata']['name'] + " is " + str(getcpuusageratetojsonload['metrics'][lastonelencpuusagerate]['value']))
      totalcpuusgrate = getcpuusageratetojsonload['metrics'][lastonelencpuusagerate]['value']
    except:
      totalcpuusgrate = 0
      #print("Something else went wrong while getting cpu/usage_rate for namespace " + rtoutjsonload['items'][i]['metadata']['name'] )
    #```
    print(rtoutjsonload['items'][i]['metadata']['name'] + " " + str(totalmemusage) + " "  + str(totalmemreq) + " "  + str(totalmemlimit) + " "  + str(totalcpulimit) + " "  + str(totalcpureq) + " "  + str(totalcpuusgrate) )
    #push values into CSV
    with open('cluster_usage.csv', mode='a') as usage_file:
              usage_writer = csv.writer(usage_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
              usage_writer.writerow([rtoutjsonload['items'][i]['metadata']['name'], totalmemusage, totalmemreq, totalmemlimit, totalcpuusgrate, totalcpureq, totalcpulimit ])
    i += 1
