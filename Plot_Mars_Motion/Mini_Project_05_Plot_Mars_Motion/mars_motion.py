import numpy as np
import matplotlib.pyplot as plt

# timedelta - difference in time
# Topos - an observer's location on Earth
from datetime import datetime, timedelta, timezone
from skyfield.api import load, Topos

#configuration variable
YEAR = 2025

OBSERVER_LATITUDE = 13.0827
OBSERVER_LONGITUDE = 80.2707
OBSERVER_NAME = "Chennai, India"

OBSERVER_DATE = datetime(2025, 1, 1, tzinfo = timezone.utc)

ORBIT_DAYS = 365
ORBIT_STEP = 5

NIGHT_HOURS = 12
NIGHT_STEP_MINUTES = 10

ts = load.timescale()
planets = load("de421.bsp")

sun = planets['sun']
earth = planets['earth']
mars = planets['mars']

observer = earth + Topos(latitude_degrees= OBSERVER_LATITUDE,
                         longitude_degrees= OBSERVER_LONGITUDE)

def create_orbit_times():
    dates = [datetime(YEAR, 1, 1, tzinfo= timezone.utc) 
            + timedelta(days = day)
            for day in range(0, ORBIT_DAYS, ORBIT_STEP)]

    return ts.from_datetimes(dates)

def create_night_times():
    dates = [OBSERVER_DATE + 
             timedelta(minutes = minute)
             for minute in range(0, NIGHT_HOURS * 60, 
                                 NIGHT_STEP_MINUTES)]

    return ts.from_datetimes(dates)

orbit_times = create_orbit_times()
night_times = create_night_times()

def calculate_mars_orbit(times):
    astrometric = sun.at(times).observe(mars)
    position_au = astrometric.position.au

    x = position_au[0]
    y = position_au[1]
    z = position_au[2]

    return x, y, z

x, y, z = calculate_mars_orbit(orbit_times)

def cartesian_to_spherical(x, y, z):
    #radius = distance from origin
    #theta = azimuthal angle
    #phi = elevation angle

    radius = np.sqrt(x**2 + y**2 + z**2)
    theta = np.arctan2(y, x)
    phi = np.arctan2(z, np.sqrt(x**2 + y**2))

    return radius, theta, phi

mars_distance, theta, phi = cartesian_to_spherical(x, y, z)

def calculate_earth_mars_distance(times):
    earth_position = earth.at(times)
    mars_position = mars.at(times)

    difference = (mars_position.position.au 
                 - earth_position.position.au)

    distance = np.linalg.norm(difference, axis = 0)

    return distance

earth_mars_distance = calculate_earth_mars_distance(orbit_times)

def calculate_ra_dec(times):
    astrometric = earth.at(times).observe(mars)

    ra, dec, dis = astrometric.radec()

    return(ra.hours, dec.degrees, dis.au)

ra_hours, dec_degrees, geocentric_dis = calculate_ra_dec(
    orbit_times)

def calculate_sidereal_and_HR(time):
    astrometric = observer.at(time).observe(mars)

    ra, dec, dis = astrometric.radec()

    #LST to GMST + converting longitude degrees to hours
    lst = time.gmst + (OBSERVER_LONGITUDE / 15)

    # scope within 24 hr(excluding > 24 and < 0)
    lst = lst % 24

    hr_angle = (lst - ra.hours) % 24

    return (lst, ra.hours, dec.degrees, hr_angle)

lst, observation_ra, observation_dec, hr_angle = (
    calculate_sidereal_and_HR(night_times[0])
)

def calculate_alt_az(times):
    astrometric = observer.at(times).observe(mars)
    apparent = astrometric.apparent()
    alt, az, dis = apparent.altaz()

    return (alt.degrees, az.degrees, dis.au)

alt, az, sky_dis = calculate_alt_az(night_times)

best_index = np.argmax(alt)
best_alt = alt[best_index]
best_az = az[best_index]

# best observer time
best_time = night_times.utc_datetime()[best_index]

print("\n" + "=" * 40)
print("MARS MOTION ANALYSIS")
print("=" * 40)

print(f"\nObserver: {OBSERVER_NAME}")
print(f"Latitude: {OBSERVER_LATITUDE:.4f}°")
print(f"Longitude: {OBSERVER_LONGITUDE:.4f}°")

print(f"\nMinimum Mars-Sun distance: "
      f"{mars_distance.min():.3f} AU")
