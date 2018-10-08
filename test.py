from weather import Weather, Unit
from weatherclass import WeatherDataclass
import  time
weather = Weather(unit=Unit.FAHRENHEIT)

lookup = weather.lookup(12780598)
forecasts = lookup.forecast
condition = lookup.condition
#for forecast in forecasts:
#    print(forecast.text)
#    print(forecast.date)

    #print(forecast.high)
    #print(forecast.low)


#print(condition.temp)
weather = Weather(unit=Unit.FAHRENHEIT)
count = 0
while (0 < 1):
    if(count == 0 or count == 30):
        lookup = weather.lookup(12780598)
        forecasts = lookup.forecast
        condition = lookup.condition
        print(int(forecasts[0].low))
        currentWeather = WeatherDataclass(int(forecasts[0].low), int(forecasts[0].high), int(condition.temp), condition.text)
        print("High Temp Dec:{}, High Temp in Bin:{}".format(currentWeather.High_temp, currentWeather.binary_high_temp))
        print("Low Temp Dec:{}, Low Temp in Bin:{}".format(currentWeather.Low_temp, currentWeather.binary_low_temp))
        print("Current Temp Dec:{}, Current Temp in Bin:{}".format(currentWeather.Current_temp, currentWeather.binary_current_temp))
        print("Current Conditions{}".format(currentWeather.Current_weather))

    time.sleep(1)
    count = count +1




