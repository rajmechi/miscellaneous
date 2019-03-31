import json
import requests
#disable insecure certificate warning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#change below vars
ocpurl = "https://xxx.yyy.com"
ocpuullistns = ocpurl + ":443/api/v1/namespaces"
headers = {"Authorization": "Bearer xxxxxxxxxxx"}

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
    try:
      urlnew =  ocpurl + ":443/api/v1/namespaces/openshift-infra/services/https:heapster:/proxy/api/v1/model/namespaces/" + rtoutjsonload['items'][i]['metadata']['name'] + "/metrics/memory/usage"
      #print(urlnew)
      getmemusage = requests.get(urlnew, headers=headers, verify=False).json()
      getmemusagetojson = json.dumps(getmemusage,  indent = 4)
      getmemusagetojsonload =  json.loads(getmemusagetojson)
      #numtimestamplen = len(getmemusagetojsonload['metrics'])
      print("Memory usage in Mebibyte of " + rtoutjsonload['items'][i]['metadata']['name'] + " is " + str(getmemusagetojsonload['metrics'][0]['value']/1.049e+6))
      print("Memory usage in Megabyte of " + rtoutjsonload['items'][i]['metadata']['name'] + " is " + str(getmemusagetojsonload['metrics'][0]['value']/1000000))
    except:
      print("Something else went wrong for namespace " + rtoutjsonload['items'][i]['metadata']['name'] )
    i += 1
