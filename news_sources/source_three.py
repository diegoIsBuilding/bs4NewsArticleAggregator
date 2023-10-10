import requests
from bs4 import BeautifulSoup
import random

def fetch_source_three_article():
    url = 'https://ucsdguardian.org/category/news/'
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/117.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
    ]
    headers = {
        'User-Agent': random.choice(user_agents),
        'Referer': 'https://ucsdguardian.org/'
    }
    try:
        with requests.Session() as session:
            session.headers.update(headers)
            response = session.get(url, verify=False, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'lxml')
        news_cards = soup.find_all('div', class_ = 'catlist-tile-inner')
        news_card_info = []
        for news_card in news_cards:
            if news_card:
                news_title = news_card.find('a', class_ = 'homeheadline')
                if news_title:
                    titles = news_title.text.strip()
                else: titles = 'Unknown'
                

                news_link = news_card.find('a', class_ = 'homeheadline').get('href')
                if news_link:
                    links = news_link.strip()
                else: links = 'Unknown'
                
                news_author = news_card.find('a', class_ = 'creditline')
                #This does not retrieve multiple names when articles are written by multiple authors
                if news_author:
                    authors = news_author.text.strip()
                else: authors = 'Unknown'
                
                news_date = news_card.find('span', class_ = 'time-wrapper')
                if news_date:
                    dates = news_date.text.strip()
                else: dates = 'Unknown'
                
                news_card_info.append(titles)
                news_card_info.append(links)
                news_card_info.append(authors)
                news_card_info.append(dates)
        print(news_card_info)
                
        
        
    except requests.ConnectionError:
        print('Failed to connect to website')
    except requests.Timeout:
        print('The request timed out')
    except requests.RequestException as e:
        print(f'An error occurred while fetching the data: {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
fetch_source_three_article()