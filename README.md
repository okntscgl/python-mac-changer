MyMacChanger
MyMacChanger is a simple Python tool that allows users to change the MAC address of a specified network interface. This can be useful for network security testing, privacy protection, or bypassing network restrictions. The script handles the process of bringing down the interface, applying the new MAC address, and bringing the interface back online. It also verifies whether the change was successful.

Features
Change the MAC address of a given network interface.
Verifies and confirms the new MAC address.
Requirements
Python 3.x
subprocess and optparse modules (both are included with the Python standard library).
Installation
Clone this repository or download the project files:

bash
git clone https://github.com/okntscgl/MyMacChanger.git
Navigate to the project directory:

bash
cd MyMacChanger
Usage
To run the script, use the following command:

bash
python MyMacChanger.py -i <interface> -m <new_mac_address>
Parameters
-i, --interface: The network interface where you want to change the MAC address (e.g., eth0, wlan0).
-m, --mac: The new MAC address in the format XX:XX:XX:XX:XX:XX (e.g., 00:11:22:33:44:55).
Example
To change the MAC address of your wireless interface wlan0 to 00:11:22:33:44:55, run:

bash
python MyMacChanger.py -i wlan0 -m 00:11:22:33:44:55
How It Works
User Input: The get_user_input function gathers the network interface and new MAC address from the user.
MAC Address Change: The change_mac_address function uses the subprocess module to:
Bring the specified interface down.
Change the MAC address.
Bring the interface back up.
Verify MAC Address: The control_new_mac function confirms that the new MAC address has been applied correctly by using regular expressions to search the ifconfig output.
Notification: The script displays a success or error message based on whether the MAC address was updated successfully.
Contributing
To contribute, please submit an issue or pull request. Discuss potential changes before making them to ensure the project's direction is aligned with your contributions.

License
This project is licensed under the MIT License. Refer to the LICENSE file for details.

Disclaimer
Be aware that changing your MAC address may violate your network's terms of service or policies. Always use this tool responsibly and ensure you have the necessary permissions.
