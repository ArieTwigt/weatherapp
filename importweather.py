from weather import Weather
import pandas as pd
import emoji


def getweather(city):
    if city is None:
        city = 'paris'

    weather = Weather()

    location = weather.lookup_by_location(city)

    forecast_date = []
    forecast_text = []
    forecast_high = []
    forecast_low = []

    forecasts = location.forecast

    for forecast in forecasts:
        forecast_date.append(forecast.date)
        forecast_text.append(forecast.text)
        forecast_high.append(forecast.high)
        forecast_low.append(forecast.low)

    def geticons(argument):
        switcher = {
            "Cloudy": emoji.emojize(':cloud:'),
            "Mostly Cloudy": emoji.emojize(':cloud:'),
            "Partly Cloudy": emoji.emojize(':cloud:'),
            "Rain": emoji.emojize(':cloud_with_rain:'),
            "Showers": emoji.emojize(':cloud_with_rain:'),
            "Fair": emoji.emojize(':sun_behind_cloud:'),
            "Mostly Sunny": emoji.emojize(':sun:'),
            "Breezy": emoji.emojize(':wind_face:'),
            "Scattered Thunderstorms": emoji.emojize(':cloud_with_lightning:'),
            "Scattered Showers": emoji.emojize(':cloud_with_rain:')
        }
        return switcher.get(argument, "nothing")

    forecast_icon = []

    for text in forecast_text:
        icon = geticons(text)
        forecast_icon.append(icon)

    forecast_celcius = []

    for i in range(0, len(forecast_high)):
        high = forecast_high[i]
        low = forecast_low[i]
        celcius = (int(high) + int(low)) / 2
        celcius_str = "˚C " + str(celcius)
        forecast_celcius.append(celcius_str)

    forecast_text_icon = []

    for i in range(0, len(forecast_text)):
        text = forecast_text[i]
        icon = forecast_icon[i]
        combined = icon + " " + text
        forecast_text_icon.append(combined)

    weather_df = pd.DataFrame({
        'Date': forecast_date,
        'Forecast': forecast_text_icon,
        '˚C': forecast_celcius
    })

    weather_df.set_index('Date', inplace=True)

    return weather_df
