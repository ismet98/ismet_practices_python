import requests
from bs4 import BeautifulSoup
import re

url = "https://www.nytimes.com/"
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Fetch page
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Select <p> inside <a>
titles = soup.select("a p")

seen = set()  # to avoid duplicates

for t in titles:
    text = t.get_text(strip=True)
    
    # Remove "X min read"
    text = re.sub(r"\d+\s*min read", "", text).strip()
    
    # Get parent <a> for link
    parent = t.find_parent("a")
    href = parent.get("href", "")
    
    # Convert relative links to full links
    if href.startswith("/"):
        href = "https://www.nytimes.com" + href
    
    # --- Filtering ---
    if (
        text and
        "/2026/" in href and                  # likely real article
        text not in seen                      # remove duplicates
    ):
        print(text)
        print("-" * 50)
        
        seen.add(text)