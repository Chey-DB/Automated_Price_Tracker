import requests
import smtplib
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

# Constants
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")



USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
ACCEPT_LANGUAGE = "en-GB,en-US;q=0.9,en;q=0.8"

headers = {"user-agent": USER_AGENT, "accept-language": ACCEPT_LANGUAGE}
url = os.getenv("URL")

response = requests.get(url, headers=headers)
camelcamelcamel_webpage = response.text

soup = BeautifulSoup(camelcamelcamel_webpage, "html.parser")
title = soup.find(id="productTitle").get_text().strip()
product_price = float(soup.find(name="span", class_="green").getText().split("£")[1])

BUY_PRICE = 30

if product_price < BUY_PRICE:
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECIPIENT_EMAIL, msg=f"Subject:Amazon Price Alert!\n\n{title} is now £{product_price}!\n{url}".encode("utf-8"))
    connection.close()
