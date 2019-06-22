'''
RUN python3 <scriptname>
REPLACE <REPLACE TOKEN> AND <REPLACE URL>
Choose Megabytes or MIB at totalmemusage etc.

Example output:
cat cluster_usage.csv 
namespace,Memory Usage,Memory Request,Memory Limit,CPU Uaage Rate,CPU Request,CPU Limit
app-storage,1934.893056,314.5728,0.0,22,300,0
chris-bolton-sbx,453.984256,536.870912,536.870912,2,0,0
default,18792.931328,1610.612736,0.0,425,600,0
gtmtest,38.248448,0.0,0.0,2,0,0
'''

import json
import requests
#disable insecure certificate warning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import csv

#initiate CSV
with open('cluster_usage.csv', mode='a') as usage_file:
         usage_writer = csv.writer(usage_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
         usage_writer.writerow(['namespace', 'Memory Usage-MiB', 'Memory Request-MiB', 'Memory Limit-MiB', 'CPU Uaage Rate', 'CPU Request', 'CPU Limit', 'Memory Quots-MiB', 'CPU Quots' ])

#change below vars
ocpurl = "https://<REPLACE URL>"
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
      totalmemusage = getmemusagetojsonload['metrics'][lastonelen]['value']/1.049e+6
      #totalmemusage = getmemusagetojsonload['metrics'][lastonelen]['value']/1000000
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
      totalmemreq = getmemreqtojsonload['metrics'][lastonelenmemreq]['value']/1.049e+6
      #totalmemreq = getmemreqtojsonload['metrics'][lastonelenmemreq]['value']/1000000
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
      #totalmemlimit = getmemlimittojsonload['metrics'][lastonelenmemlimit]['value']/1000000
      totalmemlimit = getmemlimittojsonload['metrics'][lastonelenmemlimit]['value']/1.049e+6
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
    #```
    try:
      urlnew =  ocpurl + ":443/api/v1/namespaces/" + rtoutjsonload['items'][i]['metadata']['name'] + "/resourcequotas"
      #print(urlnew)
      getmemusage = requests.get(urlnew, headers=headers, verify=False).json()
      getmemusagetojson = json.dumps(getmemusage,  indent = 4)
      getmemusagetojsonload =  json.loads(getmemusagetojson)
      #print(getmemusagetojsonload)
      #lastonelen = len(getmemusagetojsonload['metrics'])-1
      numtimestamplen = len(getmemusagetojsonload['items'])
      #print(str(numtimestamplen))
      if numtimestamplen == 0:
         memory_quota = 0
         cpu_quota = 0
         print(rtoutjsonload['items'][i]['metadata']['name'] + "CPU: " + str(cpu_quota) + " MEMORY: " + str(memory_quota) )
      else:
         if "-prd" or "-int" or "-dvl" or "-build" in rtoutjsonload['items'][i]['metadata']['name']:
             urlnew =  ocpurl + ":443/api/v1/namespaces/" + rtoutjsonload['items'][i]['metadata']['name'] + "/resourcequotas/quota"
             getmemusage = requests.get(urlnew, headers=headers, verify=False).json()
             getmemusagetojson = json.dumps(getmemusage,  indent = 4)
             getmemusagetojsonload =  json.loads(getmemusagetojson)
             cpu_quota = (getmemusagetojsonload["spec"]["hard"]["cpu"]).replace("m","")
             memory_quota = (getmemusagetojsonload["spec"]["hard"]["memory"]).replace("Gi","")
             #print(rtoutjsonload['items'][i]['metadata']['name'] + "CPU: " + cpu_quota + " MEMORY: " + memory_quota )
         elif "-1-sbx" or "-2-sbx" in rtoutjsonload['items'][i]['metadata']['name']:
              cpu_quota = 2
              memory_quota = 12
         elif "sbx-" in rtoutjsonload['items'][i]['metadata']['name']:
              cpu_quota = 2
              memory_quota = 12
         else:
             urlnew =  ocpurl + ":443/api/v1/namespaces/" + rtoutjsonload['items'][i]['metadata']['name'] + "/resourcequotas/quota"
             getmemusage = requests.get(urlnew, headers=headers, verify=False).json()
             getmemusagetojson = json.dumps(getmemusage,  indent = 4)
             getmemusagetojsonload =  json.loads(getmemusagetojson)
             cpu_quota = (getmemusagetojsonload["spec"]["hard"]["cpu"]).replace("m","")
             memory_quota = (getmemusagetojsonload["spec"]["hard"]["memory"]).replace("Gi","")
             #print(rtoutjsonload['items'][i]['metadata']['name'] + "CPU: " + cpu_quota + " MEMORY: " + memory_quota )
    except:
      memory_quota = 0
      cpu_quota = 0
    #```
    #print(rtoutjsonload['items'][i]['metadata']['name'] + " " + str(totalmemusage) + " "  + str(totalmemreq) + " "  + str(totalmemlimit) + " "  + str(totalcpulimit) + " "  + str(totalcpureq) + " "  + str(totalcpuusgrate) + memory_quota + cpu_quota)
    #push values into CSV
    with open('cluster_usage.csv', mode='a') as usage_file:
              usage_writer = csv.writer(usage_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
              usage_writer.writerow([rtoutjsonload['items'][i]['metadata']['name'], totalmemusage, totalmemreq, totalmemlimit, totalcpuusgrate, totalcpureq, totalcpulimit, memory_quota, cpu_quota ])
    i += 1


with open('cluster_usage.csv') as fin:
    headerline = fin.__next__()
    tmemuage = 0
    tmemreq = 0
    tmemlimit = 0
    tcpuusage = 0
    tcpurequests = 0
    tcpulimits = 0
    tmemquotas = 0
    tcpuquotas = 0
    for row in csv.reader(fin):
        tmemuage += float(row[1])
        tmemreq += float(row[2])
        tmemlimit += float(row[3])
        tcpuusage += float(row[4])
        tcpurequests += float(row[5])
        tcpulimits += float(row[6])
        tmemquotas += float(row[7])
        tcpuquotas += float(row[8])
    s = """ Total Memory Uaage: %s
 Total Memory Request: %s
 Total Memory Limit: %s
 Total CPU Uage: %s
 Total CPU Requests: %s
 Total CPU limits: %s
 Total Quota Mempry: %s
 Total Quota CPU : %s """ % ( str(round(tmemuage/1024)),
                              str(round(tmemreq/1024)),
                              str(round(tmemlimit/1024)),
                              str(round(tcpuusage/1000)),
                              str(round(tcpurequests/1000)),
                              str(round(tcpulimits/1000)),
                              str(round(tmemquotas)),
                              str(round(tcpuquotas)))
    print("values are approximate and rounded")
    print(s)

with open('cluster_usage.csv', mode='a') as usage_file:
              usage_writer = csv.writer(usage_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
              usage_writer.writerow(["Total", round(tmemuage/1024), round(tmemreq/1024), round(tmemlimit/1024), round(tcpuusage/1000), round(tcpurequests/1000), round(tcpulimits/1000), round(tmemquotas), round(tcpuquotas) ])





