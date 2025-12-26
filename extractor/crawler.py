# extractor/crawler.py
import requests

class DocumentationCrawler:
    def fetch(self, url: str) -> str:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
