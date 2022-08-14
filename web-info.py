import whois
domain_name = input("Enter the url:")
whois_info = whois.whois(domain_name)
print("Domain registrar:", whois_info.registrar)
print("WHOIS server:", whois_info.whois_server)
print("Domain creation date:", whois_info.creation_date)
print("Expiration date:", whois_info.expiration_date)
print(whois_info)