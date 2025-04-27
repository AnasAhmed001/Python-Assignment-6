class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        """
        Convert Celsius temperature to Fahrenheit
        Formula: F = (C * 9/5) + 32
        """
        return (c * 9/5) + 32
    
    @staticmethod
    def fahrenheit_to_celsius(f):
        """
        Convert Fahrenheit temperature to Celsius
        Formula: C = (F - 32) * 5/9
        """
        return (f - 32) * 5/9


# Test the static methods
# No need to create an instance to use static methods
print("Temperature Conversions:")
celsius_temps = [0, 25, 37, 100]

for temp_c in celsius_temps:
    temp_f = TemperatureConverter.celsius_to_fahrenheit(temp_c)
    print(f"{temp_c}°C = {temp_f:.1f}°F")

# You can also call static methods from an instance (though not typical)
converter = TemperatureConverter()
print("\nUsing instance (uncommon):")
print(f"100°C = {converter.celsius_to_fahrenheit(100):.1f}°F")

# Converting from Fahrenheit to Celsius
print("\nFahrenheit to Celsius:")
fahrenheit_temps = [32, 68, 98.6, 212]

for temp_f in fahrenheit_temps:
    temp_c = TemperatureConverter.fahrenheit_to_celsius(temp_f)
    print(f"{temp_f}°F = {temp_c:.1f}°C")
