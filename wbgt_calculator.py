import math



"""This function calculates the Wet Bulb Globe Temperature (WBGT) based on temperature, actual vapor pressure, and windspeed. The WBGT is a measure of heat stress in direct sunlight, which takes into account temperature, humidity, wind speed, sun angle, and cloud cover (solar radiation)."""

def calculate_wbgt(temperature, actual_vapor_pressure, windspeed):
    temperature: float, actual_vapor_pressure:float, windspeed: float = 0.0


""" NOTE: temperature is in Clelsius, actual_vapor_pressure is in kPa, and windspeed is in m/s. The function returns the WBGT value in Celsius."""

VaporPressure = 0.6108 * math.exp((17.27 * temperature) / (temperature + 237.3))
rh = (actual_vapor_pressure / VaporPressure) * 100
wbgt = 0.7 * temperature + 0.3 * (temperature * rh / 100)

windspeed
relative_humidity = rh

def wbgt_bom_simple(temperature, actual_vapor_pressure, windspeed):
    """This function calculates the Wet Bulb Globe Temperature (WBGT) based on temperature, actual vapor pressure, and windspeed. The WBGT is a measure of heat stress in direct sunlight, which takes into account temperature, humidity, wind speed, sun angle, and cloud cover (solar radiation)."""
    temperature: float, actual_vapor_pressure:float, windspeed: float = 0.0

    """ NOTE: temperature is in Clelsius, actual_vapor_pressure is in kPa, and windspeed is in m/s. The function returns the WBGT value in Celsius."""

    VaporPressure = 0.6108 * math.exp((17.27 * temperature) / (temperature + 237.3))
    rh = (actual_vapor_pressure / VaporPressure) * 100
    wbgt = 0.7 * temperature + 0.3 * (temperature * rh / 100)


def calc
def
def


