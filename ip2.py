import socket, nmap3, whois, scapy, time

def dns(ip):
    domain = socket.gethostbyaddr(ip)
    return(domain)

def nmap(ip):
    nmap = nmap3.Nmap()
    version_result = nmap.nmap_version_detection(ip)
    ports = nmap.scan_top_ports(ip)
    return(subdomains, version_result, ports)

def traceroute(ip):
    print()

def whois(ip):
    domain = whois.query(ip)
    whois = domain.__dict__
    return(whois)

def ping(ip):
    packet = IP(dst=ip + str(ip), ttl=64)
    reply = sr1(packet)
    if ip in reply.src:
         return(True)
    else:
        return(False)
