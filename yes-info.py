# Import packages
import whois
import typer
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
# Initialize
app = typer.Typer()
# whous-url
@app.command()
def whois_url(url: str):
    


    whois_info = whois.whois(url)
    print("Domain registrar:", whois_info.registrar)
    print("WHOIS server:", whois_info.whois_server)
    print("Domain creation date:", whois_info.creation_date)
    print("Expiration date:", whois_info.expiration_date)
    print(whois_info)
@app.command()
def phone(nbr: int):
    phonenbr = phonenumbers.parse(nbr)
    print("The location of this phone number is:")
    print(geocoder.description_for_number(nbr,'en'))
    print("The operator is:")   
    print(carrier.name_for_number(phonenbr,
                              'en')) 
# about
@app.command()
def about():
    print("Get info for osint ! GitHub: https://github.com/shourgamer2/yes-info")

@app.command()
def credit():
    print("Written by shourgamer2 | Website: https://shourgamer2.tk/ | GitHub: https://github.com/shourgamer2")
# Run
if __name__ == "__main__":
    app()