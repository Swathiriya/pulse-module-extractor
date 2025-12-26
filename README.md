# pulse-module-extractor


Pulse Module Extractor
A Streamlit-based Python application that automatically extracts modules, submodules, descriptions, and confidence scores from documentation URLs.
It uses web crawling, parsing, and caching to efficiently analyze structured documentation content.

🚀 Features
 Crawl documentation pages from a given URL
 Extract:
Module names
Descriptions
Submodules
Confidence scores
 Caching for faster repeated requests
 Simple and interactive Streamlit UI
 Modular and clean Python package structure
 
pulse-module-extractor/
│
├── app.py                     # Streamlit UI
├── api.py                     # REST API
├── Dockerfile
├── requirements.txt
│
├── extractor/
│   ├── __init__.py
│   ├── crawler.py
│   ├── parser.py
│   ├── extractor.py
│   └── confidence.py
│
├── utils/
│   ├── cache.py
│   ├── logger.py
│   └── validators.py
│
├── sample_outputs/
│   └── wordpress.json
│
└── README.md
