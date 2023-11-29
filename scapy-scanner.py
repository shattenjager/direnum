from scapy.all import *

interface = "<NET>" # eth0, eth1, lun0 etc.
ip_range = "NN.NN.X.X/24" # E.g.: 192.168.X.X/24
broadcastMac = "ff:ff:ff:ff:ff:ff"

packet = Ether(dst=broadcastMac)/ARP(pdst = ip_range) 

ans, unans = srp(packet, timeout =2, iface=interface, inter=0.1)

for send,receive in ans:
        print (receive.sprintf(r"%Ether.src% - %ARP.psrc%"))     