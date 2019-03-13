import requests
# from requests.adapters import HTTPAdapter
# from requests.packages.urllib3.util.retry import Retry
from bs4 import BeautifulSoup
import itertools

root_page = "http://limitlesstcg.com"
first_decks = "http://limitlesstcg.com/decks/?time=all"

def pokemon(deck_page):

    print('Processing: ', deck_page)

    try:
        r = requests.get(deck_page)

        soup = BeautifulSoup(r.text, 'html.parser')
        decklist_col = soup.find("div", {"class": "decklist-column"})
        card_names = [x.contents for x in decklist_col.find_all(
            "span", {"class": "decklist-card-name"})]
        card_names = list(itertools.chain(*card_names))
        card_names = list(filter(lambda x: \
                                 True if not str(x).startswith('<span') \
                                 else False, card_names))
    except AttributeError as e:
        print(e) # Some pages may not have any data, so ignore those errors.
        return []
    return card_names


# def variants(page, all_data):
#     r = requests.get(root_page + "/decks/?id=47")
#     soup = BeautifulSoup(r.text, 'html.parser')
#     soup.findAll("a", href=re.compile("\/decks\/\?id="))


def decks(page, all_data):
    r = requests.get(page)

    soup = BeautifulSoup(r.text, 'html.parser')

    deck_names = [x.contents for x in soup.select("tr td a")[:15]]
    deck_names = list(itertools.chain(*deck_names))

    p_points = [x.contents for x in soup.select("tr td span")[:15]]
    p_points = list(itertools.chain(*p_points))

    p_hrefs = [x.attrs['href'] for x in soup.select("tr td a")]

    page_decks = list(zip(deck_names, p_points, p_hrefs))

    for deck in page_decks:
        card_names = pokemon(root_page + deck[2])
        all_data.append((deck[0], deck[1], card_names))

all_data = []
for page_count in range(1, 8):
    try:
        if page_count < 2:
            decks(first_decks, all_data)
        else:
            print('page_count:', page_count)
            decks(first_decks + "&pg=" + str(page_count), all_data)
            print(all_data)
    except IOError as e:
        print(e)
        break;
    except AttributeError as e:
        print(e) # Some pages may not have any data, so ignore those errors.

with open('./decks.csv', 'w') as f:
    for (deck_name, points, card_names) in all_data:
        for card_name in card_names:
            s = str(deck_name) + ',' + str(points) + ',' + \
                str(card_name) + '\n'
            f.write(s)
