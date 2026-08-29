# Mini Project 05: Mars Motion and Observability Analysis

A Python-based astronomy visualisation project that uses **Skyfield, NumPy and Matplotlib** to analyse the motion of Mars and its position in the night sky.

The project combines astronomical position calculations, coordinate systems, time handling and scientific visualisation to explore both the **heliocentric motion of Mars** and its **apparent position from an observer on Earth**.

---

## Project Overview

Mars is constantly moving around the Sun, while Earth is also moving along its own orbit.

This project visualises that motion and connects planetary coordinates with observational astronomy.

The program calculates and visualises:

* Mars' heliocentric position
* Mars' Cartesian coordinates
* Mars' distance from the Sun
* Earth-Mars distance
* Right Ascension (RA)
* Declination (Dec)
* Local Sidereal Time (LST)
* Hour Angle
* Altitude
* Azimuth
* Mars' position throughout an observation period

The final output combines these calculations into a scientific visualisation dashboard.

---

## Objectives

The main objectives of this project are:

1. Understand how planetary positions change with time.
2. Retrieve astronomical positions using Skyfield.
3. Work with Cartesian and spherical coordinate concepts.
4. Calculate planetary distances.
5. Understand the relationship between RA, LST and Hour Angle.
6. Convert astronomical information into observer-based Altitude and Azimuth.
7. Visualise planetary motion using 2D, 3D and polar plots.
8. Apply Python numerical computing and scientific visualisation skills to an astronomy problem.

---

## Astronomy Concepts

### 1. Cartesian Coordinates

Mars' position can be represented using three coordinates:

(x,y,z)

These coordinates allow the planetary position to be visualised in three-dimensional space.

---

### 2. Spherical Coordinates

The relationship between Cartesian and spherical coordinates is:

r=\sqrt{x^2+y^2+z^2}

where `r` represents the distance from the origin.

The angular coordinates describe the direction of the object.

---

### 3. Right Ascension and Declination

From Earth's perspective, Mars can be represented using the equatorial coordinate system:

* Right Ascension (RA)
* Declination (Dec)

RA is measured in hours, while Dec is measured in degrees.

These coordinates describe where Mars is located on the celestial sphere.

---

### 4. Local Sidereal Time

Local Sidereal Time describes the rotation of the celestial sphere relative to the observer's longitude.

It is used together with Right Ascension to calculate Hour Angle.

---

### 5. Hour Angle

The basic relationship is:

H = LST - RA

where:

* `H` = Hour Angle
* `LST` = Local Sidereal Time
* `RA` = Right Ascension

This connects the celestial coordinate system to the observer's local sky.

---

### 6. Altitude and Azimuth

The horizontal coordinate system describes an object's position from an observer.

**Altitude** describes how high the object is above the horizon.

**Azimuth** describes the direction along the horizon.

For example:
Altitude = 45°
Azimuth = 120°

means Mars is 45° above the horizon in the direction corresponding to an azimuth of 120°.

---

## Technologies Used

* Python
* NumPy
* Matplotlib
* Skyfield

---

## Visualisations

The project generates a six-panel scientific visualisation containing:

### 1. Mars Heliocentric Orbit

A 2D representation of Mars' motion around the Sun.

### 2. 3D Mars Motion

A three-dimensional representation using Mars' X, Y and Z coordinates.

### 3. Mars-Sun Distance

Shows how Mars' distance from the Sun changes over time.

### 4. Earth-Mars Distance

Shows how the distance between Earth and Mars changes over time.

### 5. Mars Altitude

Shows how Mars' altitude changes during the selected observation period.

### 6. Local Sky Position

A polar representation of Mars' position using:

* Azimuth → angular position
* Altitude → distance from the horizon

---

## Output

The program generates the following visualisation:

`screenshots/mars_motion_output.png`

The dashboard provides a compact view of Mars' orbital motion, planetary distances and its position in the observer's sky.

---

## Project Structure

Mini_Project_04_Mars_Motion/
│
├── mars_motion.py
├── README.md
├── requirements.txt
│
└── screenshots/
    └── mars_motion_output.png

---

## Installation

Clone the repository:

git clone <your-repository-url>

Navigate to the project directory:

cd Mini_Project_04_Mars_Motion

Install the required libraries:

pip install -r requirements.txt

---

## Running the Project

Run:

python mars_motion.py

The program will:

1. Load the astronomical ephemeris.
2. Generate time samples.
3. Calculate Mars' position.
4. Calculate planetary distances.
5. Calculate RA and Dec.
6. Calculate Local Sidereal Time and Hour Angle.
7. Calculate Altitude and Azimuth.
8. Print a numerical summary.
9. Generate the visualisation.
10. Save the final figure inside the `images` directory.

---

## Data Source

The planetary positions are obtained using **Skyfield** and an astronomical ephemeris.

Skyfield performs the astronomical position calculations while NumPy and Matplotlib are used for numerical processing and visualisation.

---

## Connection to the AI Stargazing Assistant

This project is also a stepping stone toward my larger **AI-Powered Stargazing Assistant** project.

The concepts developed here form the foundation for:

Astronomical Position
        ↓
Coordinate Transformation
        ↓
Observer Position
        ↓
Altitude / Azimuth
        ↓
Visibility Analysis
        ↓
Weather Conditions
        ↓
ML Recommendation
        ↓
AI Stargazing Assistant

The eventual goal is to combine astronomical calculations, weather information and machine learning to recommend the best celestial objects and observing conditions for a user.

---

## Learning Outcomes

Through this project, I practised:

* Python functions
* Python datetime handling
* NumPy arrays
* Vector calculations
* Cartesian coordinates
* Spherical coordinate concepts
* RA and Dec
* Local Sidereal Time
* Hour Angle
* Altitude and Azimuth
* Skyfield astronomical calculations
* 2D plotting
* 3D plotting
* Polar plotting
* Scientific data visualisation
* Structuring a Python project for GitHub

---


This project was developed as part of my journey toward building an **AI-Powered Stargazing Assistant**.
