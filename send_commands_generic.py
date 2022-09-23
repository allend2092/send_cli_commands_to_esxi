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

def send_command(server_connection, cli_command):
    resp = server_connection.send_command(cli_command)
    return resp


if __name__ == "__main__":
    esxi_host = '172.17.0.56'
    username = 'root'
    password = 'VMware1!'

    net_connection = connect(esxi_host, username, password)

    response1 = send_command(net_connection, "net-stats -l")
    response2 = send_command(net_connection, "esxcfg-vmknic -l")

    print(response1)
    print()
    print(response2)
