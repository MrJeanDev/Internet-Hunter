import socket, python3_nmap, pyping, whois, scapy, time

def dns(ip)
    domain = socket.gethostbyaddr(ip)
    return(domain)

def nmap(ip):
    nmap = nmap3.Nmap()
    subdomains = {}
    subdomains = nmap.nmap_dns_brute_script(ip)
    version_result = nmap.nmap_version_detection(ip)
    ports = nmap.scan_top_ports(ip)
    return(subdomains, version_result, ports)

def traceroute(ip):
    print()

def ping(ip):
    ping = pyping.ping(ip)
    return(ping)

