# Amrita.edu Keyword Crawler

A lightweight, domain-specific web crawler designed to search for keywords across the [Amrita Vishwa Vidyapeetham](https://www.amrita.edu) website.  
Built with Python, it uses `requests` and `BeautifulSoup` to fetch and parse web pages, then stores results for further analysis.

---

## Features
- Search for any keyword across Amrita.edu pages  
- Recursive crawling (restricted to the same domain)  
- Keyword matches saved in `results.csv` (URL + text snippet)  
- Respects `robots.txt` and includes request throttling  
- Easy to configure (starting URL, keyword, crawl depth, delay)

---

## Tech Stack
- Python 3.7+
- requests – HTTP requests  
- beautifulsoup4 – HTML parsing  
- lxml *(optional)* – faster parsing  

---

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/amrita-crawler.git
cd amrita-crawler
```

### 2. Set Up Virtual Environment
```bash
python3 -m venv venv          # create virtual environment
source venv/bin/activate      # Linux/macOS
.\venv\Scripts\activate       # Windows
```
*A virtual environment keeps dependencies separate from your system Python.*

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Crawler
```bash
python crawler.py
```

### 5. Deactivate Virtual Environment (Optional)
```bash
deactivate
```

---

## Configuration
Modify values in `crawler.py` to customize behavior:

| Parameter     | Description                             | Default          |
|---------------|-----------------------------------------|------------------|
| `start_url`   | Starting point for crawling             | `https://www.amrita.edu` |
| `keyword`     | Keyword to search across pages          | `"scholarship"`  |
| `max_pages`   | Maximum pages to crawl                  | `50`             |
| `delay`       | Delay (seconds) between requests        | `1`              |

---

## Output Format
All keyword matches are stored in `results.csv`:

```csv
URL,Snippet
https://www.amrita.edu/scholarships,... scholarship opportunities available ...
```

---

## Notes
- Always check the website’s [robots.txt](https://www.amrita.edu/robots.txt) before crawling.  
- Keep `max_pages` reasonable to avoid overloading the server.  
- This project is for educational and research purposes only.  

---

## Roadmap
- Add command-line arguments (`--keyword`, `--max-pages`, etc.)  
- Implement breadth-first crawling strategy for balanced exploration  
- Export results in JSON and SQLite formats  
- Web interface (Flask/Streamlit) for interactive searches  

---

## License
This project is licensed under the MIT License.  
See [LICENSE](LICENSE) for more information.
