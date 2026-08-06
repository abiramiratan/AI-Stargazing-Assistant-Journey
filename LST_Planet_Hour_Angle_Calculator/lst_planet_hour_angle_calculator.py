from skyfield.api import load, wgs84

ts = load.timescale()
t = ts.now()

lnd = float(input("Enter Longitude: "))
lat = float(input("Enter Latitude: "))

gmst = t.gmst
lst = gmst + lnd / 15  # 360 / 24 = 15

while lst >= 24:
    lst -=24

while lst < 0:
    lst += 24

planets = load('de421.bsp')
earth = planets['earth']


planet_choices = {
    1 : 'mercury barycenter', 
    2 : 'venus',
    3 : 'mars',
    4 : 'jupiter barycenter',
    5 : 'saturn barycenter',
}

print("\nChoose planet")
print("1. Mercury")
print("2. Venus")
print("3. Mars")
print("4. Jupiter")
print("5. Saturn")

choice = int(input("Choice: "))

if choice not in planet_choices:
    print("Invalid choice")
    exit()

planet_name = planet_choices[choice]
planet = planets[planet_name]

location = earth + wgs84.latlon(lat, lnd)

astrometric = location.at(t).observe(planet)
apparent = astrometric.apparent()

ra, dec, dis = apparent.radec(epoch='date')
planet_ra = ra.hours
planet_dec = dec.degrees

alt, az, dis = apparent.altaz()
planet_alt = alt.degrees
planet_az = az.degrees

ha = lst - planet_ra

while ha < 0:
    ha += 24

while ha >= 24:
    ha -= 24

if planet_alt < 0:
    status = "Below Hoizon (Not visible)"
elif abs(ha) < 0.25:
    status = "Crossing Meridian"
elif ha < 12:
    status = "West of Meridian (Setting)"
else:
    status = "East of Meridian (Rising)"

print("\n===== RESULT =====")
print(f"GMST: {gmst:.2f} h")
print(f"LST: {lst:.2f} h")
print(f"RA: {planet_ra:.2f} h")
print(f"Dec: {planet_dec:.2f} °")
print(f"Altitude: {planet_alt:.2f} °")
print(f"Azimuth: {planet_az:.2f} °")
print(f"Hour Angle: {ha:.2f} h")
print(f"Status: {status}")