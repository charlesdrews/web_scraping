import requests
import csv
import bs4
import pandas as pd

movie_dict_list = []

url = "http://www.esquire.com/entertainment/movies/g2419/100-best-sci-fi-movies/?slide={}"
omdb_api_url = "http://www.omdbapi.com/?t={}&tomatoes=true"

for number in range(1, 10):
	request = requests.get(url.format(number))
	soup = bs4.BeautifulSoup(request.content, "html.parser")
	movies = soup.findAll('div', {'class':'gallery-slide--title'})

	for movie in movies:
	    text = movie.getText()
	    if len(text) > 0:
                # get rank and name from string
                rank = text.split('.')[0].strip().encode('utf-8')
                name = text.split('.')[1].strip().encode('utf-8')

                # remove (year) from end of name
                name = name.split('(')[0].strip()

                # search for movie name on omdb
                omdb_request = requests.get(omdb_api_url.format(name))

                # get Rotten Tomatoes rating from omdb response
                rating = omdb_request.json()['tomatoMeter']

                # save dict of all info for movie
                d = {'movie_rank': rank, 'movie_name': name, 'rating': rating}
	        movie_dict_list.append(d)

# sort dicts by rank value
dicts_sorted = sorted(movie_dict_list, key=lambda k: k['movie_rank'])

# to-do - remove duplicates

#with open('top_scifi_movies.csv', 'w') as csvfile:
    # write column names to csv
    #field_names = dicts_sorted[0].keys()
    #writer = csv.DictWriter(csvfile, fieldnames=field_names)
    #writer.writeheader()

    # write data to csv as rows
    #for d in dicts_sorted:
        #writer.writerow(d)

# use pandas to drop duplicates and create a csv
df = pd.DataFrame(dicts_sorted)
df = df.drop_duplicates()
df.to_csv("top_scifi_movies.csv")
