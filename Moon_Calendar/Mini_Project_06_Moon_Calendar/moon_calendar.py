import calendar
from datetime import timedelta

import matplotlib.pyplot as plt
import numpy as np

from skyfield.api import load, wgs84
from skyfield import almanac

import requests
from PIL import Image
from io import BytesIO
from matplotlib.offsetbox import ( OffsetImage, AnnotationBbox)


print("=" * 40)
print("          🌙 MOON CALENDAR")
print("=" * 40)

YEAR = int(input("Enter year: "))

MONTH = int(input("Enter month (1 - 12): "))

print("\nEnter observer location")

LATITUDE = float(input("Enter latitude: "))

LONGITUDE = float(input("Enter longitude: "))

TIMEZONE_OFFSET = float(input("Enter timezone offset from UTC (e.g., 5.5 for IST): "))

if MONTH < 1 or MONTH > 12:
    raise ValueError("Month must be between 1 and 12.")

if YEAR < 1:
    raise ValueError("Enter a valid year.")

if LATITUDE < -90 or LATITUDE > 90:
    raise ValueError("Latitude must be between -90 and 90.")

if LONGITUDE < -180 or LONGITUDE > 180:
    raise ValueError("Longitude must be between -180 and 180.")

ts = load.timescale()

planets = load("de421.bsp")

earth = planets["earth"]
moon = planets["moon"]
sun = planets["sun"]

observer = earth + wgs84.latlon(LATITUDE,LONGITUDE)


def emoji_to_image(symbol):

    emoji_codes = {"🌑": "1f311", "🌒": "1f312",
        "🌓": "1f313", "🌔": "1f314", "🌕": "1f315",
        "🌖": "1f316", "🌗": "1f317", "🌘": "1f318"}

    code = emoji_codes[symbol]

    url = (
        "https://cdn.jsdelivr.net/gh/"
        "jdecked/twemoji@latest/assets/"
        "72x72/"
        f"{code}.png"
    )

    response = requests.get(url, timeout = 10)

    response.raise_for_status()

    image = Image.open(BytesIO(response.content)).convert("RGBA")

    return np.array(image)


def get_moon_phase(t):

    moon_position = (earth.at(t).observe(moon).apparent())

    sun_position = (earth.at(t).observe(sun).apparent())

    # Angular separation between Moon and Sun
    separation = (moon_position.separation_from(sun_position).degrees)

    # Ecliptic longitudes
    moon_lon, _, _ = (moon_position.ecliptic_latlon())

    sun_lon, _, _ = (sun_position.ecliptic_latlon())

    # Difference between Moon and Sun longitude
    elongation = (moon_lon.degrees - sun_lon.degrees) % 360

    if separation < 10:
        return "New Moon", "🌑"
    elif separation > 170:
        return "Full Moon", "🌕"
    elif (separation < 80 and elongation < 180):
        return "Waxing Crescent", "🌒"
    elif (80 <= separation <= 100 and elongation < 180):
        return "First Quarter", "🌓"
    elif (separation > 100 and elongation < 180):
        return "Waxing Gibbous", "🌔"
    elif (separation > 100 and elongation >= 180):
        return "Waning Gibbous", "🌖"
    elif (80 <= separation <= 100 and elongation >= 180):
        return "Last Quarter", "🌗"
    else:
        return "Waning Crescent", "🌘"


def get_illumination(t):

    moon_position = (earth.at(t).observe(moon).apparent())
    sun_position = (earth.at(t).observe(sun).apparent())

    angle = (moon_position.separation_from(sun_position).degrees)

    illumination = (1 + np.cos(np.radians(angle))) / 2

    return illumination * 100


def get_alt_az(t):

    astrometric = (observer.at(t).observe(moon))
    apparent = (astrometric.apparent())

    altitude, azimuth, _ = (apparent.altaz())

    return (altitude.degrees, azimuth.degrees)


def get_rise_set(year, month, day):

    start = ts.utc(year, month, day, 0, 0, 0)
    end = ts.utc(year, month, day + 1, 0, 0, 0)

    # Observer location on Earth
    topos = wgs84.latlon(LATITUDE, LONGITUDE)

    # Create rise/set event function
    f = almanac.risings_and_settings(planets, moon, topos)

    # Find rise/set events
    times, events = almanac.find_discrete(start, end, f)

    moonrise = None
    moonset = None

    for t, event in zip(times, events):

        if event == 1:
            moonrise = t.utc_datetime()

        elif event == 0:
            moonset = t.utc_datetime()

    return moonrise, moonset


def utc_to_local(dt):

    if dt is None:
        return "--"

    local_time = (dt + timedelta(hours = TIMEZONE_OFFSET))

    return local_time.strftime("%H:%M")


def get_major_phase_events(year, month):

    days_in_month = (calendar.monthrange(year, month)[1])

    start = ts.utc(year, month, 1)
    end = ts.utc(year, month, days_in_month, 23, 59, 59)

    # Find actual astronomical phase events
    phase_times, phase_values = (almanac.find_discrete(start,
            end,almanac.moon_phases(planets)))

    phase_names = {

        0: ("🌑", "New Moon"),

        1: ("🌓", "First Quarter"),

        2: ("🌕", "Full Moon"),

        3: ("🌗", "Last Quarter")
    }

    events = {}

    for t, phase_value in zip(phase_times, phase_values):

        if phase_value in phase_names:

            local_datetime = (t.utc_datetime() + timedelta(
                    hours=TIMEZONE_OFFSET))

            day = local_datetime.day

            symbol, phase_name = (phase_names[phase_value])

            events[day] = {
                "symbol": symbol, "name": phase_name,
                "time": local_datetime.strftime("%H:%M")}

    return events


