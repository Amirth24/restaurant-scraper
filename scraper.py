"""
    This Scraper get restaurat data (Name and Rating) for a given webpage.
    - Assign the CSS Selector for tag containing Restaurant Name to `RESTAURANT_NAME_SELECTOR`.
    - Assign the CSS Selector for the tag containng the Restaurant's 
    rating to `RESTAURANT_RATING_SELECTOR`
"""
import sys
from collections import namedtuple
import csv

import requests
from bs4 import BeautifulSoup


URL = "https://www.mouthshut.com/Restaurants-ProID-169-page-{0}" # Just Used as an Example
RESTAURANT_NAME_SELECTOR='.card-deck *  .card-body .listing-prod-title'
RESTAURANT_RATING_SELECTOR='.rating-no'


###################### DON'T CHANGE CODE BELOW ##############################


Restaurant = namedtuple('Restaurants', ('Name', 'Rating'))


def scrape_page(url: str) -> type[Restaurant]:
    """Scrape the nth page
        Args: 
            url (str): The webpage to be scraped.
        Returns:
            List[type[Restaurant]]: The list of restaurants in the page n.
    """
    try:
        res = requests.get(url, timeout=1000)
        res.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e, file=sys.stderr)
        sys.exit(-1)


    soup = BeautifulSoup(res.content, "lxml")
    name_and_rating = map(
        Restaurant,
        map(lambda x: x.text.strip(), soup.select(RESTAURANT_NAME_SELECTOR)),
        map(
            lambda x: float(x.text.strip()) if len(x.text.strip()) <= 4 else None,
            soup.select(RESTAURANT_RATING_SELECTOR)
        )
    )
    return list(name_and_rating)

###################### DON'T CHANGE CODE ABOVE ##############################


restaurants = []
for i in range(5):
    formatted_url = URL.format(i)
    print("Extracting data from:", formatted_url)
    restaurants.extend(scrape_page(formatted_url))

###################### DON'T CHANGE CODE BELOW ##############################
with open('restaurants.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Rating'])
    writer.writerows(restaurants)
###################### DON'T CHANGE CODE ABOVE ##############################
