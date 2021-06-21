#!/bin/bash
namespacename=$1
pod_name=$2

#check if pod exist
oc project $namespacename
ifpodexist=$(oc get pod $2 -n $1 | grep Running | awk '{ print $3}')
echo $ifpodexist
podstatus=Running
if [[ "$podstatus" == $ifpodexist ]]; then
  echo "Pod exist"
else
  echo "pod not exist or Running. exiting"
  exit 1
fi

# delete temp files
rm -rf roots.pem cleaned-roots.pem index.crt parsed-remote-or-local-certs.pem listoffingerprintsfromjava.out cacertsfrompod

#get remote certificates to be compared with
#wget https://pki.goog/roots.pem
curl -o  roots.pem https://pki.goog/roots.pem
sed -ne "/-----BEGIN CERTIFICATE-----/,/-----END CERTIFICATE-----/p" roots.pem  > cleaned-roots.pem
certcount=$(grep -e "-----BEGIN CERTIFICATE-----" cleaned-roots.pem | wc -l)
for index in $(seq 1 $certcount); do
    #echo "======== cert $index"
    awk "/-----BEGIN CERTIFICATE-----/{i++}i==$index" cleaned-roots.pem > index.crt
    openssl x509 -noout -fingerprint -sha256 -inform pem -in index.crt >> parsed-remote-or-local-certs.pem
    #openssl x509 -in index.crt -text -noout | grep -E "Subject:"
    rm index.crt
done
sed -i -e 's/SHA256 Fingerprint=//g' parsed-remote-or-local-certs.pem
#echo "testtest" >> parsed-remote-or-local-certs.pem

#compre root cert SHAs with java
#cp /etc/pki/ca-trust/extracted/java/cacerts .
oc cp $pod_name:/etc/pki/ca-trust/extracted/java/cacerts cacertsfrompod
keytool -list -keystore cacertsfrompod -storepass changeit | grep "Certificate fingerprint" > listoffingerprintsfromjava.out

while read line
do
    if [[ ! -z $(grep "$line" listoffingerprintsfromjava.out) ]];
    then
      echo "FOUND: $line"
    else
      echo "NOT FOUND in POD: $line"
    fi
done < parsed-remote-or-local-certs.pem
