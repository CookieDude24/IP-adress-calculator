import netaddr
import math

from netaddr.ip import IPNetwork

selection = input("Subnetzteiler oder IP Info Rechner [1/2]: ")

if selection == "1":
    netip = input("IP Address: ")
    cidr = input("CIDR: ")
    n = input("Anzahl Subnetze: ")

    network = f"{netip}/{cidr}"

    log_of_n = math.ceil(math.log(int(n),2))
    cidr = int(cidr) + log_of_n

    net = IPNetwork(network)
    subnets = list(net.subnet(cidr))

    i = 0
    for subnets in subnets:
        i+=1
        print(str(i) + ". Subnetz: " + str(subnets.ip) + " Maske: " + str(subnets.netmask) + " 1. Host: " +
              str(netaddr.IPAddress(subnets.first+1)) +" letzer Host: " + str(netaddr.IPAddress(subnets.last-1)) +
              " Broadcast: " + str(subnets.broadcast))



elif selection == "2":
    ip = input("IP Address: ")
    cidr = input("CIDR: ")

    ip_with_bits = f"{ip}/{cidr}"

    ip = netaddr.IPAddress(ip)
