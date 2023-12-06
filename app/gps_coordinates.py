import json
from dataclasses import dataclass
from urllib.error import URLError
from urllib.request import urlopen

from settings.exceptions import CantGetCoordinates
from settings.config import USE_ROUNDED_COORDS


@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float


def get_gps_coordinate() -> Coordinates:
    """Модуль для получения gps координат по IP."""
    coordinates = _get_ip_coordinates()
    return _round_coordinates(coordinates)


def _get_ip_coordinates() -> Coordinates:
    data = _get_coordinates_data()
    coordinates = _parse_coordinates(data)
    return coordinates


def _get_coordinates_data() -> dict:
    try:
        data = json.load(urlopen("http://ipinfo.io/json"))
    except URLError:
        raise CantGetCoordinates
    return data


def _parse_coordinates(data: dict) -> Coordinates:
    try:
        latitude = data['loc'].split(',')[0]
        longitude = data['loc'].split(',')[1]
    except Exception:
        raise CantGetCoordinates
    return Coordinates(latitude=_parse_float_coordinate(latitude),
                       longitude=_parse_float_coordinate(longitude))


def _parse_float_coordinate(value: str) -> float:
    try:
        return float(value)
    except ValueError:
        raise CantGetCoordinates


def _round_coordinates(coordinates: Coordinates) -> Coordinates:
    if not USE_ROUNDED_COORDS:
        return coordinates
    return Coordinates(*map(lambda c: round(c, 1),
                            [coordinates.latitude, coordinates.longitude]))


if __name__ == '__main__':
    print(get_gps_coordinate())
