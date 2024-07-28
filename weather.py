import requests


class Weather:
    API_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

    def __init__(self, lat, lon, api_key, cnt=4, units="metric"):
        self.api_key = api_key
        self.lat = lat
        self.lon = lon
        self.cnt = cnt  # number of 3-hour data points
        self.units = units
        self.forecast = self.get_weather_data()

    def get_weather_data(self):
        weather_parameters = {
            "lat": self.lat,
            "lon": self.lon,
            "appid": self.api_key,
            "cnt": self.cnt,
            "units": self.units
        }

        response = requests.get(url=self.API_ENDPOINT, params=weather_parameters)
        response.raise_for_status()
        return response.json()["list"]

    def will_rain(self):
        for hourly_data in self.forecast:
            condition_code = hourly_data["weather"][0]["id"]
            condition_description = hourly_data["weather"][0]["description"]
            temp_min = hourly_data["main"]["temp_min"]
            temp_max = hourly_data["main"]["temp_max"]
            humidity = hourly_data["main"]["humidity"]
            if condition_code < 600:
                return True, condition_description, temp_min, temp_max, humidity
        return False, None, None, None, None

    def will_snow(self):
        for hourly_data in self.forecast:
            condition_code = hourly_data["weather"][0]["id"]
            condition_description = hourly_data["weather"][0]["description"]
            temp_min = hourly_data["main"]["temp_min"]
            temp_max = hourly_data["main"]["temp_max"]
            humidity = hourly_data["main"]["humidity"]
            if 600 <= condition_code < 700:
                return True, condition_description, temp_min, temp_max, humidity
        return False, None, None, None, None

    def will_have_low_visibility(self):
        for hourly_data in self.forecast:
            condition_code = hourly_data["weather"][0]["id"]
            condition_description = hourly_data["weather"][0]["description"]
            temp_min = hourly_data["main"]["temp_min"]
            temp_max = hourly_data["main"]["temp_max"]
            humidity = hourly_data["main"]["humidity"]
            if 700 <= condition_code < 800:
                return True, condition_description, temp_min, temp_max, humidity
        return False, None, None, None, None

    def will_be_clear(self):
        for hourly_data in self.forecast:
            condition_code = hourly_data["weather"][0]["id"]
            condition_description = hourly_data["weather"][0]["description"]
            temp_min = hourly_data["main"]["temp_min"]
            temp_max = hourly_data["main"]["temp_max"]
            humidity = hourly_data["main"]["humidity"]
            if condition_code == 800:
                return True, condition_description, temp_min, temp_max, humidity
        return False, None, None, None, None

    def will_be_cloudy(self):
        for hourly_data in self.forecast:
            condition_code = hourly_data["weather"][0]["id"]
            condition_description = hourly_data["weather"][0]["description"]
            temp_min = hourly_data["main"]["temp_min"]
            temp_max = hourly_data["main"]["temp_max"]
            humidity = hourly_data["main"]["humidity"]
            if condition_code > 800:
                return True, condition_description, temp_min, temp_max, humidity
        return False, None, None, None, None