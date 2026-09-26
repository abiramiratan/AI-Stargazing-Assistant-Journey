from skyfield.api import load, wgs84
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

print("\n BEST STARGAZING TIME CALCULATOR")
print("-" * 50)

DATE = input("📅 Enter date (YYYY-MM-DD): ")

LOCATION_NAME = input("📍 Enter location name: ")

LATITUDE = float(input("🌐 Enter latitude: "))

LONGITUDE = float(input("🌐 Enter longitude: "))

TIMEZONE = input("🕐 Enter timezone (e.g. Asia/Kolkata): ")

print("\nCalculating astronomical events...")
print("Please wait...\n")

# Load Skyfield Data
ts = load.timescale()

eph = load("de421.bsp")

sun = eph["sun"]
earth = eph["earth"]

location = earth + wgs84.latlon(LATITUDE, LONGITUDE)

# Timezone
tz = ZoneInfo(TIMEZONE)

date_obj = datetime.strptime(DATE, "%Y-%m-%d").replace(tzinfo = tz)

next_day = date_obj + timedelta(days = 1)

# Convert Local Date to UTC
start_utc = date_obj.astimezone(timezone.utc)
end_utc = next_day.astimezone(timezone.utc)

# Calculate Sun Altitude
times = []
altitudes = []

current = start_utc

while current <= end_utc:

    t = ts.from_datetime(current)

    astrometric = location.at(t).observe(sun)
    apparent = astrometric.apparent()

    altitude, azimuth, distance = apparent.altaz()
    local_time = current.astimezone(tz)
    times.append(local_time)

    altitudes.append(altitude.degrees)
    current += timedelta(minutes=2)

# Find Solar Events
def find_crossing(target_altitude, direction):

    for i in range(len(altitudes) - 1):

        current_altitude = altitudes[i]
        next_altitude = altitudes[i + 1]

        if direction == "rising":

            if (current_altitude < target_altitude and next_altitude >= target_altitude):
                return times[i + 1]

        elif direction == "setting":

            if (current_altitude >= target_altitude and next_altitude < target_altitude):
                return times[i + 1]

    return None

# Sunrise ans Sunset
sunrise = find_crossing(-0.833, "rising")
sunset = find_crossing(-0.833, "setting")

# Twilight Events
civil_morning = find_crossing(-6, "rising")
civil_evening = find_crossing(-6, "setting")

nautical_morning = find_crossing(-12, "rising")
nautical_evening = find_crossing(-12, "setting")

astronomical_morning = find_crossing(-18, "rising")
astronomical_evening = find_crossing(-18, "setting")

# Golden Hour
golden_hour_duration = timedelta(minutes = 28)

if sunrise is not None:
    morning_golden_start = sunrise
    morning_golden_end = (sunrise + golden_hour_duration)
else:
    morning_golden_start = None
    morning_golden_end = None

if sunset is not None:
    evening_golden_start = (sunset - golden_hour_duration)
    evening_golden_end = sunset
else:
    evening_golden_start = None
    evening_golden_end = None

# Format Time
def format_time(dt):
    if dt is None:
        return "N/A"
    return dt.strftime("%H:%M")

def format_range(start, end):
    if start is None or end is None:
        return "N/A"
    return (f"{format_time(start)} - "f"{format_time(end)}")

# Terminal Output
print("🌌 BEST STARGAZING TIME")
print("═" * 50)

print(f"📅 Date: "f"{date_obj.strftime('%d %B %Y')}")
print(f"📍 Location: {LOCATION_NAME}")
print(f"🌐 Coordinates: "f"{LATITUDE:.4f}°, "f"{LONGITUDE:.4f}°")

print()

print("☀️ Sunrise")
print(f"{format_time(sunrise)}")
print()

print("🌅 Morning Golden Hour")
print(f"{format_range(evening_golden_start, evening_golden_end)}")
print()

print("🌇 Sunset")
print(f"{format_time(sunset)}")
print()

print("🌅 Evening Golden Hour")
print(f"{format_range(evening_golden_start, evening_golden_end)}")
print()

print("🌆 Civil Twilight")
print(f"{format_range(sunset, civil_evening)}")
print()

print("🌃 Nautical Twilight")
print(f"{format_range(civil_evening, nautical_evening)}")
print()

print("🌌 Astronomical Twilight")
print(f"{format_range(nautical_evening, astronomical_evening)}")
print()

print("🌠 Astronomical Night")
print(f"{format_range(astronomical_evening, astronomical_morning)}")
print()

print("⭐ BEST DARK-SKY PERIOD")
print(f"{format_range(astronomical_evening, astronomical_morning)}")

print("═" * 50)

# Visualization

fig, ax = plt.subplots(figsize = (15, 7))

ax.plot(times, altitudes, linewidth = 2, label = "Sun altitude")

ax.axhline(0, linestyle = "--", linewidth = 1, label = "Horizon (0°)")
ax.axhline(-6, linestyle = "--", linewidth = 1, label = "Civil Twilight (-6°)")
ax.axhline(-12, linestyle = "--", linewidth = 1, label = "Nautical Twilight (-12°)")
ax.axhline(-18, linestyle = "--", linewidth = 1, label = "Astronomical Twilight (-18°)")

if (astronomical_evening is not None and astronomical_morning is not None):
    ax.axvspan(astronomical_evening, astronomical_morning, alpha = 0.20, label = "Best dark-sky period")

if sunrise is not None:
    ax.axvline(sunrise, linestyle = ":", linewidth = 2)
    ax.annotate(f"Sunrise\n{format_time(sunrise)}", xy = (sunrise, 0), xytext = (10, 20),
        textcoords = "offset points", rotation = 90, verticalalignment = "bottom")

if sunset is not None:
    ax.axvline(sunset, linestyle = ":", linewidth = 2)
    ax.annotate(f"Sunset\n{format_time(sunset)}", xy = (sunset, 0), xytext = (10, 20),
        textcoords = "offset points", rotation = 90, verticalalignment = "bottom")

ax.set_title(f"Best Stargazing Time\n" f"{date_obj.strftime('%d %B %Y')} — "
    f"{LOCATION_NAME}", fontsize = 16)
ax.set_xlabel("Local Time")
ax.set_ylabel("Sun Altitude (°)")

ax.set_ylim(-25, 90)

ax.xaxis.set_major_formatter(
    mdates.DateFormatter("%H:%M", tz = tz))

ax.xaxis.set_major_locator(
    mdates.HourLocator(interval = 2, tz = tz))

ax.grid(True, alpha = 0.3)
ax.legend(loc = "upper right")
plt.tight_layout()
plt.show()