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

# Running the script in Docker container
To run script in the Docker container please do the following:  
1. Clone the repo
2. Build the image
   ```
      cd coding_test/
      sudo docker build -t coding_test .
   ```
3. Run the container:
   ```
   sudo docker run -d -e API_TOKEN=<YOUR_API_TOKEN> coding_test
   sudo docker exec -it <container_id> /bin/bash
   cd /srv/app
   python run.py --address <MAC_ADDRESS> --output json 
   ```
