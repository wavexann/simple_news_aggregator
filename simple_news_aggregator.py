import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.bbc.com/news"

response = requests.get(url)

if response.status_code == 200:
	print("Request was successful.")

	data = []

	soup = BeautifulSoup(response.text , "lxml")

	class_names = ["sc-f98732b0-5 gGpWNz", "sc-b8778340-3 gxEarx", "sc-e5949eb5-2 eOoDdE"]

	articles = soup.find_all("div", class_ = class_names)

	for article in articles:
		headline = article.find("h2")
		paragraph = article.find("p")


		headline_text = headline.text.strip() if headline else "No headline"
		paragraph_text = paragraph.text.strip() if paragraph else "No paragraph"



		data.append({
			"Headlines": headline_text,
			"Paragraph": paragraph_text,
			})

	df = pd.DataFrame(data)
	df.to_csv("simple_news_aggregator.csv" , index = False)

	print("Data is saved as simple_news_aggregator.csv.")

	