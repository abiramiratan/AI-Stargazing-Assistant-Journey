# Astronomy Cheat Sheet — Visibility Engine

## 1. Coordinate Systems

**Explanation:** Different ways to describe an object's position in the sky.

**Common Systems:**

* Equatorial -> (Right Ascension[RA], Declination[Dec])
* Horizontal -> (Altitude[Alt], Azimuth[Az])

**Why it matters:** Visibility calculations convert Equatorial coordinates into Horizontal coordinates.

---

## 2. Right Ascension (RA) and Declination (Dec)

**Explanation:** The celestial equivalent of longitude and latitude.

**Formula:**

* RA -> measured in hours (0h–24h)
* Dec -> measured in degrees (-90° to +90°)

**Why it matters:** Most star catalogs provide object positions in RA and Dec.

---

## 3. Spherical -> Cartesian Conversion

**Explanation:** Converts celestial coordinates into 3D vectors.

**Formula:**

x = cos(Dec) * cos(RA)

y = cos(Dec) * sin(RA)

z = sin(Dec)

**Why it matters:** Useful for vector operations, rotations, and visibility calculations.

---

## 4. Local Sidereal Time (LST)

**Explanation:** Right Ascension currently crossing the local meridian.

**Formula:**

LST = GST(Greenwich Sidereal Time) + Longitude

**Why it matters:** Required to determine where an object appears in the local sky.

---

## 5. Hour Angle (HA)

**Explanation:** Angular distance between the object and the local meridian.

**Formula:**

HA = LST − RA

**Why it matters:** Indicates whether an object is rising, setting, or overhead.

---

## 6. Altitude Formula

**Explanation:** Calculates how high an object appears above the horizon.

**Formula:**

sin(Alt) = sin(Lat) * sin(Dec) + cos(Lat) * cos(Dec) * cos(HA)

Alt = arcsin(Alt)

**Why it matters:** If Alt > 0°, the object is above the horizon and potentially visible.

---

## Visibility Rule

**Altitude > 0°** → Object is above horizon

**Altitude < 0°** → Object is below horizon

**Altitude = 90°** → Object is near zenith

**Altitude = 0°** → Object is on horizon

---

## Visibility Engine Pipeline

1. Get RA and Dec
2. Compute LST
3. Compute Hour Angle
4. Calculate Altitude
5. Check Altitude > 0°
6. Recommend observable objects