print(f"\nMaximum Mars-Sun distance: "
      f"{mars_distance.max():.3f} AU")
print(f"\nAverage Mars-Sun distance: "
      f"{mars_distance.mean():.3f} AU")

print(f"\nMinimum Earth-Mars distance: "
      f"{earth_mars_distance.min():.3f} AU")
print(f"\nMaximum Earth-Mars distance: "
      f"{earth_mars_distance.max():.3f} AU")

print(f"\nObsevation date: "
      f"{OBSERVER_DATE.strftime('%Y-%m-%d')}")
print(f"Best sample altitude: "
      f"{best_alt:.2f}°")
print(f"Best sample azimuth: "
      f"{best_az:.2f}°")

print(f"Best sample time: "
      f"{best_time.strftime('%Y-%m-%d %H:%M UTC')}")
print(f"\nLocal Sidereat Time: "
      f"{lst:.2f} hours")

print(f"Mars Right Ascension: "
      f"{observation_ra:.2f} hours")
print(f"Mars Declination: "
      f"{observation_dec:.2f}°")
print(f"Mars Hour Angle: "
      f"{hr_angle:.2f} hours")

print("=" * 40)

fig = plt.figure(figsize = (16, 12))
fig.suptitle("Mars Motion and Observability Analysis",
             fontsize = 18, fontweight = "bold")

ax1 = fig.add_subplot(231)
ax1.plot(x, y, linewidth = 2, label = "Mars trajectory")
ax1.scatter(0, 0, s = 250, label = "Sun", zorder = 5)
ax1.scatter(x[0], y[0], s = 70, label = "Start", zorder = 5)
ax1.scatter(x[-1], y[-1], s = 70, label = "End", zorder = 5)

ax1.set_title("Mars Heliocenter Orbit")
ax1.set_xlabel("X position(AU)")
ax1.set_ylabel("Y position(AU)")
ax1.axis("equal")
ax1.grid(alpha = 0.3)
ax1.legend(fontsize = 8)

ax2 = fig.add_subplot(232, projection = "3d")
ax2.plot(x, y, z, linewidth = 2)
ax2.scatter(0, 0, 0, s = 200, label = "Sun")
ax2.scatter(x[0], y[0], z[0], s = 60, label = "Mars start")
ax2.set_title("3D Mars Motion")
ax2.set_xlabel("X (AU)")
ax2.set_ylabel("Y (AU)")
ax2.set_zlabel("Z (AU)")
ax2.legend(fontsize = 8)

ax3 = fig.add_subplot(233)
days = np.arange(len(mars_distance)) * ORBIT_STEP
ax3.plot(days, mars_distance, linewidth = 2)
ax3.set_title("Mars-Sun Distance")
ax3.set_xlabel("Days since Jan 1")
ax3.set_ylabel("Distance (AU)")
ax3.grid(alpha = 0.3)

ax4 = fig.add_subplot(234)
ax4.plot(days, earth_mars_distance, linewidth = 2)
ax4.set_title("Earth-Mars Distance")
ax4.set_xlabel("Days since Jan 1")
ax4.set_ylabel("Distance (AU)")
ax4.grid(alpha = 0.3)

ax5 = fig.add_subplot(235)
night_datetimes = night_times.utc_datetime()
hours = np.array([(dt - night_datetimes[0]).total_seconds() / 3600
                  for dt in night_datetimes])
ax5.plot(hours, alt, linewidth = 2, label = "Altitude")
ax5.axhline(0, linestyle = "--", label = "Horizon")
ax5.scatter(hours[best_index], best_alt, s = 70,
            zorder = 5, label = "Highest altitude")
ax5.set_title("Mars Altitude During Observation")
ax5.set_xlabel("Hours from observation start")
ax5.set_ylabel("Altitude (degrees)")
ax5.grid(alpha = 0.3)
ax5.legend(fontsize = 8)

ax6 = fig.add_subplot(236, projection = "polar")
az_rad = np.radians(az)
sky_radius = 90 - alt
ax6.plot(az_rad, sky_radius, linewidth = 2)
ax6.scatter(np.radians(best_az), 90 - best_alt, s = 70,
            zorder = 5, label = "Best position")
ax6.set_theta_zero_location("N")
ax6.set_theta_direction(-1)
ax6.set_ylim(90, 0)
ax6.set_rlabel_position(225)
ax6.legend(fontsize = 8, loc = "lower left")

plt.tight_layout(rect = [0, 0, 1, 0.96])
plt.show()