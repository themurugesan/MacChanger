
import subprocess
import re
import random
import os
def get_current_mac(interface):
    result = subprocess.run(['ifconfig', interface], capture_output=True, text=True)
    mac_address_search = re.search(r'ether (\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)', result.stdout)

    if mac_address_search:
        return mac_address_search.group(1)
    else:
        raise ValueError("Could not read MAC address")


def change_mac(interface, new_mac):
    subprocess.run(['sudo', 'ifconfig', interface, 'down'])
    subprocess.run(['sudo', 'ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.run(['sudo', 'ifconfig', interface, 'up'])


def generate_random_mac():
    mac = [0x00, 0x16, 0x3e,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: "%02x" % x, mac))


def main():
    interface = input("Enter the network interface (e.g., en0, eth0): ")
    current_mac = get_current_mac(interface)
    print(f"Current MAC Address: {current_mac}")

    new_mac = generate_random_mac()
    print(f"Changing MAC Address to: {new_mac}")
    change_mac(interface, new_mac)

    current_mac = get_current_mac(interface)
    print(f"New MAC Address: {current_mac}")


if __name__ == "__main__":
    main()