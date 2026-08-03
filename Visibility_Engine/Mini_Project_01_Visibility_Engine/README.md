# Mini Project 01 — Visibility Engine

## 1. Problem Statement

Astronomical catalogs provide the positions of celestial objects using Right Ascension (RA) and Declination (Dec). However, these coordinates alone do not tell an observer whether an object is currently visible from a specific location on Earth.

The goal of this project is to build a simple Visibility Engine that determines whether a celestial object is above the observer's horizon using basic astronomical calculations.

---

## 2. Astronomy Concepts Used

* Right Ascension (RA) -> The celestial equivalent of longitude.
* Declination (Dec) -> The celestial equivalent of latitude.
* Local Sidereal Time (LST) -> Represents the Right Ascension currently crossing the observer's local meridian.
* Hour Angle (HA) -> Measures how far an object is from the local meridian.
* Altitude -> The angle between the object and the observer's horizon.

### Visibility Rule:
Altitude > 0°  → Visible
Altitude < 0°  → Not Visible

---

## 3. Mathematical Formulas

### Hour Angle

HA = LST − RA
Convert hours to degrees: HA(degrees) = HA(hours) × 15 

---

### Altitude Formula

sin(Alt) = sin(Lat) * sin(Dec) + cos(Lat) * cos(Dec) * cos(HA)
Alt = arcsin(result)

Where:
Lat = Observer Latitude
Dec = Declination
HA  = Hour Angle
Alt = Altitude

---

## 4. Algorithm

Input:
    Latitude
    Right Ascension (RA)
    Declination (Dec)
    Local Sidereal Time (LST)

Step 1:
    Compute Hour Angle
    HA = LST − RA

Step 2:
    Convert HA to degrees

Step 3:
    Calculate Altitude using spherical astronomy formula

Step 4:
    If Altitude > 0°
        Object is Visible
    Else
        Object is Not Visible

Output: Hour Angle, Altitude, Visibility Status.

---

## 5. Code Structure

Mini_Project_01_Visibility_Engine/
├── visibility_engine.py
├── examples.py
└── README.md

### visibility_engine.py

Contains:
calculate_hour_angle()
calculate_altitude()
is_visible()
main()

Responsibilities:

* Perform visibility calculations
* Determine visibility status
* Run interactive user input mode

## Example Output

The Visibility Engine was tested using five sample celestial objects.

Visible Objects:
- Object A
- Object B
- Object C

Not Visible:
- Object D
- Object E

---

## 6. Future Improvements

Version 2: Read celestial objects from a CSV catalog. stars.csv -> Visibility Engine -> Visible Objects List.
Version 3: Calculate Azimuth in addition to Altitude. Output: Altitude, Azimuth, Visibility.
Version 4: Integrate real Local Sidereal Time calculations from date, time, and longitude.
Version 5: Visualize visible objects on a sky map.
Version 6: Integrate weather data to remove objects hidden by clouds.
Version 7: Build the recommendation engine for the AI Stargazing Assistant.

Astronomy + Weather + Machine Learning = Best Objects to Observe Tonight