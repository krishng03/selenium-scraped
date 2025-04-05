from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import json

print('Creating driver...')
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
print('Driver Created✅')

URL = 'https://www.wunderground.com/weather/in/new-delhi'

print('Fetching data...')
driver.get(URL)

print('Fetched data✅')
print('Extracting info.... Please Wait...')

RETURN_OBJECT = {}

current_temp = driver.find_element(By.CSS_SELECTOR, 'div.current-temp').text
RETURN_OBJECT['current_temp'] = current_temp

feels_like_temp = driver.find_element(By.CSS_SELECTOR, 'div.feels-like').text
RETURN_OBJECT['feels_like_temp'] = feels_like_temp

weather_quickie = driver.find_element(By.CSS_SELECTOR, 'p.weather-quickie').text
RETURN_OBJECT['weather_quickie'] = weather_quickie

LIST_OF_CARDS = []

precipitation_title = driver.find_element(By.ID, 'precipTopBar').text
precipitation_body = driver.find_element(By.ID, 'precipBarChart')
precipitation_text = (' ').join([val.text for val in precipitation_body.find_elements(By.CSS_SELECTOR, 'text')])

LIST_OF_CARDS.append({
    'title': precipitation_title, 
    'body': precipitation_text
})

air_quality_title = driver.find_element(By.ID, 'aqTopBar').text
air_quality_body = driver.find_element(By.ID, 'aqBarChart')
air_quality_text = (' ').join([val.text for val in air_quality_body.find_elements(By.CSS_SELECTOR, 'text')])

LIST_OF_CARDS.append({
    'title': air_quality_title, 
    'body': air_quality_text
})

uv_index_title = driver.find_element(By.ID, 'uvTopBar').text
uv_index_body = driver.find_element(By.ID, 'uvBarChart')
uv_index_text = (' ').join([val.text for val in uv_index_body.find_elements(By.CSS_SELECTOR, 'text')])

LIST_OF_CARDS.append({
    'title': uv_index_title, 
    'data': uv_index_text
})

RETURN_OBJECT['cards'] = LIST_OF_CARDS

ADDITIONAL_DATA = []

additional_data = driver.find_elements(By.CSS_SELECTOR, 'div.additional-conditions div.content div.row')
for data in additional_data:
    list = data.text.split('\n')
    ADDITIONAL_DATA.append({
        'param': list[0].lower(),
        'value': list[1]
    })

RETURN_OBJECT['additional_data'] = ADDITIONAL_DATA

low_high_temp = driver.find_elements(By.CSS_SELECTOR, 'div.city-almanac div.content div.collapse')[1:3]
for data in low_high_temp:
    list = data.text.split('\n')[:2]
    RETURN_OBJECT[f'{list[0].lower()}_temp'] = list[1]

driver.close()
print('Closed driver!')

with open('weather_data.json', 'w') as file:
    json.dump(RETURN_OBJECT, file, indent=2)

print('JSON file saved successfully✅')