import socket, nmap3, whois, time
def dns(ip):
    domain = socket.gethostbyaddr(ip)
    return(domain)

def nmap(ip):
    nmap = nmap3.Nmap()
    version_result = nmap.nmap_version_detection(ip)
    ports = nmap.scan_top_ports(ip)
    return(version_result, ports)

def whois(ip):
    domain = whois.query(ip)
    whois = domain.__dict__
    return(whois)
