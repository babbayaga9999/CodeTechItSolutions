import requests

from bs4 import BeautifulSoup

with open("Booking.html", "r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc,'html.parser')
print(soup.prettify())
print(soup.title.string)
print(soup.find_all("div")[0])

"""for link in soup.find_all("a") :
    print(link.get("href"))
print(link.get_text())"""