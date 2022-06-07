import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["currency"])
async def start_command(message: types.Message):
    await message.reply("Актуальний курс валют PrivatBank: \n"
                        "Євро - /EUR   \n"
                        "Злотий - /PLN  \n"
                        "Біткоїн - /BTC  \n"
                        "Долар США - /USD \n"
    )

@dp.message_handler(commands=["info"])
async def start_command(message: types.Message):
    await message.reply("Брати парасольку чи не брати? Це питання виникає у всіх людей, які не хочуть зіпсувати собі настрій і одяг в тому числі. "
                        "Ми плануємо свій день і хочемо бути готовими до всього, навіть до того, що змінити не можливо – Погоду. "
                        "Звичайно ж, можна моніторити прогнози, але це не зовсім зручно. "
                        "І, чесно кажучи, мало хто буде присвячувати стільки часу постійному моніторингу погодних сайтів. "
                        "А насправді, цього робити і не треба, якщо у вас є наш WeatherBot."
                        "Все що вам знадобиться - вписати назву вашого населеного пункту і наша програма залюбки видасть вам"
                        "останнє зведення погоди з офіційного сайту National Aeronautics and Space Administration.")


@dp.message_handler(commands=["contact"])
async def start_command(message: types.Message):
    await message.reply(f"Якщо у Вас є унікальні пропозиції з покращення нашого сервісу чи виявили помилку, звертайтесь сюди:\n"
                        f"parlamentteamwork@gmail.com\n"
                        f"Ми відповімо якнайшвидше.\n"
                        f"З повагою, команда Parlament™.")


@dp.message_handler(commands=["PLN"])
async def start_command(message: types.Message):
        await message.reply("Обмінник:\n💰Купівля: 7.90 UAH\n💸Продаж: 8.20 UAH\n"
                           f"Чорний ринок: \n💰Купівля: 7.98 UAH\n💸Продаж: 8.15 UAH")


@dp.message_handler(commands=["EUR"])
async def start_command(message: types.Message):
     await message.reply("Обмінник:\n💰Купівля: 31.31 UAH\n💸Продаж: 31.49 UAH\n"
                        f"Чорний ринок: \n💰Купівля: 37.86 UAH\n💸Продаж: 35.75 UAH")

@dp.message_handler(commands=["USD"])
async def start_command(message: types.Message):
        await message.reply("Обмінник:\n💰Купівля: 29.25 UAH\n💸Продаж: 29.26 UAH\n"
                           f"Чорний ринок: \n💰Купівля: 34.48 UAH\n💸Продаж: 32.24 UAH")


@dp.message_handler(commands=["BTC"])
async def start_command(message: types.Message):
        await message.reply("Обмін в USD:\n💰Купівля: 29614.80 USD\n💸Продаж: 29614.80 USD\n"
                           f"Обмін в EUR:\n💰Купівля: 27722.41 EUR\n💸Продаж: 27722.41 EUR")


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привіт, відішли назву населеного пункту і я видам тобі прогноз погоди.\nДля більш детальної інформації про нашого бота використовуй - /info.\nДля перегляду актуального курсу валют - /currency.")


@dp.message_handler(commands=["time"])
async def start_command(message: types.Message):
    await message.reply(f"Точний час: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}.\n")

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
            wd = "Виглянь у вікно, не можу описати словами."

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        await message.reply(
              f"Населений пункт: {city}\n"
              f"Температура: {cur_weather} C° | {wd}\n"
              f"Вітер: {wind} м/с\n"
              f"Вологість: {humidity}%\n"
              f"Тривалість дня: {length_of_the_day}\n"
              f"Світанок: {sunrise_timestamp}\n"
              f"Захід сонця: {sunset_timestamp}\n"
              f"Атмосферний тиск: {pressure-260} мм.рт.ст""\n"
              f"Рowered by Parlament Team\n"
              f"Dev: @bodya_respect\n"
              f"Гарного дня!\n"
              )

    except:

        await message.reply("🤔 Перевір грамотність написаного!")

@dp.message_handler(commands=["stop"])
async def stop(message):
  if message.from_user.username == cfg.Father:
    pid = str(os.getpid())
    stoper = open('ozerx/stoper.bat', 'w')
    stoper.write("Taskkill /PID " + pid + " /F")
    stoper.close()
    os.system('C:/Users/smp/Desktop/SMP/ozerx/stoper.bat')
  else:
    await message.reply("У вас недостатньо прав!")


if __name__ == '__main__':
    executor.start_polling(dp)