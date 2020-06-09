# _Fogwing IoT Simulator Program for Raspberry Pi using UDP protocol_
This directory provide two files that sends sample data over Fogwing IoTHub using UDP protocol.

**Note that these SDKs are currently in preview and are subject to change.**

## Fogwing IoT Simulation using UDP protocol
We have provided two files:
* [Fogwing_UDP_client_simulator.py]()
* [configuration.json]()

The logic behind the code is to send the sample data over Fogwing
IoTHub using UDP protocol.

### Step:1
#### Python & json file
* Copy all the files into your Rasberry Pi and 
  you are good to start ! You now finish with coding part.
  
### Step:2
#### Credentials
* Change the **client_id** and **dev_eui** with your Fogwing IoTHub access
  credentials in **configuration.json file**.  
  

### Step:3
#### Run and Get Started with Fogwing IoT
* Now run the file with the below command.
    ```
    python Fogwing_UDP_client_simulator.py
    ```
  **Note:-** Provided everything goes in line with the above mentioned instructions,
         you will be able to see a message that reads 'successfully published' in command line.

## Step:4
#### Start analyzing your data at Fogwing Platform
* Now you are ready to analyze your data at [Fogwing Platform](https://enterprise.fogwing.net/) portal,
  you can check all the data within the data storage in the portal.
  
 #### Getting help and finding Fogwing docs
 * [Fogwing Platform Forum]()
 * [Fogwing Platform Docs](https://docs.fogwing.io/)