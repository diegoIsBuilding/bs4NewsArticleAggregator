import requests
from bs4 import BeautifulSoup
import random
import os
import json

# Make sure these directories exist
if not os.path.exists("data/raw"):
    os.makedirs("data/raw")
if not os.path.exists("data/processed"):
    os.makedirs("data/processed")

def fetch_source_one_article():
    url = 'https://newuniversity.org/category/news/campus-news/'
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
        'Referer': 'https://newuniversity.org/'
    }
    
    try:
        with requests.Session() as session:
            session.headers.update(headers)
            response = session.get(url, verify=False, timeout=10)
        response.raise_for_status()
        
        #save raw data
        with open('data/raw/source_one_raw_data.html', 'w', encoding='utf-8') as file:
            file.write(response.text)
        
        soup = BeautifulSoup(response.text, 'lxml')
        headlines = soup.find_all('div', class_ = 'td-module-meta-info td-module-meta-info-bottom')
        article_info = []
        for headline in headlines: 
            title = headline.contents[1].text.strip()
            links = headline.find('a').get('href').strip()
            authors = headline.find('span', class_ = 'td-post-author-name').find('a').text.strip()
            date = headline.find('span', class_ = 'td-post-date').find('time').text.strip()
            article_info.append({
                'title': title,
                'link': links,
                'author': authors,
                'date': date
            })
        
       
            
        with open('data/processed/source_one.json', 'w') as file:
            json.dump(article_info, file, indent=4)
        
        
    except requests.ConnectionError:
        print('Failed to connect to website')
    except requests.Timeout:
        print('The request timed out')
    except requests.RequestException as e:
        print(f'An error occurred while fetching the data: {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        
fetch_source_one_article()