from skyfield.api import load, wgs84
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

planets = load('de421.bsp')

earth = planets['earth']
moon = planets['moon']

ts = load.timescale()

print("=" * 55)
print("                   MOON POSITION FINDER")
print("=" * 55)

print("\nEnter your obsrving location.")

lat = float(input("Latitude: "))
lon = float(input("Longitude: "))

observer = earth + wgs84.latlon(lat, lon)

print("\nTime Selection")
print("1. Use current UTC time")
print("2. Enter a specific UTC date and time")

choice = input("Choose 1 or 2: ")

if choice == "1":
    t = ts.now()
    time_description = "Current UTC time"

elif choice == "2":
    date_input = input("Enter date(YYYY-MM-DD): ")
    time_input = input("Enter time(HH:MM): ")

    year, month, day = map(int, date_input.split("-"))
    hour, minute = map(int, time_input.split(":"))

    t = ts.utc(year, month, day, hour, minute)

    time_description = (f"{date_input} {time_input} UTC")

else:
    print("Invalid choice. Using current UTC time.")

    t = ts.now()

    time_description = "Current UTC time"

astrometric = observer.at(t).observe(moon)
apparent = astrometric.apparent()

altitude_angle, azimuth_angle, distance = apparent.altaz()

altitude = altitude_angle.degrees
azimuth = azimuth_angle.degrees
distance_km = distance.km

if altitude > 0:
    visibility = "Above the horizon"
else:
    visibility = "Below the horizon"

if altitude < 0:
    quality = "Not visible"
elif altitude < 10:
    quality = "Very Low altitude"
elif altitude < 20:
    quality = "Low altitude"
elif altitude < 45:
    quality = "Good observing altitude"
else:
    quality = "Excellent observing altitude"

def compass_direction(azimuth):
    if azimuth < 22.5 or azimuth >= 337.5:
        return "North"
    elif azimuth < 67.5:
        return "Northeast"
    elif azimuth < 112.5:
        return "East"
    elif azimuth < 157.5:
        return "Southeast"
    elif azimuth < 202.5:
        return "South"
    elif azimuth < 247.5:
        return "Southwest"
    elif azimuth < 292.5:
        return "West"
    else:
        return "Northwest"

direction = compass_direction(azimuth)

print("\n")
print("=" * 55)
print("                   MOON POSITION FINDER")
print("=" * 55)

print("\nObserver")
print("-" * 55)

print(f"Latitude: {lat:.4f}°")
print(f"Longitude: {lon:.4f}°")
print(f"Time: {time_description}")

print("\nMoon Information")
print("-" * 55)

print(f"Altitude: {altitude:.2f}°")
print(f"Azimuth: {azimuth:.2f}°")
print(f"Direction: {direction}")
print(f"Distance: {distance_km:,.2f} km")

print("\nVisibility")
print("-" * 55)

print(f"Status: {visibility}")
print(f"Quality: {quality}")

radius = 90 - altitude

theta = np.radians(azimuth)

fig = plt.figure(figsize = (8, 8))
# 111 -> 1 row, 1 col, 1st plot & circular graph
ax = fig.add_subplot(111, polar = True)

ax.set_theta_zero_location("N")
ax.set_theta_direction(-1) # clockwise increase the angle

if altitude >= 0:
    ax.scatter(theta, radius, s = 300, marker = "o")
    ax.text(theta, radius, "Moon", fontsize = 12)

ax.set_ylim(0, 90)
ax.set_yticks([0, 15, 30, 45, 60, 75, 90])
ax.set_yticklabels(["90°", "75°", "60°", "45°", "30°", "15°", "0°"])

plt.title("Moon Position in the Sky", pad = 25)

plt.show()