#Log-D7
#https://t.me/Decode7Channel

import requests
from bs4 import BeautifulSoup

def search_happymod(query):
    url = f"https://happymod.com/search.html?q={query.replace(' ', '+')}"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        
        for item in soup.select('.pdt-app-box'):
            title = item.select_one('.pdt-app-h3 a').text.strip()
            link = "https://happymod.com" + item.select_one('.pdt-app-h3 a')['href']
            results.append({'Title': title, 'Link': link})
        
        return results
    else:
        print("Failed to retrieve data.")
        return []

def display_results(results):
    print("=" * 30 + " Search Results " + "=" * 30)
    for i, result in enumerate(results, start=1):
        print(f"\n{i}")
        print(f"Name: {result['Title']}")
        print(f"Link: {result['Link']}")
        print("-" * 70)

# Example usage
query = input("What apk do you want to search? ")
results = search_happymod(query)
if results:
    display_results(results)
