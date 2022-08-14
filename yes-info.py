import whois
import typer

app = typer.Typer()


@app.command()
def whois_url(url: str):
    


    whois_info = whois.whois(url)
    print("Domain registrar:", whois_info.registrar)
    print("WHOIS server:", whois_info.whois_server)
    print("Domain creation date:", whois_info.creation_date)
    print("Expiration date:", whois_info.expiration_date)
    print(whois_info)


@app.command()
def about():
    print("Get info for osint ! GitHub: https://github.com/shourgamer2/yes-info")
if __name__ == "__main__":
    app()