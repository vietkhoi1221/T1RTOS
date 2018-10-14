import pyowm
from googletrans import Translator
owm = pyowm.OWM('a3ac1a7d13422b804a326029769907f2')
translator = Translator()
def common(city):
    global observation,weather,status,temperature,wind_speed,humidity,pressure
    observation = owm.weather_at_place(city)
    weather = observation.get_weather()
    status = translator.translate(weather.get_status(), dest='vi')
    temperature = weather.get_temperature('celsius')['temp']
    wind_speed = weather.get_wind()['speed']
    humidity = weather.get_humidity()
    pressure = weather.get_pressure()['press']
def completeWeather(city):
    global wind_speed,status,temperature,humidity,pressure
    common(city)
    print("Thời tiết tại "+city+" "+status.text+" với nhiệt độ "+str(temperature)+" độ C, "+"tốc độ gió "+str(wind_speed)+" m/s, "+"độ ẩm "+str(humidity)+" %"+" và áp suất "+str(pressure)+" atm.\n")
    return "Thời tiết tại "+city+" "+status.text+" với nhiệt độ "+str(temperature)+" độ C, "+"tốc độ gió "+str(wind_speed)+" mét trên giây, "+"độ ẩm "+str(humidity)+" %"+" và áp suất "+str(pressure)+" atmosphere."
