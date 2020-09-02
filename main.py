#codinng: utf-8
from sys import argv
import geoip3
import web2
import os
import ip2
#import threading
import relatorio

inicialização = (argv[0],argv[1])
decisão = {
        1 :"Analise Web",
        2 :"Analise Ip",
        3 :"Rastreamento Ip"
    }

def ip():
    try:
        ip1 = input("Digite seu ip")

        ping = ip2.ping(ip1)
        traceroute = ip2.traceroute(ip1)
        subdomains, version_result, ports = ip2.nmap(ip1)
        dns = ip2.dns(ip1)

        relatorio.relatorio_ip(user)
    except:
        print("Digitou ip errado, escreve denovo")
        ip()

def web():
    web1 = input("Digite o site. Sera melhor sem .www")
    web_service = web2.web_service(web)
    crimeflaredb = web2.crimeflaredb(web)
    whois = web2.whois(web)
    ip_addr = web2.dns(web)
    maxmind = web2.maxmind(web)
    relatorio.relatorio_web(user)

def geoip():
    geoip = input("Digite o ip")
    city, country, anonymous, latitude, longitude, domain, postalcode = geoip3.exec(geoip)
    relatorio.relatorio_geoip(user)

def Options(user,opt):
    print()
    print("-" * 20)
    print("\nBem vindo {}!\n".format(user))
    print("-" * 20)
    
    if opt in decisão:
        decis = decisão[opt]
        print('''
                   ,ood8888booo,
                ,od8           8bo,
             ,od                   bo,
           ,d8                       8b,
          ,o                           o,    ,a8b
         ,8                             8,,od8  8
         8'                             d8'     8b
         8                           d8'ba     aP'
         Y,                       o8'         aP'
          Y8,                      YaaaP'    ba
           Y8o                   Y8'         88
            `Y8               ,8"           `P
              Y8o        ,d8P'              ba
         ooood8888888P"""'                  P'
      ,od                                  8
   ,dP     o88o                           o'
  ,dP          8                          8
 ,d'   oo       8                       ,8
 $    d$"8      8           Y    Y  o   8
d    d  d8    od  ""boooooooob   d"" 8   8
$    8  d   ood' ,   8        b  8   '8  b
$   $  8  8     d  d8        `b  d    '8  b
 $  $ 8   b    Y  d8          8 ,P     '8  b
 `$$  Yb  b     8b 8b         8 8,      '8  o,
      `Y  b      8o  $$o      d  b        b   $o
       8   '$     8$,,$"      $   $o      '$o$$
       $o$$P"                 $$o$
        ''')
        if opt == 1:
            web()

        elif opt == 2:
            ip()
        else:
            geoip()
for iniciar in inicialização:
    if iniciar == "run":
        user = input("\nDigite nome de usuario\nName: ")
        print()
        opt = int(input("1. Analise web.\n2. Analise ip\n3. Geoip\ndigite o numero: "))
        Options(user,opt)
