# Astronomy Formulas Used - LST & Planet Hour Angle Calculator

## 1. Longitude Conversion

Since Earth rotates:

360° = 24 hours

Therefore:

1 hour = 15°

Longitude in hours:

Longitude(hours) = Longitude(degrees) / 15

---

## 2. Local Sidereal Time (LST)

Local Sidereal Time is obtained by adjusting Greenwich Mean Sidereal Time for the observer's longitude.

LST = GMST + Longitude(hours)

or

LST = GMST + Longitude(degrees) / 15

---

## 3. Hour Angle (HA)

Hour Angle is the angular distance between the observer's local meridian and the celestial object's meridian.

HA = LST − RA

---

## 4. Hour Angle Normalization

To keep the Hour Angle within the standard 24-hour range:

If HA < 0
HA = HA + 24

If HA ≥ 24
HA = HA − 24

Result:

0 ≤ HA < 24

---

## 5. Meridian Crossing Condition

An object is considered to be crossing the meridian when:

HA ≈ 0

In this project:

|HA| < 0.25 hours

---

## 6. Object Position Relative to Meridian

HA = 0
Object on the meridian.

0 < HA < 12
Object west of the meridian (setting).

12 < HA < 24
Object east of the meridian (rising).
