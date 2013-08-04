from forecastio import Forecastio

forecast = Forecastio("af533cce990d681fbefe188f902a6619")
result = forecast.load_forecast(48, 13)

byHour = forecast.get_hourly()
print result

for stuff in byHour.data:
    print stuff