def create_month_data(year, month):

    days_in_month = (calendar.monthrange(year, month)[1])

    data = []

    for day in range(1, days_in_month + 1):

        # Use 12:00 UTC as the daily reference
        t = ts.utc(year, month, day, 12, 0, 0)

        phase, symbol = (get_moon_phase(t))

        illumination = (get_illumination(t))

        altitude, azimuth = (get_alt_az(t))

        moonrise, moonset = (get_rise_set(year, month, day))

        data.append({"day": day, "phase": phase, "symbol": symbol,
            "illumination": illumination, "altitude": altitude,
            "azimuth": azimuth, "moonrise": utc_to_local(moonrise),
            "moonset": utc_to_local(moonset)})

    return data

def plot_moon_calendar(data, year, month, major_events):

    month_name = (calendar.month_name[month])

    month_calendar = (calendar.monthcalendar(year, month))

    fig, ax = plt.subplots(figsize=(16, 10))

    ax.set_xlim(0, 7)

    ax.set_ylim(len(month_calendar) + 1, 0)

    ax.axis("off")

    ax.text(3.5, -0.45, f"Moon Calendar — "
        f"{month_name} {year}", ha = "center", fontsize = 22,
        fontweight = "bold")


    ax.text(3.5, -0.10, f"Location: "
        f"{LATITUDE:.4f}°, " f"{LONGITUDE:.4f}°",
        ha = "center", fontsize = 10)

    weekdays = ["Monday", "Tuesday", "Wednesday", 
        "Thursday", "Friday", "Saturday", "Sunday"]

    for col, weekday in enumerate(weekdays):

        ax.text(col + 0.5, 0.45, weekday, ha = "center",
            fontsize = 10, fontweight = "bold")

    for row, week in enumerate(month_calendar, start=1):

        for col, day in enumerate(week):

            rectangle = plt.Rectangle((col, row), 1,
                1, fill = False, linewidth = 0.8)


            ax.add_patch(rectangle)

            if day == 0:
                continue

            item = data[day - 1]

            ax.text(col + 0.08, row + 0.16, str(day),
                fontsize = 10, fontweight = "bold", va = "top")

            moon_image = emoji_to_image(item["symbol"])


            moon_image_box = OffsetImage(moon_image, zoom = 0.35)

            moon_image_artist = AnnotationBbox(
                moon_image_box,(col + 0.5, row + 0.30),
                frameon = False,
                box_alignment=(0.5, 0.5))


            ax.add_artist(moon_image_artist)

            ax.text(col + 0.5, row + 0.63,
                f"{item['illumination']:.0f}%", ha = "center",
                fontsize = 9)

            ax.text(col + 0.5, row + 0.77, f"↑ {item['moonrise']}",
                ha = "center", fontsize = 7)

            ax.text(col + 0.5, row + 0.88,
                f"↓ {item['moonset']}", ha = "center",
                fontsize = 7)

            if day in major_events:

                phase_info = (major_events[day])


                ax.text(col + 0.5, row + 0.97, f"{phase_info['name']} "
                    f"{phase_info['time']}", ha = "center", va = "bottom",
                    fontsize = 5.8, fontweight = "bold")

    plt.subplots_adjust(left = 0.02, right = 0.98, top = 0.90, bottom = 0.03)


    plt.show()


def plot_illumination(data, year, month):

    days = [item["day"] for item in data]

    illumination = [item["illumination"] for item in data]

    plt.figure(figsize = (12, 6))

    plt.plot(days, illumination, marker="o")

    plt.title(f"🌙 Moon Illumination — "
        f"{calendar.month_name[month]} " f"{year}",
        fontsize=16, fontweight="bold")

    plt.xlabel("Day of Month")

    plt.ylabel("Illumination (%)")

    plt.ylim(0, 100)

    plt.xticks(days)

    plt.grid(True, alpha=0.3)

    plt.tight_layout()

    plt.show()


def print_summary(data):

    print("\n")

    print("=" * 90)

    print(f"🌙 " f"{calendar.month_name[MONTH]} "
        f"{YEAR} — MOON INFORMATION")

    print("=" * 90)

    for item in data:
        print(f"\nDay {item['day']:02d} "
            f"{item['symbol']} " f"{item['phase']}")

        print(f"  Illumination : "
            f"{item['illumination']:.1f}%")

        print(f"  Altitude     : "
            f"{item['altitude']:.1f}°")

        print(f"  Azimuth      : "
            f"{item['azimuth']:.1f}°")

        print(f"  Moonrise     : "
            f"{item['moonrise']}")

        print(f"  Moonset      : "
            f"{item['moonset']}")


def main():

    print(f"\nCalculating Moon Calendar for "
        f"{calendar.month_name[MONTH]} " f"{YEAR}...")

    # Create daily Moon data
    data = create_month_data(YEAR, MONTH)

    # Find major Moon phases
    major_events = (get_major_phase_events(YEAR, MONTH))

    # Print information
    print_summary(data)

    # Display Moon calendar
    plot_moon_calendar(data, YEAR, MONTH, major_events)

    # Display illumination graph
    plot_illumination(data, YEAR, MONTH)

    print("\n🌙 Moon Calendar "
          "completed successfully!")


if __name__ == "__main__":

    main()