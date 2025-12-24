# MyMacChanger

MyMacChanger is a simple **Python-based MAC address changer** that allows users to modify the MAC address of a specified network interface.

This tool is commonly used in **network security testing, privacy protection, and lab environments** where MAC address spoofing is required.  
The script safely brings the interface down, applies the new MAC address, brings it back up, and verifies whether the change was successful.

> ⚠️ **Disclaimer**  
> This tool is intended **only for educational purposes, security labs, and authorized environments**.  
> Changing your MAC address without permission may violate network policies or local laws.

---

## Features

- Change the MAC address of a specified network interface
- Verifies and confirms the new MAC address
- Simple command-line interface
- Uses only Python standard libraries

---

## Requirements

- Python 3.x
- Linux-based operating system
- Root / sudo privileges (required to modify network interfaces)

> The script uses `subprocess` and `optparse`, both included in the Python standard library.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/okntscgl/MyMacChanger.git
cd MyMacChanger
No additional dependencies are required.

Usage
Run the script with the target interface and desired MAC address:

bash
python MyMacChanger.py -i <interface> -m <new_mac_address>
Parameters
-i, --interface
Network interface to modify (e.g. eth0, wlan0)

-m, --mac
New MAC address in the format XX:XX:XX:XX:XX:XX

Example
Change the MAC address of wlan0 to 00:11:22:33:44:55:

bash
python MyMacChanger.py -i wlan0 -m 00:11:22:33:44:55
How It Works
User Input
The script parses command-line arguments to identify the interface and new MAC address.

Interface Control
Using the subprocess module, the script:

Brings the interface down

Applies the new MAC address

Brings the interface back up

Verification
The script checks the interface configuration output using regular expressions to confirm that the MAC address was successfully changed.

Feedback
A success or error message is displayed based on the verification result.

Project Structure
graphql
Kodu kopyala
.
├── MyMacChanger.py   # Main MAC changer script
├── README.md        # Project documentation
Security Notes
MAC address spoofing is commonly used in:

Wireless security testing

Network anonymity experiments

Penetration testing labs

Modern networks may detect MAC changes using:

Network Access Control (NAC)

DHCP fingerprinting

Behavioral monitoring

Understanding how MAC spoofing works is essential for both offensive and defensive security.

Contributing
Contributions are welcome.
Please open an issue or submit a pull request, and discuss changes before making major modifications.

License
This project is licensed under the MIT License.
See the LICENSE file for details.
