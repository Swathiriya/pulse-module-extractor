from extractor.crawler import DocumentationCrawler
from extractor.parser import ContentParser
from utils.cache import get_cached, set_cache

class ModuleExtractor:
    def extract(self, url: str):
        # Check cache first
        cached = get_cached(url)
        if cached:
            return cached

        # Crawl the URL
        crawler = DocumentationCrawler()
        html = crawler.crawl(url)

        # Parse the crawled content
        parser = ContentParser()
        parsed = parser.parse(html)

        # Format result
        result = []
        for module, data in parsed.items():
            result.append({
                "module": module,
                "Description": data.get("Description", "").strip(),
                "Confidence": data.get("Confidence", 0.85),
                "Submodules": data.get("Submodules", [])
            })

        # Save to cache
        set_cache(url, result)
        return result
