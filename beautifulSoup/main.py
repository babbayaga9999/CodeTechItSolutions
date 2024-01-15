import requests

def parseAndSave(url, path) :
    r = requests.get(url)
    with open(path, "w") as f:
        f.write(r.text)

url  = "https://www.booking.com/index.en-gb.html?label=gen173nr-1BCAEoggI46AdIM1gEaGyIAQGYAQm4ARnIAQzYAQHoAQGIAgGoAgO4Arb9iK0GwAIB0gIkYTc1NzJmZTUtYjE5MS00YzVlLThiNWYtZDg4ZjBlNDk2N2Fl2AIF4AIB&sid=139fd86ae0f36c8bac8707dcf971cb09&keep_landing=1&sb_price_type=total&"     
parseAndSave(url,"data/Booking.html")    