# VaccineAlerter
COVID-19 Vaccine Appointment Bot use Selenium and Python3.

COVID-19 vaccine appointments have been notoriously hard to get. With no set schedule for when new appointment times are released, I found myself stalking my local vaccine appointment page every few hours. And after asking around, I found that I wasn't the only one struggling with this issue.

So thus, I developed a script that periodically checks for COVID-19 vaccine appointments at local pharmacies. It will scrape vaccinespotter.org for available times around you and will send you a text message if one is found within the given radius.

## Installation and Usage
Must use python3 or later.

Grab your local copy.
```
git clone https://github.com/johnnyhuang97/VaccineAlerter.git
```
Install dependencies, including.
```
pip install -r requirements.txt
```

Obtain your Twilio account SID, auth token, and phone number. fill out the corresponding variables in `get_vaccine_alert.py` along with the number you want to send your alerts to.
```python3
TWILIO_ACCOUNT_SID = 'enter_twilio_account_sid'
TWILIO_AUTH_TOKEN = 'enter_twilio_auth_token'
TWILIO_FROM_NUM = 'enter_twilio_from_number'
TWILIO_TO_NUM = 'enter_to_number'
```
Run the bot in the background.
```
python3 get_vaccine_alert.py arg1 arg2 arg3 &
```
where
`arg1` is the 2 letter abbrevation of your state, all in uppercase. You can check `us_state_abbrev.py` for abbrevations.
`arg2` is your 5 digit zipcode
`arg3` is the radius in miles that you wish to search from. Either 5, 10, 25, 50, or 100.
