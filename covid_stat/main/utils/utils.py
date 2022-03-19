import re
import os
import json
from datetime import datetime

import requests
from bs4 import BeautifulSoup as BS

from ..models import Stat


def get_current_date():
    return str(datetime.now().date())

def _get_covid_stat_info(date):
    url = "https://стопкоронавирус.рф/information/"
    data = requests.get(url)
    soup = BS(data.text, 'html.parser')
    cases = soup.find_all("cv-stats-virus")
    data = re.findall(r":stats-data=\'(.*?)\'>", str(cases[0]))[0]

    date_json = json.loads(data)
    date_json["sick_change"] = date_json["sickChange"].replace("+", "")
    date_json["healed_change"] = date_json["healedChange"].replace("+", "")
    res = {k:v for k, v in date_json.items() if k in ("sick", "sick_change", "healed", "healed_change")}
    
    return res

def _get_covid_stat_with_shell():
    stream = os.popen('main/utils/html_parser.sh')
    output = stream.read().strip().split("\n")
    res = {k:v for v, k in zip(output, ["sick", "healed", "sick_change", "healed_change"])}
    return res

def check_date_in_table(date):
    data = Stat.objects.filter(date=date)
    print("Current data in table: ", data)
    if data:
        return True
    return False

def update_table(date):
    #data = _get_covid_stat_info(date)
    data = _get_covid_stat_with_shell()
    print("New data: ", data)
    stat = Stat(
        date=date, 
        sick=data["sick"], 
        sick_change=data["sick_change"], 
        healed=data["healed"], 
        healed_change=data["healed_change"]
        )
    stat.save()

def get_stat(date):
    return Stat.objects.filter(date=date)[0]