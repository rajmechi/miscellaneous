pod_name=airport-auth-api-150-l5qkn
# get all root certs SHAs
rm -rf rootpemshas.pem
rm -rf roots.pem
rm -rf listoffingerprintsfromjava.out
rm -rf cacerts

#wget https://pki.goog/roots.pem
curl -o  roots.pem https://pki.goog/roots.pem
sed -ne "/-----BEGIN CERTIFICATE-----/,/-----END CERTIFICATE-----/p" roots.pem  > allcerts.pem
certcount=$(grep -e "-----BEGIN CERTIFICATE-----" allcerts.pem | wc -l)
for index in $(seq 1 $certcount); do
    #echo "======== cert $index"
    awk "/-----BEGIN CERTIFICATE-----/{i++}i==$index" allcerts.pem > index.crt
    openssl x509 -noout -fingerprint -sha256 -inform pem -in index.crt >> rootpemshas.pem
    #openssl x509 -in index.crt -text -noout | grep -E "Subject:"
    rm index.crt
done
sed -i -e 's/SHA256 Fingerprint=//g' rootpemshas.pem

#compre root cert SHAs with java
#cp /etc/pki/ca-trust/extracted/java/cacerts .
oc cp $pod_name:/etc/pki/ca-trust/extracted/java/cacerts cacerts
keytool -list -keystore cacerts -storepass changeit | grep "Certificate fingerprint" > listoffingerprintsfromjava.out

while read line
do
    if [[ ! -z $(grep "$line" listoffingerprintsfromjava.out) ]];
    then
      echo "FOUND: $line"
    else
      echo "NOT FOUND: $line"
    fi
done < rootpemshas.pem
