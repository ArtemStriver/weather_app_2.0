import json
import ssl
import urllib.request
from datetime import datetime
from enum import Enum
from json import JSONDecodeError
from typing import NamedTuple, Literal
from urllib.error import URLError

import config
from exceptions import ApiServiceError
from gps_coordinates import Coordinates

Celsius = float


class WeatherType(Enum):
    THUNDERSTORM = 'Гроза'
    DRIZZLE = 'Изморозь'
    RAIN = 'Дождь'
    SNOW = 'Снег'
    CLEAR = 'Ясно'
    CLOUDS = 'Облачно'
    FOG = 'Туман'


class Weather(NamedTuple):
    temperature: Celsius
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str


def get_weather_data(coordinates: Coordinates) -> Weather:
    """Модуль получения данных о погоде по gps координатам."""
    openweather_response = _get_openweather_response(latitude=coordinates.latitude,
                                                     longitude=coordinates.longitude)
    weather = _parce_openweather_response(openweather_response)
    return weather


def _get_openweather_response(latitude: float, longitude: float) -> str:
    # ssl._create_default_https_context = ssl._create_unverified_context
    url = config.OPENWEATHER_URL.format(latitude=latitude, longitude=longitude)
    try:
        return urllib.request.urlopen(url).read()
    except URLError:
        raise ApiServiceError


def _parce_openweather_response(openweather_response: str) -> Weather:
    try:
        openweather_dict = json.loads(openweather_response)
    except JSONDecodeError:
        raise ApiServiceError
    return Weather(
        temperature=_parse_temperature(openweather_dict),
        weather_type=_parse_weather_type(openweather_dict),
        sunrise=_parse_sun_time(openweather_dict, 'sunrise'),
        sunset=_parse_sun_time(openweather_dict, 'sunset'),
        city=_parse_city(openweather_dict),
    )


def _parse_temperature(openweather_dict: dict) -> Celsius:
    return round(openweather_dict['main']['temp'], 1)


def _parse_weather_type(openweather_dict: dict) -> WeatherType:
    try:
        weather_type_id = str(openweather_dict["weather"][0]["id"])
    except (IndexError, KeyError):
        raise ApiServiceError
    weather_types = {
        "1": WeatherType.THUNDERSTORM,
        "3": WeatherType.DRIZZLE,
        "5": WeatherType.RAIN,
        "6": WeatherType.SNOW,
        "7": WeatherType.FOG,
        "800": WeatherType.CLEAR,
        "80": WeatherType.CLOUDS
    }
    for _id, _weather_type in weather_types.items():
        if weather_type_id.startswith(_id):
            return _weather_type
    raise ApiServiceError


def _parse_sun_time(openweather_dict: dict, time: Literal['sunrise'] | Literal['sunset']) -> datetime:
    return datetime.fromtimestamp(openweather_dict['sys'][time])


def _parse_city(openweather_dict: dict) -> str:
    try:
        return openweather_dict['name']
    except KeyError:
        raise ApiServiceError


if __name__ == '__main__':
    print(get_weather_data(Coordinates(latitude=58.0105, longitude=56.2502)))
