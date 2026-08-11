import numpy as np

R = 6371

def observer_vector(lat_deg, lon_deg):
    lat = np.radians(lat_deg)
    lon = np.radians(lon_deg)

    x = R * np.cos(lat) * np.cos(lon)
    y = R * np.cos(lat) * np.sin(lon)
    z = R * np.sin(lat)

    return x, y, z

def haversine(lat1, lon1, lat2, lon2):
    lat1 = np.radians(lat1)
    lon1 = np.radians(lon1)

    lat2 = np.radians(lat2)
    lon2 = np.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2)

    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))

    return c, R *c

print("===== Observatory Distance Calculator =====")

print("\nObservatory A")
lat1 = float(input("Latitude: "))
lon1 = float(input("Longitude: "))

print("\nObservatory B")
lat2 = float(input("Latitude: "))
lon2 = float(input("Longitude: "))

theta, dis = haversine(lat1, lon1, lat2, lon2)

vec1 = observer_vector(lat1, lon1)
vec2 = observer_vector(lat2, lon2)

print("\n===== Result =====")

print(f"Central Angle: {np.degrees(theta):.2f}°")
print(f"Distance: {dis:.2f}km")

print("\nObserver Vector A") 
print(f"x = {vec1[0]:.2f}")
print(f"y = {vec1[1]:.2f}")
print(f"z = {vec1[2]:.2f}")

print("\nObserver Vector B")
print(f"x = {vec2[0]:.2f}")
print(f"y = {vec2[1]:.2f}")
print(f"z = {vec2[2]:.2f}")