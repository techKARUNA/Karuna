import requests
import pandas as pd

API_KEY = "bdb5ed0e7ba88100077ff04179ea3f657542d7c8718cf1e50bd8a490776e6337"

query = 'site:linkedin.com/in "founder" AND "tech startup" AND "India"'

params = {
    "q": query,
    "engine": "google",
    "api_key": API_KEY,
    "num": 20
}

response = requests.get("https://serpapi.com/search", params=params)
data = response.json()

results = data.get("organic_results", [])
leads = []

for result in results:
    title = result.get("title", "N/A")
    link = result.get("link", "N/A")
    snippet = result.get("snippet", "N/A")

    leads.append({
        "Name/Title": title,
        "Profile URL": link,
        "Description": snippet
    })

df = pd.DataFrame(leads)
df.to_excel("google_leads_india.xlsx", index=False)

print("✅ Leads saved to 'google_leads_india.xlsx'")
