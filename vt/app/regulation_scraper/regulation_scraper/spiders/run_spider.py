from scrapy.crawler import CrawlerProcess
from app import RegulationSpider

def run_regulation_spider():
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    })
    process.crawl(RegulationSpider)
    process.start()

if __name__ == '__main__':
    run_regulation_spider()
