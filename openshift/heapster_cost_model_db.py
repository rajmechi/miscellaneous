import json
import requests
#disable insecure certificate warning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#data base
import mysql.connector

#change below vars
ocpurl = "https://<URL>"
ocpuullistns = ocpurl + ":443/api/v1/namespaces"
headers = {"Authorization": "Bearer <TOKEN>"}

test = requests.get(ocpuullistns, headers=headers, verify=False).json()
rtoutjson = json.dumps(test, indent = 4)
rtoutjsonload = json.loads(rtoutjson)
#find the jason array length for list of projects
numprojects = len(rtoutjsonload['items'])
i = 0
#print("Total Number of Projects are  " + str(numprojects))
#loop through all namespaces

#open connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="<PASS>",
  database="metrics"
)
mycursor = mydb.cursor()

while i < numprojects:
    #print(rtoutjsonload['items'][i]['metadata']['name'])
    try:
      urlnew =  ocpurl + ":443/api/v1/namespaces/openshift-infra/services/https:heapster:/proxy/api/v1/model/namespaces/" + rtoutjsonload['items'][i]['metadata']['name'] + "/metrics/memory/usage" 
      #print(urlnew)
      getmemusage = requests.get(urlnew, headers=headers, verify=False).json()
      getmemusagetojson = json.dumps(getmemusage,  indent = 4)
      getmemusagetojsonload =  json.loads(getmemusagetojson)
      #print(getmemusagetojsonload)
      lastonelen = len(getmemusagetojsonload['metrics'])-1
      #numtimestamplen = len(getmemusagetojsonload['metrics'])
      #print("Memory usage in Mebibyte of " + rtoutjsonload['items'][i]['metadata']['name'] + " is " + str(getmemusagetojsonload['metrics'][0]['value']/1.049e+6))
      print("Memory usage in Megabyte of " + rtoutjsonload['items'][i]['metadata']['name'] + " is " + str(getmemusagetojsonload['metrics'][lastonelen]['value']/1000000))
      #print("tried this for namespace $s hello" %(rtoutjsonload['items'][i]['metadata']['name']))
      #Add new namespaces
      namespace_add = "INSERT IGNORE INTO costmodel (namespace,memusage) VALUES ('" + rtoutjsonload['items'][i]['metadata']['name'] + "',0)"
      mycursor.execute(namespace_add)
      #perm solution
      #mycursor.execute("INSERT IGNORE INTO costmodel (namespace) VALUES (%s)",(rtoutjsonload['items'][i]['metadata']['name']))   
      mydb.commit()
      #update memory value
      update_pre = "UPDATE costmodel SET memusage= CASE WHEN memusage<" + str(getmemusagetojsonload['metrics'][lastonelen]['value']/1000000) + " THEN " + str(getmemusagetojsonload['metrics'][lastonelen]['value']/1000000) + " ELSE memusage END WHERE namespace='" + rtoutjsonload['items'][i]['metadata']['name'] + "'"
      mycursor.execute(update_pre)
      mydb.commit()
      #print(update_pre)

      #print(get_previous_value)
      #mycursor.execute(get_previous_value)
      

    except:
      print("Something else went wrong for namespace " + rtoutjsonload['items'][i]['metadata']['name'] )
    i += 1
