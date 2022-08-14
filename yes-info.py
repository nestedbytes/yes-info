# Import packages
import whois
import typer
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

# about
@app.command()
def about():
    print("Get info for osint ! GitHub: https://github.com/shourgamer2/yes-info")

@app.command()
def credit():
    print("Written by shourgamer2 | Website: https://shourgamer2.tk/ | ")
# Run
if __name__ == "__main__":
    app()