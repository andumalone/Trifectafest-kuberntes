import requests, os, bs4, lxml, re
import pandas as pd
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

# relevant 'crawlable' information
# ev3page-finish < start_date & end_date
# ev3page < page-items
# ev3page-title < title
# ev3page-week < week day
# ev3page-venue < venue
# ev3page-day < day
# ev3page-month < month
# ev3page-year < year
# ev3page-hour < hours

def functie3():
    print("Retrieving data from https://festivalfans.nl/agenda/")

    urls = ['https://festivalfans.nl/agenda/']

    events_list = []

    for url in urls:
        # request the URL and parse the HTML using BeautifulSoup
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # <div class="ev3page">
        ev3page_amount = r'<div class="[^"]ev3page3[^"]">(.*?)<\/div>'
        matches = re.search(ev3page_amount, str(soup), re.DOTALL)

        if matches:
            div_content = matches.group(1)
            ev3page_number = int(re.sub(r'\D', '', div_content))
            print(ev3page_number)
        else:
            print('No match found')

        # find all the div elements with class 'ev3page'
        events = soup.find_all('div', class_='ev3page')

        # loop through each event and scrape the relevant information
        for event in events:
            # scrape start and end date
            element = event.find('div', class_='ev3page-finish')

            if element is not None:
                start_date = event.find('div', class_='ev3page-finish').text.strip()
                end_date = event.find_all('div', class_='ev3page-finish')[-1].text.strip()
            else:
                continue
            date_range = f"Date: {start_date} - {end_date}"

            # scrape event name
            link = event.find_all('a', href=re.compile(r'https://festivalfans.nl/event/'))
            if len(link) > 1:
                event_name = link[1].text.strip()
            else:
                event_name = link[0].text.strip()

            # scrape venue
            venue = event.find('div', class_='ev3page-venue').text.strip()

            # scrape hours
            hours = event.find('div', class_='ev3page-hour').text.strip()

            # scrape week day
            week = event.find('div', class_='ev3page-week').text.strip()

            events_dict ={
                'Name': event_name,
                'In': venue,
                'Day': week,
                'Date': date_range,
                'Hours': hours,
            }

            events_list.append(events_dict)

    # ! return the scraped information for each event
    events_dict = {'Events': events_list}

    for k in events_dict['Events'][::]:
        print(k['Date'])

    return(events_dict['Events'][::])

# {"Events":[{"Date":"Date: 31 Mar - 01 Apr","Day":"Vrijdag","Hours":"18:00 - 23:00","In":"GelreDome, Arnhem","Name":"Snollebollekes Live in Concert"},{"Date":"Date: 07 Apr - 09 Apr","Day":"Vrijdag","Hours":"12:00 - 23:00","In":"NDSM-Werf, Amsterdam","Name":"DGTL Amsterdam"}]}