from bs4 import BeautifulSoup
from extractor.confidence import calculate_confidence

class ContentParser:
    def parse(self, pages):
        modules = {}

        for page in pages:
            for h2 in page.find_all("h2"):
                module = h2.get_text(strip=True)

                if module not in modules:
                    modules[module] = {
                        "Description": "",
                        "Confidence": 0.0,
                        "Submodules": {}
                    }

                current = h2.find_next_sibling()
                while current and current.name != "h2":
                    if current.name == "p":
                        modules[module]["Description"] += current.get_text(strip=True) + " "

                    if current.name == "h3":
                        sub = current.get_text(strip=True)
                        p = current.find_next_sibling("p")
                        desc = p.get_text(strip=True) if p else ""

                        modules[module]["Submodules"][sub] = {
                            "Description": desc,
                            "Confidence": calculate_confidence(desc)
                        }

                    current = current.find_next_sibling()

                modules[module]["Confidence"] = calculate_confidence(
                    modules[module]["Description"]
                )

        return modules
