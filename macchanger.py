import subprocess
import optparse
import re

def figlet():
	print(" __  __               ____ _                                  ")
	print("|  \/  | __ _  ___   / ___| |__   __ _ _ __   __ _  ___ _ __ ")
	print("| |\/| |/ _` |/ __| | |   | '_ \ / _` | '_ \ / _` |/ _ \ '__|")
	print("| |  | | (_| | (__  | |___| | | | (_| | | | | (_| |  __/ |   ")
	print("|_|  |_|\__,_|\___|  \____|_| |_|\__,_|_| |_|\__, |\___|_|   ")
	print("                                           -by Akshat Pal")

def cmd_arguments_acceptor():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface", dest="interface", help="Interface to chage MAC")
	parser.add_option("-m", "--macaddr", dest="new_mac", help="New MAC")

	(options, arguments) = parser.parse_args()
	if not options.interface:
		parser.error("[!] Please specify an interface")
	if not options.new_mac:
		parser.error("[!] Please specify a MAC address")

	return (options.interface, options.new_mac)

(interface, mac) = cmd_arguments_acceptor()
def regexFunc():
	extr_mac = subprocess.check_output(["ifconfig", interface])
	get_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(extr_mac))
	print("Old MAC: ")
	print("Get mac: ", get_mac)
	
	return get_mac.group(0)

def mac_changer(interface, mac_addr):
	figlet()
	returnMac = regexFunc()	
	if returnMac:
		print("[+] Changing mac for ", interface)
		subprocess.call(["ifconfig", interface, "down"])
		subprocess.call(["ifconfig", interface, "hw", "ether", mac])
		subprocess.call(["ifconfig", interface, "up"])
		print("[+] Successfully changed MAC for", interface, "from" , returnMac, "to", mac)
	else:
		print("[!] Unable to read MAC of", interface)

mac_changer(interface, mac)
