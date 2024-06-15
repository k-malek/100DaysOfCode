import requests
from bs4 import BeautifulSoup as bs

response=requests.get('https://www.reuters.com/graphics/EURO-2024/LIVE/akpeoalwxpr/schedule/',timeout=5)
response.raise_for_status()
bs_data = bs(response.content,'html.parser')
past_matches=bs_data.select_one('.pastmatches')
for match_day in past_matches.select('li.mx-auto'):
    day=match_day.find('h2').get_text()
    print(day)
    print('-'*10)
    print()
    for match in match_day.select('ol.mx-auto li'):
        team_1=match.find('span',class_='text-left').get_text().strip()
        team_2=match.find('span',class_='text-right').get_text().strip()
        score_1=match.find('div',class_='score-home').get_text().strip()
        score_2=match.find('div',class_='score-away').get_text().strip()
        print(f'{team_1} {score_1:>3}:{score_2:<3} {team_2}')
    print()
    print()
    print()
