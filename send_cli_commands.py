# A simple script to connect to an esxi host and send some cli commands
#
# Author: Daryl Allen
#

import paramiko
import time

if __name__ == "__main__":
    print("Initial Connection")

    command = "net-stats -l"

    # Update the next three lines with your
    # server's information

    host = "172.17.0.56"
    username = "root"
    password = "VMware1!"

    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    _stdin, _stdout, _stderr = client.exec_command(command)
    time.sleep(.5)
    print(_stdout.read().decode())
    client.close()

