import subprocess

# subprocess.call("ifconfig",shell=True)
# subprocess.call("sudo ifconfig wlan0 down",shell=True)
# subprocess.call("sudo ifconfig wlan0 hw ether 00:55:66:88:77:99",shell=True)
# subprocess.call("sudo ifconfig wlan0 up ",shell=True)

interface=input("Enter Interface : ")
new_mac=input("Enter New MAC : ")

print("Changing MAC Address "+interface+" To "+new_mac)
# subprocess.call("ifconfig "+ interface+" down",shell=True)
# subprocess.call("ifconfig "+interface+" hw ether "+new_mac,shell=True)
# subprocess.call("ifconfig "+interface+" up ",shell=True)


subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
subprocess.call(["ifconfig",interface,"up"])
