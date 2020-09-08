from geoip2.database import Reader

def city(geoip):
    with Reader('./Databases/GeoLite2-City.mmdb') as reader:
        response = reader.city(geoip)
        country = response.country.name
        state = response.subdivisions.most_specific.name
        city = response.city.name
        postal_code = response.postal.code
        latitude = response.location.latitude
        longitude = response.location.longitude
        return(country,state,city,postal_code,latitude,longitude)
'''
def domain(geoip):
    with Reader('/Database/GeoIP2-Domain.mmdb') as reader:
        response = reader.domain(geoip)
        domain = response.domain
        return(domain)
def anonymous(geoip):
    with Reader('./Database/GeoIP2-Anonymous-IP.mmdb') as reader:
        response = reader.anonymous_ip(geoip)
        anonymous = response.is_anonymous
        return(anonymous)

def anonymous_True(geoip):
    with Reader('/path/to/GeoIP2-Anonymous-IP.mmdb') as reader:
        response = reader.anonymous_ip(geoip)
        vpn = response.is_anonymous_vpn
        hosting = response.is_hosting_provider
        proxy = response.is_public_proxy
        tor = response.is_tor_exit_node
        if vpn == True:
            return("VPN")
        elif hosting == True:
            return("HOSTING")
        elif proxy == True:
            return("PROXY")
        else:
            return("TOR")
'''
