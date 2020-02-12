import argparse
import datetime

import requests

from bot.services.secret_key_of_project import openweathermap_api_key

def print_weather_for_day(city):
	api_key = openweathermap_api_key
	responce = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api_key}')
	responce=responce.json()
	if responce['cod'] == '200':
		day = responce['list'][0]['dt_txt']
		day = datetime.datetime.strptime(day, '%Y-%m-%d %H:%M:%S')
		day = day.strftime('%d.%m.%Y')
		temp = responce['list'][0]['main']['temp']
		temp = ('+' if round(temp) > 0 else '') + str(round(temp))
		weather = responce['list'][0]['weather'][0]['description']
		text_to_return = f'{day}  {temp}  {weather}'
	else:
		text_to_return = 'Неверный параметр. Попробуйте ещё.'
	return text_to_return