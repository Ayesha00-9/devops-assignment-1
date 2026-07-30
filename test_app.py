import pytest
from app import get_weather_advice


def test_cold_weather():
    result = get_weather_advice(5)
    assert "Wear warm clothes." in result
    assert "Drink hot beverages." in result


def test_pleasant_weather():
    result = get_weather_advice(15)
    assert "Carry a light jacket." in result
    assert "Weather is pleasant." in result


def test_hot_weather():
    result = get_weather_advice(25)
    assert "Wear comfortable clothes." in result
    assert "Stay hydrated." in result


def test_very_hot_weather():
    result = get_weather_advice(35)
    assert "Stay hydrated." in result
    assert "Wear light clothes." in result
    assert "Avoid direct sunlight." in result


def test_extreme_heat():
    result = get_weather_advice(42)
    assert "Extreme heat warning!" in result
    assert "Drink plenty of water." in result
    assert "Stay indoors if possible." in result
