# Introduction
This script is used to query the information about specific MAC Address from the https://macaddress.io site.

# Running the script
Script has two parameters: 
* -a / --address - MAC address, Mandatory parameter
* -o / --output - The output format

To see the list of available options, type: 
```
python run.py --help
```
API Token should be stored in the Environment variable **API_TOKEN**

So, the script can be run like the following: 
```
export API_TOKEN=<YOUR_API_TOKEN>
python run.py --address <MAC_ADDRESS> --output json
```
