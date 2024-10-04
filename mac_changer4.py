import subprocess
import optparse
import re

def get_user_input():

    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", help="interface to change!")
    parse_object.add_option("-m", "--mac", dest="mac_address", help="new mac address")

    return parse_object.parse_args()

def change_mac_address(user_interface, user_mac_address):

    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_address])
    subprocess.call(["ifconfig", user_interface, "up"])

def control_new_mac(interface):

    ifconfig = subprocess.check_output(["ifconfig", interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))

    if new_mac:
        return new_mac.group(0)
    else:
        return None

print("MyMacChanger started!")

(user_input, arguments) = get_user_input()
change_mac_address(user_input.interface, user_input.mac_address)
finalized_mac = control_new_mac(str(user_input.interface))

if finalized_mac == user_input.mac_address:
    print("Success!")

else:
    print("Error!")




#After copying the place you want to find in Linux to regex101, you check the commands there on the regex101.com site to see what you want to find, and then you write those commands here using the re library.
#Since we adapted it to Python3 for the string, we converted it - you can see these errors when you run it in the terminal.
