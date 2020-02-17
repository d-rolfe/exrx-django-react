import requests
from bs4 import BeautifulSoup

class Parser:
    def parse_exercise_details_page(self):
        url = 'https://exrx.net/WeightExercises/PectoralSternal/AsChestDip'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        main_content = soup.main.article.div.div
        left_div = main_content.div
        right_div = left_div.find_next_sibling()
        # print('left div')
        # print(left_div.prettify())
        # print('right div')
        # print(right_div.prettify())
        gif = left_div.div.img
        tbody = left_div.table.tbody
        utility = tbody.findAll('tr')[0].td.find_next_sibling().a
        mechanics = tbody.findAll('tr')[1].td.find_next_sibling().a
        force = tbody.findAll('tr')[2].td.find_next_sibling().a
        print(gif)
        print(utility)

p = Parser()
p.parse_exercise_details_page()