# generic send commands script

from netmiko import ConnectHandler

def connect(host, username, password):
    print(f"Attempting connection to {host}")
    try:
        hostobj = ConnectHandler(host=host, device_type='generic', username=username, password=password)
        print('connected...')
        return hostobj
    except:
        print('Failed to connect. Quitting!')

    esxi_host = '172.17.0.56'
    password = 'VMware1!'
    username = 'root'

    net_connection = connect(esxi_host, username, password)

    response = net_connection.send_command("net-stats -l")

    print(response)
