# import random
# import requests
# from bs4 import BeautifulSoup

# #crawl Imdb top 250 and ramdomly select a movie

# url = 'http://www.imdb.com/chart/top'

# def main():
#     response = requests.get(url)
#     print(f'Response : {response.status_code}')

#     soup = BeautifulSoup(response.text, 'html.parser')

#     movietags = soup.select('td.titleColumn')
#     inner_movietags = soup.select('td.titleColumn a')
#     ratings = soup.select('td.posterColumn span[name=ir]')

#     def get_year(movie_tag):
#         moviesplit = movie_tag.text.split()
#         year = moviesplit[-1]
#         return year
#     year = [get_year(tag) for tag in movietags]
#     actors_list = [tag['title'] for tag in inner_movietags]
#     titles = [tag.text for tag in inner_movietags]
#     ratings = [float(tag['data-value']) for tag in ratings]

#     n_movies = len(titles)
#     print(year, actors_list, titles, ratings)

#     while True:
#         idx = random.randrange(0,n_movies)

#         print(f'{titles[idx]} {year[idx]}, Rating: {ratings[idx]:.1f}, Starring: {actors_list[idx]}')

#         user_input = input('Do you want another movie (y/[n])? ')
#         if user_input != 'y':
#             break

# if __name__ == '__main__':
#     main()


import time
import socket 
from sklearn.datasets import load_iris

data = load_iris()

server = socket.socket(socket.SF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0",9999))

server.listen

while True:
    client, addr = server.accept()
    print("Connection from", addr)
    client.send("You are connected!\n".encode())
    client.send(f"{data['data'][:,0]}\n".encode())
    time.sleep(2)
    client.send("You are being disconnected\n".encode())
    client.close()







