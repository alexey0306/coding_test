# Import section
import requests
import argparse
import re
import os
import json
from jsonschema import validate, ValidationError, SchemaError

# Response schema
response_schema = {
    "type": "object",
    "properties":{
        "vendorDetails": {
            "type": "object",
            "properties": {
                "companyName": {
                    "type": ["string"],
                    "minLength": 1
                }
            },
            "required": ["companyName"]
        }
    },
    "required": ['vendorDetails']
}

# Init section
REQUEST_URL = "https://api.macaddress.io/v1?output=json&search={}"
API_TOKEN = os.getenv("API_TOKEN","")

# Initialize the parser
parser = argparse.ArgumentParser()
parser.add_argument("-a","--address",help="MAC Address",required=True)
parser.add_argument("-o","--output",choices=["string","json","xml"],default="string",help="Output format")

# Parsing the args
args = parser.parse_args()

# Checking the MAC address format using REGEX
p = re.compile(r'(?:[0-9a-fA-F]:?){12}')
matches = re.findall(p,args.address)
if not matches:
    print("\n  >> [ERROR]: Incorrect MAC address\n")
    exit()

# Sending request
headers = {"X-Authentication-Token": API_TOKEN}
response = requests.get(REQUEST_URL.format(args.address),headers=headers)
if response.ok == False:
    print("\n  >> [ERROR]: Request failed. Status code={}, Error={}\n".format(response.status_code,response.text))
    exit()

# Processing the response
result = response.json()

try:
    validate(result,schema=response_schema)
except (ValidationError, SchemaError) as e:
    print("\n  >> [ERROR]: Incorrect response: {}\n".format(e.message))
    exit()

if args.output == "json":
    print(json.dumps({
        "name": result['vendorDetails']['companyName']
    }))
elif args.output == "xml":
    print('<?xml version="1.0" encoding="UTF-8"?><company>{}</company>'.format(result['vendorDetails']['companyName']))
else:
    print(result['vendorDetails']['companyName'])
