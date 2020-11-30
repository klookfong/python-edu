import requests
from bs4 import BeautifulSoup


response = requests.get("https://news.ycombinator.com/").text
soup = BeautifulSoup(response, "html.parser")
titles_html = soup.find_all(name="a", class_="storylink")
titles = [title.getText() for title in titles_html]
points_html = soup.find_all(name="span", class_="score")
points = [point.getText().split()[0] for point in points_html]

with open("hacker_news.txt", "w") as text_file:
    for i in range(len(points)):
        writing = f"{i}. {titles[i]}: {points[i]}\n"
        text_file.write(writing)
