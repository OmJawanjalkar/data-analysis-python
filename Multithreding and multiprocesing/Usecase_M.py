import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def scrape_url(url):
    try:
        response = requests.get(url, timeout=5)
        # Use .content to handle encoding properly
        soup = BeautifulSoup(response.content, "html.parser")
        # Get title safely
        title = soup.title.string.strip() if soup.title and soup.title.string else "No Title"
        return f"{url} --> {title}"
    except Exception as e:
        return f"{url} --> Error: {e}"

if __name__ == "__main__":
    urls = [
        "https://www.python.org/",
        "https://www.wikipedia.org/",
        "https://www.github.com/",
        "https://www.stackoverflow.com/",
        "https://www.openai.com/"
    ]

    start = time.time()
    results = []

    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(scrape_url, url): url for url in urls}
        for future in as_completed(future_to_url):
            results.append(future.result())

    for r in results:
        print(r)

    print(f"⏳ Time taken: {time.time() - start:.2f} seconds")
