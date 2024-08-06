import netaddr
import math

from netaddr.ip import IPNetwork

selection = input("Subnetzteiler oder IP Info Rechner [1/2]: ")

if selection == "1":
    netip = input("IP Address: ")
    cidr = input("CIDR: ")
    n = input("Anzahl Subnetze: ")

    network = f"{netip}/{cidr}"

    log_of_n = math.ceil(math.log(int(n), 2))
    cidr = int(cidr) + log_of_n

    net = IPNetwork(network)
    subnets = list(net.subnet(cidr))

    i = 0
    print("Nr.  Subnetz        Maske         1. Host     Letzer Host     Broadcast")
    for subnets in subnets:
        i += 1
        print(str(i) + "  " + str(subnets.ip) + "  " + str(subnets.netmask) + "  " + str(netaddr.IPAddress(subnets.first + 1)) + "  " +
               str(netaddr.IPAddress(subnets.last - 1)) + "  " + str(subnets.broadcast))

elif selection == "2":
    ip = input("IP Address: ")
    cidr = input("CIDR: ")

    ip_with_bits = f"{ip}/{cidr}"

    net = netaddr.IPNetwork(ip_with_bits).network
    iprange = netaddr.IPSet([f"{net}/{cidr}"]).iprange()

    print("IP Addresse Binär: " + netaddr.IPAddress(ip).bits())
    print("Subnetzmaske Binär: " + netaddr.IPNetwork(ip_with_bits).netmask.bits())

    print("Subnetzadresse: " + str(net))
    print("Subnetzmaske: " + str(netaddr.IPNetwork(ip_with_bits).netmask))
    print("Broadcastadresse: " + str(netaddr.IPNetwork(ip_with_bits).broadcast))

    print("Erster Host: " + str(netaddr.IPAddress(iprange.first + 1)))
    print("Letzer Host: " + str(str(netaddr.IPAddress(iprange.last - 1))))
