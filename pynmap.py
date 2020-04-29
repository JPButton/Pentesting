import nmap
import sys
import socket

if len(sys.argv)<2:
    print ("Usage: pynmap.py targetip\n")
    exit(1)

target = str(sys.argv[1])
ports = [21,22,53,80,139,443,445,8080]

scan_v = nmap.PortScanner()

print("\nScanning",target,"for ports 21,22,53,80,139,443,445 and 8080...\n")

for port in ports:
    portscan = scan_v.scan(target,str(port))
    print("Port",port," is ",portscan["scan"][target]["tcp"][port]["state"])

print("\nHost",target," is ",portscan["scan"][target]["status"]["state"])

