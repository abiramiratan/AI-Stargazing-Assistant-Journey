# Mini Project 04: Moon Position Calculator

A Python-based astronomical computation project that determines the **apparent position of the Moon** for a given observer location and observation time using the **Skyfield** library.

This project is part of the **AI-Powered Stargazing Assistant** learning journey and focuses on building the astronomical position-calculation component of the system.

---

## Overview

The position of the Moon in the sky changes continuously with time and observer location.

This project uses astronomical ephemeris data and an observer's geographic coordinates to calculate the Moon's position in both:

* **Equatorial coordinates** — Right Ascension and Declination
* **Horizontal coordinates** — Altitude and Azimuth

It also determines whether the Moon is currently **above or below the local horizon**.

---

## Objectives

The project was developed to:

* Calculate the Moon's apparent position for a given time.
* Work with observer latitude, longitude, and elevation.
* Understand and apply astronomical coordinate systems.
* Convert celestial coordinates into observer-based horizontal coordinates.
* Determine the Moon's visibility relative to the horizon.
* Gain practical experience with the **Skyfield astronomy library**.

---

## Astronomical Concepts

### Equatorial Coordinates

The Moon's celestial position is represented using:

| Parameter            | Description                                              |
| -------------------- | -------------------------------------------------------- |
| Right Ascension (RA) | Angular position along the celestial equator             |
| Declination (Dec)    | Angular distance north or south of the celestial equator |

### Horizontal Coordinates

The position is also expressed relative to the observer:

| Parameter | Description                               |
| --------- | ----------------------------------------- |
| Altitude  | Angular height above or below the horizon |
| Azimuth   | Direction of the object along the horizon |

For example:

Azimuth
0°   → North
90°  → East
180° → South
270° → West

An altitude greater than `0°` indicates that the Moon is geometrically above the horizon.

---

## System Workflow

                 Observer Input
                       │
                       ▼
          ┌─────────────────────────┐
          │ Latitude / Longitude    │
          │ Elevation / Date / Time │
          └────────────┬────────────┘
                       │
                       ▼
             Skyfield Ephemeris
                       │
                       ▼
                Earth + Moon
                       │
                       ▼
             Apparent Position
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
       RA / Declination      Altitude / Azimuth
             │                   │
             └─────────┬─────────┘
                       ▼
              Horizon Visibility
                       │
                       ▼
                  Final Output

---

## Tech Stack

| Technology                 | Purpose                                |
| -------------------------- | -------------------------------------- |
| Python                     | Core implementation                    |
| Skyfield                   | Astronomical calculations              |
| NumPy                      | Numerical operations                   |
| Jupyter Notebook / VS Code | Development environment                |
| Git & GitHub               | Version control and project management |

---

## Inputs

The calculator accepts:

* Observer latitude
* Observer longitude
* Observer elevation
* Observation date
* Observation time

Example:
Latitude  : 13.0827°
Longitude : 80.2707°
Elevation : 6 m
Date      : 2026-08-18
Time      : 20:00:00

---

## Outputs

The program calculates:

Right Ascension
Declination
Altitude
Azimuth
Distance from Earth
Horizon visibility

Example output format:

========================================
         MOON POSITION CALCULATOR
========================================

Observer
Latitude  : 13.0827°
Longitude : 80.2707°
Elevation : 6 m

Observation Time
2026-08-18 20:00:00

----------------------------------------
Moon Position
----------------------------------------

Right Ascension : XXh XXm XXs
Declination     : XX° XX' XX"
Altitude        : XX.XX°
Azimuth         : XXX.XX°
Distance        : XXXXX km

Visibility      : Above Horizon
========================================

The numerical values depend on the observation time and observer location.

---

## Core Implementation

The project uses Skyfield to obtain the Moon's apparent position relative to an observer.

earth = planets["earth"]
moon = planets["moon"]

observer = earth + location

astrometric = observer.at(t).observe(moon)
apparent = astrometric.apparent()

The equatorial coordinates are obtained using:

ra, dec, distance = apparent.radec()

The observer-based horizontal coordinates are obtained using:

alt, az, distance = apparent.altaz()


The horizon visibility is then determined from the altitude:

if alt.degrees > 0:
    print("Moon is above the horizon")
else:
    print("Moon is below the horizon")

---

## Project Structure

Mini_Project_04_Moon_Position/
│
├── README.md 
├── moon_position.py

---

## Installation

### 1. Clone the repository

git clone <your-repository-url>
cd Mini_Project_04_Moon_Position

### 2. Create a virtual environment

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

---

## Running the Project

Run:

python moon_position.py

Provide the required observer location and observation time when prompted.

The program will calculate and display the Moon's current astronomical position.

---

## Dependencies

Example `requirements.txt`:

skyfield
numpy

---

## Applications

The calculations developed in this project can be used in:

* Astronomy applications
* Stargazing applications
* Telescope pointing systems
* Educational astronomy software
* Celestial navigation
* Astronomical visualization
* Observation planning systems

---

## Learning Outcomes

Through this project, the following concepts were applied in a practical implementation:

* Astronomical time
* Observer location
* Celestial coordinate systems
* Right Ascension
* Declination
* Altitude
* Azimuth
* Apparent position
* Ephemeris-based astronomy
* Skyfield
* Python-based astronomical computation

---

## Part of a Larger Project

This project is one component of my **AI-Powered Stargazing Assistant**.

The larger system aims to combine:

Astronomical Calculations
          +
Weather Data
          +
Celestial Visibility
          +
Machine Learning
          ↓
Personalized Stargazing Recommendations

The Moon Position Calculator provides the foundational astronomical-position functionality required by the larger system.

---

## Future Vision

The long-term goal is to transform these individual astronomical calculations into a complete intelligent stargazing system capable of answering:

**"What can I observe from my location right now, and what is the best thing to observe?"**

**From astronomical calculations to intelligent stargazing recommendations.**
