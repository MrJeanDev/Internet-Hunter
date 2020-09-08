#codinng: utf-8
from sys import argv
import geoip3
import data
import web2
import os
import ip2
#import threading talvez update futuro
import relatorio

inicialização = (argv[0],argv[1])

decisão = {
        1 :"Analise Web",
        2 :"Analise Ip",
        3 :"Rastreamento Ip"
    }

def web():
    print("-" * 20)
    web1 = input("Digite o site. Sera melhor sem .www e sem espaço\nSite: ")
    print("-" * 20)

    print("Analisando o site. Espere um pouco")
    web_service = web2.web_service(web1)
    print("[X]Web Service")
    whois = web2.whois(web1)
    print("[X]Whois")
    ip_addr, subdomain = web2.dns(web1)
    print("[X]IP\n[X]Subdomains")
    web_on = web2.web_on(web1)
    print("[X]Web On")
    relato = data.web(web_service,whois,ip_addr,web_on)

    print("-" * 20)
    relato_decisão = input("Quer um 'relatorio'? Escreve Y\nSe não apenas só apenas aperte enter: ")
    print("-" * 20)
    if relato_decisão == "Y" or "y":
        relatorio.relatorio_web(relato, user)
    else:
        print("Adeus, e obrigado por usar o programa")

def ip():
    print("-" * 20)
    ip1 = input("Digite seu ip: ")
    print("-" * 20)

    print("Analisando o Ip")
    version_result = ip2.nmap(ip1)
    whois = ip2.whois(ip1)
    print("[X]Portas\n[X]Resultado das versões")
    dns = ip2.dns(ip1)
    print("[X]Dns Resolve")
    relato = data.ip(version_result, whois, dns)

    print("-" * 20)
    relato_decisão = input("Quer um 'relatorio'? Escreve Y\nSe não apenas só apenas aperte enter: ")
    print("-" * 20)
    if relato_decisão == "Y" or "y":
        relatorio.relatorio_web(relato, user)
    else:
        print("Adeus, e obrigado por usar o programa")

def geoip():
    print("-" * 20)
    geoip = input("Digite o ip: ")
    print("-" * 20)

    country,state,city,postal_code,latitude,longitude = geoip3.city(geoip)

    relato = data.geoip(city, country, latitude, longitude, postal_code)
    print()
    relato_decisão = input("Quer um 'relatorio'? Escreve Y\nSenão apenas só apenas aperte enter")
    print("-" * 20)
    if relato_decisão == "Y" or "y":
        relatorio.relatorio_geoip(relato,user)
    else:
        print("Obrigado por usar o programa")

def Options(user,opt):

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
        print("-" * 20)
        user = input("Digite nome de usuario\nName: ")
        print("-" * 20)
        opt = int(input("1. Analise web.\n2. Analise ip\n3. Geoip\ndigite o numero: "))
        Options(user,opt)
