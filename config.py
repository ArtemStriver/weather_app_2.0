USE_ROUNDED_COORDS = False
OPENWEATHER_API = "6458174fba0708611deace21f1e29b77"
OPENWEATHER_URL = (
        'https://api.openweathermap.org/data/2.5/weather?'
        'lat={latitude}&lon={longitude}'
        '&appid=' + OPENWEATHER_API + '&lang=ru&'
        'units=metric'
)
