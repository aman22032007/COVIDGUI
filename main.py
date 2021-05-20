import random
import requests
import countrylist
import datetime

yesterday = datetime.date.today() - datetime.timedelta(days=1)
day_before_yesterday = datetime.date.today() - datetime.timedelta(days=2)
country = None


def execute():
    url2 = f'https://api.covid19api.com/total/country/{country}?from={day_before_yesterday}T00:00:00Z&to={yesterday}T00:00:00Z'
    response2 = requests.get(url2)
    resp2 = response2.json()
    cases_country = resp2
    return cases_country

def execute_world():
    url = 'https://api.covid19api.com/world/total'
    response = requests.get(url)

    resp_json = response.json()
    cases = resp_json
    return cases


if __name__ == "__main__":
    execute()
