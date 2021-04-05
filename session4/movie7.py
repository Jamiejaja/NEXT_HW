import requests
from bs4 import BeautifulSoup
import csv
file = open('movie.csv', mode='w', newline='')

writer = csv.writer(file)
writer.writerow(["title","img_src"])
MOVIE_URL ='https://movie.naver.com/movie/running/current.nhn'
movie_html = requests.get(MOVIE_URL)

movie_soup = BeautifulSoup(movie_html.text,"html.parser")
movie_list_box = movie_soup.find("ul", {"class" : "lst_detail_t1"})
movie_list = movie_list_box.find_all('li')

final_result = []
for movie in movie_list:
    title = movie.find("dt", {"class" : "tit"}).find("a").text
    img_src = movie.find("div", {"class" : "thumb"}).find("img")['src']
    score = movie.find("div", {"class" : "star_t1"}).find("span").text
    director = movie.find("dl", {"class" : "info_txt1"}).find("dt").text
    actor = movie.find("dl", {"class" : "info_txt1"}).find("dd")[2].text
    date = movie.find("dl", {"class" : "info_txt1"}).find("dd")[0].text
    print(date.replace('\r','').replace('\t','').replace('\n',''))

    movie_info = {
    'title' : title,
    'img_src' : img_src,
    'score' : score,
    'director' : director,
    'actor' : actor,
    'date' : date
    }
    final_result.append(movie_info)

for result in final_result:
    row = []
    row.append(result['title'])
    row.append(result['img_src'])
    row.append(result['score'])
    row.append(result['director'])
    writer.writerow(row)
print(final_result)