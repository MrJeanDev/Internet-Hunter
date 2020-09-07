def web(web_service,whois,ip_addr,web_on):
    print(web_service)
    print("-" * 20)
    print(whois)
    print("-" * 20)
    print(ip_addr)
    print("-" * 20)
    print(web_on)

def ip(version_result, whois, dns):
    print(version_result)
    print("-" * 20)
    print(whois)
    print("-" * 20)
    print(dns)

def geoip(city, country, latitude, longitude, postalcode):
    print("Cidade: {}".format(city))
    print("-" * 20)
    print("País: {}".format(country))
    print("-" * 20)
    print("Latitude: {}".format(latitude))
    print("-" * 20)
    print("Longitude: {}".format(longitude))
    print("-" * 20)
    print("Postal Code: {}".format(postalcode))
    print("-" * 20)
