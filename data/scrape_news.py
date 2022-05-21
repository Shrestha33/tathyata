import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

FILE_NAME = "datasets.csv"

links_ekantipur = [
    "https://ekantipur.com/news/2022/05/21/165309257608019409.html",
]

def scrape_ekantipur():
    for link in links_ekantipur:
        req = urlopen(link)
        soup = BeautifulSoup(req.read().decode("utf-8"), "html.parser")
        body = soup.find("div", attrs={"class": "article-header"})
        title = body.find("h1").text
        # get sub heading of the news as the body 
        contents_list = body.find_all("div", attrs={"class": "sub-headline"})

        # get all the paragraphs
        contents_list.extend(soup.find("div", attrs={"class": "current-news-block"}).find_all("p"))

        content = "".join([content_tag.text for content_tag in contents_list])
        
        with open(FILE_NAME, 'a') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([0, title, link, content])


def scrape_nagarik():
    raise NotImplementedError

def scrape_annapurna():
    raise NotImplementedError

def setup():
    if not os.path.exists("datasets.csv"):
        with open(FILE_NAME, 'w') as f:
            f.write("id, Title, Link, Text\n")
    
        f.close()


if __name__ == "__main__":
    scrape_ekantipur()