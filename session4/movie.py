import requests
from bs4 import BeautifulSoup
import csv

file = open('movie.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(['title','image'])

movie_URL = f'https://movie.naver.com/movie/running/current.nhn'
movie_html = requests.get(movie_URL)
movie_soup = BeautifulSoup(movie_html.text,"html.parser")

movie_list_box = movie_soup.find("ul", {"class" : "lst_detail_t1"})
movie_list = movie_list_box.find_all('li')

final_result = []
for movie in movie_list:
    title = movie_soup.find('dt',{'class': 'tit'}).find('a').text
    image = movie_soup.select('div.thumb > a> img')[0]['src']

for result in final_result:
    row = []
    row.append(result['title'])
    row.append(result['image'])
    writer.writerow(row)
print(final_result)
