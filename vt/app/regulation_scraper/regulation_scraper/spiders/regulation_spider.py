import scrapy
from scrapy.crawler import CrawlerProcess

class RegulationSpider(scrapy.Spider):
    name = 'regulation_spider'
    
    # Définissez ici les URLs de départ
    start_urls = [
        'https://dataprotection.ie',  # Remplacez par une URL valide où vous avez le droit de scraper
    ]
    
    def parse(self, response):
        # Extraire les articles ou les entrées de blog
        for post in response.css('div.news-post'):
            yield {
                'title': post.css('h2.title::text').get(),
                'summary': post.css('p.summary::text').get(),
                'date': post.css('span.date::text').get(),
                'url': response.urljoin(post.css('a::attr(href)').get())
            }

        # Suivre les liens vers les pages suivantes
        next_page = response.css('a.next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

# Cette section est facultative et sert à exécuter le spider indépendamment si nécessaire
if __name__ == "__main__":
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
    })
    process.crawl(RegulationSpider)
    process.start()
