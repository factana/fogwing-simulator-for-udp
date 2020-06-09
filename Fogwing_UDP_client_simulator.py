import socket
import json


def send_data_UDP(sample_data, hostAddress, port):

    global UDP_socket

    if 'Enter' in config['IoTHub_cred']['dev_eui']:
        print("Fogwing UDP Server: Enter dev_eui in configuration file")

    else:
        try:
            # Creating a UDP socket
            UDP_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except socket.error as err:
            print('Fogwing UDP Server: socket creation failed with error %s' % (err))
        print('Fogwing UDP Server: Socket successfully created.')

        try:

            # Get host_ip from host_address
            host_ip = socket.gethostbyname(hostAddress)

            # Connect socket to Fogwing UDP server
            UDP_socket.connect((host_ip, port))
            print("Fogwing UDP Server: The socket has successfully connected to Fogwing UDP server.")

            # Sample data getting from configuration file
            sample_data1 = json.dumps(sample_data['payload'], indent=4)
            print("Fogwing UDP Server: Sending... %s" % sample_data1)

            # Send data to Fogwing IoTHub using created UDP socket
            UDP_socket.send(str.encode(json.dumps(sample_data)))
            print('Fogwing UDP Server: Successfully Published.')

        except socket.gaierror:
            print('Fogwing UDP Server: There was an error resolving the host.')

        finally:
            UDP_socket.close()
            print("Fogwing UDP Server: Closing connection to the server.")


# Reading configuration file
with open('configuration.json', 'r') as file:
    config = json.load(file)

host_add = config['serverCredential']['hostAddress']
port = config['serverCredential']['port']
data = config['IoTHub_cred']


send_data_UDP(data, host_add, port)






