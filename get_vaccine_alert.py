#!/usr/bin/env python
"""
    checks for vaccine appointments on vaccinespotter.org
    notifies you if there is.

    @author: Johnny Huang <johnny.h1997@berkeley.edu>

"""
import sys
import time
import schedule
from selenium import webdriver
from bs4 import BeautifulSoup
from twilio.rest import Client
import re
from selenium.webdriver.common.by import By
from us_state_abbrev import us_state_abbrev

# TODO ENTER TWILIO INFORMATION
# Twilio credentials..obtain from https://www.twilio.com/console
TWILIO_ACCOUNT_SID = 'enter_twilio_account_sid'
TWILIO_AUTH_TOKEN = 'enter_twilio_auth_token'
TWILIO_FROM_NUM = 'enter_twilio_from_number'
TWILIO_TO_NUM = 'enter_to_number'

# vaccine location detail
TARGET_URL = 'https://www.vaccinespotter.org/CA/?zip=947043&radius=50'


def scrape_location(url):
    """ Scrapes for appointments at location
    """
    browser = webdriver.Chrome(executable_path=r'/chromedriver')
    browser.get(url)
    time.sleep(5)
    html_source = browser.page_source
    
    no_appt = browser.find_element_by_xpath("//div[contains(@class, 'alert alert-warning')]").is_displayed()
    browser.quit()
    return no_appt

def send_msg(msg):
    """ Sends message via Twilio
    """
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(from_=TWILIO_FROM_NUM, to=TWILIO_TO_NUM, body=msg)


def check_for_availability():
    """ Check if there is an availability vaccine appointments in area.
    """
    no_appt = scrape_location(TARGET_URL)
    if not no_appt:
        message = "There are appointments available. Please go to " + TARGET_URL
        send_msg(message)

def get_vaccinate(argv):
    global TARGET_URL
    state, zipcode, radius = argv[1:]
    TARGET_URL = 'https://www.vaccinespotter.org/{}/?zip={}&radius={}'.format(state, zipcode, radius)

    check_for_availability()
    schedule.every(30).minutes.do(check_for_availability)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    get_vaccinate(sys.argv)