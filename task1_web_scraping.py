import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://quotes.toscrape.com/"

# Send request
response = requests.get(url)

print("Website Status Code:", response.status_code)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Extract quotes
quotes = soup.find_all("div", class_="quote")

data = []

for quote in quotes:
    text = quote.find("span", class_="text").get_text(strip=True)
    author = quote.find("small", class_="author").get_text(strip=True)

    data.append({
        "Quote": text,
        "Author": author
    })

# Convert to DataFrame
df = pd.DataFrame(data)

print("\n===== SCRAPED DATA =====")
print(df)

# Save data
df.to_csv("scraped_quotes.csv", index=False)

print("\nData saved successfully to scraped_quotes.csv")