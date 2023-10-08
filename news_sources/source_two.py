import requests
from bs4 import BeautifulSoup
import random

def fetch_source_two_article():
    url = 'https://dailybruin.com/category/campus'
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
        'Referer': 'https://dailybruin.com/'
    }
    
    try:
        with requests.Session() as session:
            session.headers.update(headers)
            response = session.get(url, verify=False, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'lxml')
        vertical_cards = soup.find_all('div', class_ = 'css-1urk0hm')
        horizontal_cards = soup.find_all('div', class_ = 'style_card__2hnxE')
        
        for vert_card in vertical_cards:
            article_info = []
            vert_campus_tag = vert_card.find('h2', class_ = 'css-mhukz7').text
            print(vert_campus_tag)
            if vert_campus_tag == 'Campus':
                small_title_tag = vert_card.find('div', class_ = 'css-1or0iyk')
                large_title_tag = vert_card.find('div', class_ = 'css-u3qgkr')
                if small_title_tag:
                    titles = small_title_tag.text.strip()
                elif large_title_tag:
                    titles = large_title_tag.text.strip()
                else:
                    'Unknown'

                link_tag = vert_card.find('a', style="text-decoration:none")
                if link_tag:
                    links = link_tag.get('href').strip()
                else: 'Unknown'

                small_author_tag = vert_card.find('h3', class_ = 'css-122uc6i').find('a')
                large_author_tag = vert_card.find('h3', class_ = 'css-fwulup').find('a') 
                if small_author_tag:
                    authors = small_author_tag.text.strip()
                elif large_author_tag:
                    authors = large_author_tag.text.strip()
                else: 'Unknown'

                date_tag = vert_card.find('span', class_ = 'css-7zra3w')
                if date_tag:
                    dates = date_tag.text.strip()
                else: 'Unknown'
            
            for horiz_card in horizontal_cards:
                horiz_campus_tag = horiz_card.find('h2', class_ = 'css-5yw8gm').text
                if horiz_campus_tag == 'Campus':
                    horiz_title_tag = horiz_card.find('h2', class_ = 'css-m9vgwi')
                    if horiz_title_tag:
                        horiz_titles = horiz_title_tag.text.strip()
                    else: 'Unknown'
                    
                    horiz_link_tag = horiz_card.find('a', style="text-decoration:none")
                    if horiz_link_tag:
                        horiz_links = horiz_link_tag.get('href').strip()
                    else: 'Unknown'
                    
                    horiz_author_tag = horiz_card.find('h3', class_ = 'css-yoisth').find('a')
                    if horiz_author_tag:
                        horiz_authors = horiz_author_tag.text.strip()
                    else: 'Unknown'
                    
                    horiz_date_tag = horiz_card.find('span', class_ = 'css-1fg4j61')
                    if horiz_date_tag:
                        horiz_dates = horiz_date_tag.text.strip()
                    else: 'Unknown'
            

                article_info.append(titles)
                article_info.append(links)
                article_info.append(authors)
                article_info.append(dates)
                article_info.append(horiz_titles)
                article_info.append(horiz_links)
                article_info.append(horiz_authors)
                article_info.append(horiz_dates)
                print(article_info)
        
        
    except requests.ConnectionError:
        print('Failed to connect to website')
    except requests.Timeout:
        print('The request timed out')
    except requests.RequestException as e:
        print(f'An error occurred while fetching the data: {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        
fetch_source_two_article()