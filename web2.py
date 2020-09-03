import socket, whois, nmap3

def dns(web):
    ip_addr = socket.gethostbyname(web)
    subdomains = nmap.nmap_dns_brute_script(ip)
    return(ip_addr, subdomains)

def web_on(web):
    ip = socket.gethostbyname(web), 80
    try:
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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

    except:
        print("Deu algo errado, deseja pular? Digita enter.\nSe não. escreve Y e aperte enter")
def web_service(web):
    nmap = nmap3.Nmap()
    version_result = nmap.nmap_version_detection(ip)
    return(version_result)

def whois(web):
    domain = whois.query(web)
    whois = domain.__dict__
    return(whois)
