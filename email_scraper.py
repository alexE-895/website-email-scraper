import requests
import re

url = "https://example.com"

response = requests.get(url, timeout=10)

emails = set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", response.text))

for email in emails:
    print(email)
