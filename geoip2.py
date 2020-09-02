import geoip2

def exec(geoip):
    with geoip2.database.Reader('/path/to/GeoLite2-City.mmdb') as reader:
        response = reader.city(geoip)
        country = response.country.name
        state = response.subdivisions.most_specific.name
        city = response.city.name
        postal_code = response.postal.code
        latitude = response.location.latitude
        longitude = response.location.longitude

    with geoip2.database.Reader('/path/to/GeoIP2-Domain.mmdb') as reader:
        resposta = leutura.domain(geoip)
        domain = response.domain
    
    with geoip2.database.Reader('/path/to/GeoIP2-Anonymous-IP.mmdb') as reader:
        resposta = reader.anonymous_ip(geoip)
        anonymous = response.is_anonymous


    return(city, country, anonymous,latitude, longitude, domain, postal_code)
