import requests
from bs4 import BeautifulSoup

def fetch_prices(item_name):
    websites = {
        'Amazon': f'https://www.amazon.com/s?k={item_name}',
        'eBay': f'https://www.ebay.com/sch/i.html?_nkw={item_name}',
        'Walmart': f'https://www.walmart.com/search/?query={item_name}',
        'Best Buy': f'https://www.bestbuy.com/site/searchpage.jsp?st={item_name}',
        'Target': f'https://www.target.com/s?searchTerm={item_name}'
    }

    prices = []
    
    for site, url in websites.items():
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            soup = BeautifulSoup(response.content, 'html.parser')
            
            if site == 'Amazon':
                price = soup.find('span', {'class': 'a-offscreen'})
            elif site == 'eBay':
                price = soup.find('span', {'class': 's-item__price'})
            elif site == 'Walmart':
                price = soup.find('span', {'class': 'price-characteristics'})
            elif site == 'Best Buy':
                price = soup.find('span', {'class': 'price'})
            elif site == 'Target':
                price = soup.find('span', {'class': 'h-padding-h-tight'})

            if price:
                prices.append((site, price.text.strip()))
            else:
                prices.append((site, "Price not found"))
        
        except Exception as e:
            prices.append((site, f"Error fetching price: {str(e)}"))

    return prices