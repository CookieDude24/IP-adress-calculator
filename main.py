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
    netmask = netaddr.IPNetwork(ip_with_bits).netmask
    net = netaddr.IPNetwork(ip_with_bits).network
    broadcast = netaddr.IPNetwork(ip_with_bits).broadcast
    set = netaddr.IPSet([f"{net}/{cidr}"])

    iprange = set.iprange()

    print("IP Addresse Binär: " + ip.bits())
    print("Subnetzmaske Binär: " + netmask.bits())

    print("Subnetzadresse: " + str(net))
    print("Subnetzmaske: " + str(netmask))
    print("Broadcastadresse: " + str(broadcast))

    print("Erster Host: " + str(netaddr.IPAddress(iprange.first+1)))
    print("Letzer Host: " + str(str(netaddr.IPAddress(iprange.last-1))))

