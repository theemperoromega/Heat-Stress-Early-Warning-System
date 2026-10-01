import math
from xml.parsers.expat import model



#This function calculates the Wet Bulb Globe Temperature (WBGT) based on temperature, actual vapor pressure, and windspeed. The WBGT is a measure of heat stress in direct sunlight, which takes into account temperature, humidity, wind speed, sun angle, and cloud cover (solar radiation).

def calculate_wbgt(temperature, actual_vapor_pressure, windspeed):
    temperature: float, actual_vapor_pressure:float, windspeed: float = 0.0



# NOTE: temperature is in Clelsius, actual_vapor_pressure is in kPa, and windspeed is in m/s. The function returns the WBGT value in Celsius."""

VaporPressure = 0.6108 * math.exp((17.27 * temperature) / (temperature + 237.3))
rh = (actual_vapor_pressure / VaporPressure) * 100
wbgt = 0.7 * temperature + 0.3 * (temperature * rh / 100)

windspeed
relative_humidity = rh

def wbgt_bom_simple(temperature, actual_vapor_pressure, windspeed):

#This function calculates the Wet Bulb Globe Temperature (WBGT) based on temperature, actual vapor pressure, and windspeed. The WBGT is a measure of heat stress in direct sunlight, which takes into account temperature, humidity, wind speed, sun angle, and cloud cover (solar radiation).
 
    temperature: float, actual_vapor_pressure:float, windspeed: float = 0.0

    """ NOTE: temperature is in Clelsius, actual_vapor_pressure is in kPa, and windspeed is in m/s. The function returns the WBGT value in Celsius."""

    VaporPressure = 0.6108 * math.exp((17.27 * temperature) / (temperature + 237.3))
    rh = (actual_vapor_pressure / VaporPressure) * 100
    wbgt = 0.7 * temperature + 0.3 * (temperature * rh / 100)


def calculate_vapor_pressure(temp_c, rh_pct):
    return 0.6108 * math.exp((17.27 * temp_c) / (temp_c + 237.3))

def wbgt_bom_simple(temp_c, rh_pct):
     
def calculate_wet_bulb_stull(temp_c, rh_pct):

def estimate_globe_temperature(temp_c, rh_pct, wind_speed_ms, solar_radiation_wm2):

def wbgt_enhanced(...):