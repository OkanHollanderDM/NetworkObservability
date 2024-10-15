from scapy.all import *
from scapy.layers.dns import DNS, DNSQR, DNSRR
from scapy.layers.inet import IP, ICMP, UDP

host = "1.1.1.1"

# ICMP test
send(IP(dst=host) / ICMP())

response = sr1(IP(dst=host) / ICMP())

# DNS test
response = sr1(IP(dst=host) / UDP() / DNS(rd=1, qd=DNSQR(qname="www.example.org")))
response.show()
response[DNSRR].rdata
