import requests
import csv
import bs4

url = "http://www.esquire.com/entertainment/movies/g2419/100-best-sci-fi-movies/?slide=1"
request = requests.get(url)
soup = bs4.BeautifulSoup(request.content, "html.parser")

