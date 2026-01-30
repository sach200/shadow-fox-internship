# Web Scraper

A Python web scraping tool using Beautiful Soup and Scrapy for extracting data from websites.

## Features
- Beautiful Soup scraper for quotes and news headlines
- Scrapy spiders for advanced scraping
- Export data to JSON and CSV formats
- Session management and proper headers
- Error handling and pagination support

## Installation
```bash
pip install -r requirements.txt
```

## Usage

### Beautiful Soup Scraper
```bash
python scraper.py
```

### Scrapy Spiders
```bash
# Run quotes spider
scrapy crawl quotes -o quotes.json

# Run books spider  
scrapy crawl books -o books.json
```

## Supported Sites
- quotes.toscrape.com (quotes with authors and tags)
- news.ycombinator.com (latest headlines)
- books.toscrape.com (book catalog with ratings)

## Output Formats
- JSON: Structured data with proper formatting
- CSV: Tabular data for spreadsheet analysis

## Author
Created for Shadow Fox Internship Task