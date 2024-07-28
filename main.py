import asyncio
from telegram import Bot
import os
from weather import Weather

API_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.environ.get("OWM_API_KEY")
MY_LAT = 51.497700
MY_LONG = -0.018580

BOT_TOKEN = os.environ.get("TLGRM_BOT_TOKEN")
bot_chat_id = 74897720

weather = Weather(MY_LAT, MY_LONG, API_KEY)
data = weather.get_weather_data()
# print(data)

rain, rain_description, rain_temp_min, rain_temp_max, rain_humidity = weather.will_rain()
snow, snow_description, snow_temp_min, snow_temp_max, snow_humidity = weather.will_snow()
visibility, visibility_description, visibility_temp_min, visibility_temp_max, visibility_humidity \
    = weather.will_have_low_visibility()
clear, clear_description, clear_temp_min, clear_temp_max, clear_humidity = weather.will_be_clear()
cloudy, cloudy_description, cloudy_temp_min, cloudy_temp_max, cloudy_humidity = weather.will_be_cloudy()


async def telegram_bot_sendtext(bot_message):
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=bot_chat_id, text=bot_message)


# async def telegram_bot_sendphoto(photo_url):
#     await bot.send_photo(chat_id=bot_chat_id, photo=photo_url)


async def main():
    if rain:
        await telegram_bot_sendtext(
            f"12-HOUR FORECAST:\n\n"
            f"High temperature: {rain_temp_max}ºC .\nLow temperature: {rain_temp_min}ºC.\n"
            f"Humidity: {rain_humidity}%.\n\n"
            f"It's going to be rainy later. The forecast is for {rain_description}. "
            f"Don't forget to bring an umbrella!☔️")

    if snow:
        await telegram_bot_sendtext(
            f"12-HOUR FORECAST:\n\n"
            f"High temperature: {snow_temp_max}ºC .\nLow temperature: {snow_temp_min}ºC.\n"
            f"Humidity: {snow_humidity}%.\n\n"
            f"It's going to snowy today. The forecast is for {snow_description}. "
            f"Don't forget to keep yourself warm!🥶")

    if visibility:
        await telegram_bot_sendtext(
            f"12-HOUR FORECAST:\n\n"
            f"High temperature: {visibility_temp_max}ºC .\nLow temperature: {visibility_temp_min}ºC.\n"
            f"Humidity: {visibility_humidity}%.\n\n"
            f"Visibility will be lower than usual today. The forecast is for {visibility_description}. "
            f"Take extra caution when crossing the road!🚶🏻‍️")

    if clear:
        await telegram_bot_sendtext(
            f"12-HOUR FORECAST:\n\n"
            f"High temperature: {clear_temp_max}ºC .\nLow temperature: {clear_temp_min}ºC.\n"
            f"Humidity: {clear_humidity}%.\n\n"
            f"The skies will be clear today. The forecast is for {clear_description}. "
            f"Have fun and don't forget to wear sunscreen during the day! ☀️")

    if cloudy:
        await telegram_bot_sendtext(
            f"12-HOUR FORECAST:\n\n"
            f"High temperature: {cloudy_temp_max}ºC .\nLow temperature: {cloudy_temp_min}ºC.\n"
            f"Humidity: {cloudy_humidity}%.\n\n"
            f"The weather calls for cloudy skies in the next 12 hours. The forecast is for {cloudy_description}. "
            f"It may be cloudy but don't forget to wear sunscreen during the day! ☀️")


if __name__ == "__main__":
    asyncio.run(main())
