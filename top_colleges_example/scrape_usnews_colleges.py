# pip install selenium beautifulsoup4
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from time import sleep
from random import randint

chromedriver_path = "C:\\Users\\ytang\\Documents\\workspace\\teaching\\intermediate\\youtube\\front_page_titles\\chromedriver.exe"
service = Service(chromedriver_path)
options = Options()
driver = webdriver.Chrome(service=service, options=options)

url = "http://www.usnews.com/best-colleges/rankings/national-universities"
base_url = "http:/www.usnews.com"

driver.get(url)
sleep(randint(3, 5))
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()
links = soup.find_all("a", href=re.compile("^/best-colleges/(?!rankings).*"))
# links = soup.find_all("a")
top10 = set()
for link in links:
    if "college-search" in link["href"] or "compare" in link["href"] or "admissions" in link["href"] or "myfit" in link["href"] or "photos" in link["href"] or "reviews" in link["href"]:
        continue
    top10.add(base_url+link["href"])
    # top10.add(link.get("href"))
for link in top10:
    print(link)

for link in top10:
    # navigate to page
    # click read more
    # make soup
    # get text from all paragraphs
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(link)
    sleep(randint(2, 4))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    paragraphs = soup.find_all("div", class_=re.compile("^Raw-.*"))
    text = ""
    for p in paragraphs:
        text += p.get_text() + " "
    driver.quit()
    filename = link.split("best-colleges/")[1] + ".txt"
    with open(filename, "w") as f:
        f.write(text)
