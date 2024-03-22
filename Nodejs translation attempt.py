import time
import json
import hmac
import requests

# const http = require('https')

# crypto = require('crypto')

username = 'leeyuchen0926'
password = 'centagateYUCHEN2021'
integrationKey = '4ce567344b15aaa597c23afe1005edc2c89256bac199d1af9eea81812626e829'

userAgent = ''
supportFido = ''
browserFp = ''
ipAddress = ''

unixTimestamp = str(round(time.time()))

secretKey = 'ZmuPThp19e79'
algorithm = 'sha256'
hmacText = username + password + userAgent + integrationKey + supportFido + browserFp + unixTimestamp + ipAddress

# generate HMAC value
hm=hmac.new(secretKey.encode(),hmacText.encode(),digestmod=algorithm)
hashh=hm.hexdigest()



#JSON
data = {"username" : username,
        "password" : password,
        "userAgent" : userAgent,
        "integrationKey" : integrationKey,
        "supportFido" : supportFido,
        "browserFp" : browserFp,
        "unixTimestamp" : unixTimestamp,
        "ipAddress" : ipAddress,
        "hmac" : hashh
        }


data_jsonStr=json.dumps(data)


# REST API
# https://realpython.com/api-integration-in-python/


options = { "hostname" : "console.centagatecloud.com",
            "port" : 443,
            "path" : '/v2/CentagateWS/webresources/auth/authBasic',
            "method" : 'POST',
            "headers" : {
                    'Accept' : 'application/json',
                    'Content-Type' : 'application/json',
                        }
            }

url = "https://cloud.centagate.com/v2/CentagateWS/webresources/auth/authBasic"

req = requests.post(url,data=data_jsonStr,headers=options["headers"])

print("Status code : ",req.status_code)
print(dir(req),"\n\n")
print(req.__attrs__,'\n\n')
print(req._content)





'''
req2 = requests.get(url)

print(req2.status_code)
req2.json()

'''




