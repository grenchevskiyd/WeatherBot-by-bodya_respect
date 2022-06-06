import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["price"])
async def start_command(message: types.Message):
    await message.reply("Актуальний курс валют НБУ:\n"
                        f"1 USD = 29.2549 UAH\n"
                        f"1 EUR = 31.3877 UAH\n"
                        f"1 PLN = 6.87510 UAH\n"
                        f"1 BTC =  31,290 USD\n"
                        f"1 RUB = За кораблем\n"
                        f"🇺🇦Cлава Україні!")


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привіт! Напиши мені назву населеного пункту!")

@dp.message_handler()
async def get_weather(message: types.Message):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Хмарно \U00002601",
        "Rain": "Дощ \U00002614",
        "Drizzle": "Мряка \U00002614",
        "Thunderstorm": "Злива \U000026A1",
        "Snow": "Сніг \U0001F328",
        "Mist": "Густий туман \U0001F32B"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Виглянь у вікно, не розумію що там!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Населений пункт: {city}\n"
              f"Температура: {cur_weather} C° | {wd}\n"
              f"Вологість: {humidity}%\n"
              f"Атмосферний тиск: {pressure-260} мм.рт.ст""\n"
              f"Вітер: {wind} м/с\n"
              f"Світанок: {sunrise_timestamp}\n"
              f"Захід сонця: {sunset_timestamp}\n"
              f"Тривалість дня: {length_of_the_day}\n"
              f"***Гарного дня!***\n"
              f"Developer: @bodya_respect \n"
              f"Рowered by Parlament Team"
              )

    except:

        await message.reply("\U00002620 Перевір грамотність написаного! \U00002620")


if __name__ == '__main__':
    executor.start_polling(dp)