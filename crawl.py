import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re, time, csv

visited = set()
matches = []

def crawl(url, keyword, max_pages=100, delay=1):
    if len(visited) >= max_pages or url in visited:
        return
    visited.add(url)

    try:
        response = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        if "text/html" not in response.headers.get("Content-Type", ""):
            return
    except Exception as e:
        print(f"Failed: {url} ({e})")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text(separator=" ").lower()

    if keyword.lower() in text:
        snippet = re.search(rf".{{0,40}}{keyword.lower()}.{{0,40}}", text)
        snippet_text = snippet.group(0) if snippet else ""
        matches.append((url, snippet_text))
        print(f"✅ Found keyword in {url}")

    # follow links
    for link in soup.find_all("a", href=True):
        full_url = urljoin(url, link["href"])
        if urlparse(full_url).netloc == urlparse(url).netloc:  # same domain
            crawl(full_url, keyword, max_pages, delay)
            time.sleep(delay)

# ---- Run the crawler ----
start_url = "https://www.amrita.edu"
keyword = "amma"   # try with "ai" or "admission"

crawl(start_url, keyword, max_pages=50, delay=1)

# Save results
with open("results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["URL", "Snippet"])
    writer.writerows(matches)

print("\n🎯 Results saved to results.csv")
