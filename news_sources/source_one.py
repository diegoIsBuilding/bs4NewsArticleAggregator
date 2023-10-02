import requests
from bs4 import BeautifulSoup

def fetch_source_one_article():
    url = 'https://bitcoinmagazine.com/articles'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, verify=False, timeout =10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'lxml')
        headlines = soup.find_all('h2', class_='m-ellipsis--text m-card--header-text')
        print(headlines)
        
        
    except requests.ConnectionError:
        print('Failed to connect to website')
    except requests.Timeout:
        print('The request timed out')
    except requests.RequestException as e:
        print(f'An error occurred while fetching the data: {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        
fetch_source_one_article()