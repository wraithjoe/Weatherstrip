class WeatherDataclass:
    def __init__(self, Low_temp, High_temp, Current_Temp, Current_weather):
        self.Low_temp = Low_temp
        self.High_temp = High_temp
        self.Current_temp = Current_Temp
        self.Current_weather = Current_weather
        self.convert_to_binary()
        self.current_temp_color

        self.LED_color_data()
        binaryLine = self.binary_current_temp + self.binary_low_temp + self.binary_high_temp
        print(binaryLine)
        self.pixels = []
        x = 0
        for bit in binaryLine:
            if(bit == 0):
                on = False;
            else:
                on = True;

            if(0 <= x >= 7 ):
                self.pixels.append(Pixel(self.binary_current_temp, on))
            elif(8 <= x >= 15):
                self.pixels.append(Pixel(self.binary_low_temp, on))
            elif (16 <= x >= 23):
                self.pixels.append(Pixel(self.binary_high_temp, on))
            x = x + 1







    def convert_to_binary(self):

        self.binary_low_temp = "{0:b}".format(self.Low_temp)
        #Pad with zeros
        while(len(self.binary_low_temp) < 8):
            self.binary_low_temp = "0" + self.binary_low_temp

        self.binary_high_temp = "{0:b}".format(self.High_temp)
        # Pad with zeros
        while (len(self.binary_high_temp) < 8):
            self.binary_high_temp = "0" + self.binary_high_temp


        self.binary_current_temp = "{0:b}".format(self.Current_temp)
        # Pad with zeros
        while (len(self.binary_current_temp) < 8):
            self.binary_current_temp = "0" + self.binary_current_temp

    def LED_color_data(self):
        self.high_temp_color = self.definecolor(self.High_temp)
        self.low_temp_color  = self.definecolor(self.Low_temp)
        self.current_temp_color = self.definecolor(self.Current_temp)



    def definecolor(self,temperature):
        if(temperature > 67):  # 67 Degrees is mid point 100 degrees is highest on red spectrum
            if(temperature > 100):
                return(Color_data(255,0,0))
            else:
                tempred    = 255
                tempgreen  = 255-(255 * ((temperature-67)/(100-67)))
                tempblue   = tempgreen
                return(Color_data(tempred, tempgreen, tempblue))
        if(temperature < 67):
            if(temperature < -10):
                return(Color_data(0,0,255))
            else:
                tempred    = 255-(255 * (abs(temperature-67)/abs(-10-67)))
                tempgreen  = tempred
                tempblue   = 255
            return(Color_data(tempred, tempgreen, tempblue))
        else:
            return (Color_data(255,255,255))






class Color_data:
    def __init__(self, red, green, blue):
        self.red   = red
        self.green = green
        self.blue  = blue


class Pixel:
    def __init__(self, inColorData, lightOn):
        self.color =  inColorData
        self.on = lightOn