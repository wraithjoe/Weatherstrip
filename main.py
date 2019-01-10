from weather import Weather, Unit
from weatherclass import WeatherDataclass
import  time
from neopixel import *

# LED strip configuration:
LED_COUNT      = 144      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

weather = Weather(unit=Unit.FAHRENHEIT)

lookup = weather.lookup(12780598)
forecasts = lookup.forecast
condition = lookup.condition
#for forecast in forecasts:
#    print(forecast.text)
#    print(forecast.date)

    #print(forecast.high)
    #print(forecast.low)

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
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
        print("Current Conditions:{}".format(currentWeather.Current_weather))
        pixelNo = 0
        while(pixelNo < LED_COUNT):

            if(currentWeather.pixels[pixelNo].on):
                strip.setPixelColor(pixelNo,Color(currentWeather.pixels[pixelNo].color.red,currentWeather.pixels[pixelNo].color.green, currentWeather.pixels[pixelNo].color.blue))
            pixelNo = pixelNo + 1





    time.sleep(1)
    count = count +1










#TODO: Create function to update LED Strip with WeatherDataClass as input


