import subprocess

print("MyMacChanger started!")

interface = "eth0"
mac_address = "00:22:33:77:99:11"

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
subprocess.call(["ifconfig", interface, "up"])
