# usr/bin/ env python
import scapy.all as scapy
import cryptography

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    # arp_request.show()
    # print(arp_request.summary())
    # broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast = scapy.Ether(dst="88:b4:a6:1d:4d:77")
    broadcast.show()
    # print(broadcast.summary())
    #  scapy.ls(scapy.Ether())  #list of all ip commands
    arp_request_broadcast = broadcast/arp_request
    # arp_request_broadcast.show()
    # print(arp_request_broadcast.summery())
    answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout = 5 )[0]
    print(answered_list.summary())
    for element in answered_list:
        print(element)
        print("------------------------------------------------------------------------------")

scan("10.0.2.1/24")
