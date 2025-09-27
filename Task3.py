import requests
from bs4 import BeautifulSoup

url = "https://www.thehindu.com/"

response = requests.get(url)

try:
    response.raise_for_status()                   # Will raise an exception for HTTP errors
except requests.exceptions.HTTPError as e:
    print("Failed to load website")
    exit()


soup = BeautifulSoup(response.text, "html.parser")    # Parse the HTML content

# Extract headlines using appropriate CSS selectors
headlines = soup.select("h3 a")  # Adjusted to match current HTML structure


if not headlines:
    print("No headlines found — check selector or site structure")
    exit()

# Save the headlines to a text file
with open("headlines.txt", "w", encoding="utf-8") as file:
    for i, h in enumerate(headlines, start=1):
        title = h.get_text(strip=True)
        file.write(f"{i}. {title}\n")

print(f"Scraped {len(headlines)} headlines. Saved in headlines.txt")
