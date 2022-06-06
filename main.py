import requests
import datetime
from pprint import pprint
from config import open_weather_token
from config import banktoken


def currency(valuta, banktoken):

        r = requests.get(
            f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
        )
        currenc = r.json()
        pprint(currenc)

        valuta = currenc["сс"]

        print(f"Доллар: {valuta}")



def pohodka(city, open_weather_token):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Хмарно \U00002601",
        "Rain": "Дощ \U00002614",
        "Drizzle": "Мряка \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Сніг \U0001F328",
        "Mist": "Густий туман \U0001F32B"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Заглянь у вікно, не розумію, що коїться..."

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        print(f"   {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
              f"Місто: {city}\nТемпература: {cur_weather}C° {wd}\n"
              f"Вологість: {humidity}%\nАтмосферний тиск: {pressure} мм.рт.ст\nВітер: {wind} м/с\n"
              f"Світанок: {sunrise_timestamp}\nЗахід: {sunset_timestamp}\nТривалість дня: {length_of_the_day}\n"
              f"Хорошого дня!")
        print("Developer: @bodya_respect\nРowered by Parlament Team")


    except Exception as ex:
        print(ex)
        print("Перевірте грамотність написаного")


def main():
    valuta = input("Введи валюту: ")
    currency(valuta, banktoken)
    city = input("Введіть назву населеного пункту: ")
    pohodka(city, open_weather_token)


if __name__ == '__main__':
    main()
