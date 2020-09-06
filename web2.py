def dns(target):
    from socket import gethostbyname
    from nmap3 import Nmap , NmapScanTechniques
    nmap = Nmap()
    ip_addr = gethostbyname(target)
    subdomains = nmap.nmap_dns_brute_script(target)
    return(ip_addr, subdomains)

def web_on(target):
    from socket import gethostbyname, socket
    ip = gethostbyname(target), 80
    tcp = socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.connect(ip)
    msg = b"GET / HTTP/1.1\nHost: developer.mozilla.org\n\r\n\r"
    tcp.send(msg)
    response = str(tcp.recv(1024))
    print(oi)
    if response.find('1.1 404') >= 2:
        print("Site ou pagina não encontrado\n")
        result = False
        return(result)
    elif response.find('1.1 200') >= 2:
        print("Site encontrado\n")
        result = True
        return(result)
    else:
        print("Algo errado na url, mas servidor do site responde normalmente\n")
        result = True
        return(result)
def web_service(target):
    from nmap3 import Nmap
    nmap = Nmap()
    version_result = nmap.nmap_version_detection(target)
    return(version_result)

def whois(target):
    from whois import whois
    whois1 = whois(target)
    return(whois1)
