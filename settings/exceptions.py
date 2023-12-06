"""Модуль для обработки ошибок приложения."""


class CantGetCoordinates(Exception):
    """Program can't get current GPS coordinates."""


class ApiServiceError(Exception):
    """Program can't get current weather."""
