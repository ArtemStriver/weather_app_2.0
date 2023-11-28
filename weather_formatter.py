from datetime import datetime

from weather_api_service import Weather, WeatherType


def get_weather_format(weather: Weather) -> str:
    """Модуль форматирования данных о погоде к единому виду."""
    return (f'{weather.city}, температура {weather.temperature}°C, '
            f'{weather.weather_type.value}\n'
            f'Восход: {weather.sunrise.strftime("%H:%M")}\n'
            f'Закат: {weather.sunset.strftime("%H:%M")}\n')


if __name__ == '__main__':
    print(get_weather_format(Weather(
        temperature=-25,
        weather_type=WeatherType.CLEAR,
        sunrise=datetime.fromisoformat('2023-12-01 08:00:00'),
        sunset=datetime.fromisoformat('2023-12-01 17:00:00'),
        city='Moscow'
    )))
