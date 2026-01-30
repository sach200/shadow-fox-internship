import requests
from bs4 import BeautifulSoup
import csv
import json

class WebScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def scrape_quotes(self, url="http://quotes.toscrape.com"):
        """Scrape quotes from quotes.toscrape.com"""
        quotes_data = []
        page = 1
        
        while True:
            response = self.session.get(f"{url}/page/{page}")
            if response.status_code != 200:
                break
                
            soup = BeautifulSoup(response.content, 'html.parser')
            quotes = soup.find_all('div', class_='quote')
            
            if not quotes:
                break
                
            for quote in quotes:
                text = quote.find('span', class_='text').text
                author = quote.find('small', class_='author').text
                tags = [tag.text for tag in quote.find_all('a', class_='tag')]
                
                quotes_data.append({
                    'text': text,
                    'author': author,
                    'tags': tags
                })
            
            page += 1
            
        return quotes_data
    
    def scrape_news_headlines(self, url="https://news.ycombinator.com"):
        """Scrape headlines from Hacker News"""
        response = self.session.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        headlines = []
        stories = soup.find_all('tr', class_='athing')
        
        for story in stories[:20]:
            title_elem = story.find('span', class_='titleline')
            if title_elem:
                title = title_elem.find('a').text
                link = title_elem.find('a')['href']
                headlines.append({'title': title, 'link': link})
                
        return headlines
    
    def save_to_csv(self, data, filename):
        """Save data to CSV file"""
        if not data:
            return
            
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
    
    def save_to_json(self, data, filename):
        """Save data to JSON file"""
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

def main():
    scraper = WebScraper()
    
    print("Web Scraper - Choose an option:")
    print("1. Scrape quotes")
    print("2. Scrape news headlines")
    
    choice = input("Enter choice (1-2): ")
    
    if choice == '1':
        print("Scraping quotes...")
        quotes = scraper.scrape_quotes()
        scraper.save_to_json(quotes, 'quotes.json')
        scraper.save_to_csv(quotes, 'quotes.csv')
        print(f"Scraped {len(quotes)} quotes. Saved to quotes.json and quotes.csv")
        
    elif choice == '2':
        print("Scraping news headlines...")
        headlines = scraper.scrape_news_headlines()
        scraper.save_to_json(headlines, 'headlines.json')
        scraper.save_to_csv(headlines, 'headlines.csv')
        print(f"Scraped {len(headlines)} headlines. Saved to headlines.json and headlines.csv")
    
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()