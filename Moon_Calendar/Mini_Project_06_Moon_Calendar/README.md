# Mini Project 06: Moon Calendar

A Python-based astronomy mini-project that generates a **Moon Calendar** for a selected month and location. The project uses astronomical calculations to identify lunar phases and provide useful Moon visibility information.

This project is developed as part of my larger **AI-Powered Stargazing Assistant** journey, where I am combining astronomy, programming, data analysis, and machine learning to build an intelligent stargazing recommendation system.

---

## Project Objective

The objective of this project is to build a simple Moon Calendar that helps users understand the Moon's appearance and visibility throughout a month.

The calendar is designed to provide information such as:

* 🌑 New Moon
* 🌒 Waxing Crescent
* 🌓 First Quarter
* 🌔 Waxing Gibbous
* 🌕 Full Moon
* 🌖 Waning Gibbous
* 🌗 Last/Third Quarter
* 🌘 Waning Crescent
* 💡 Moon illumination
* 🌅 Moonrise
* 🌇 Moonset
* 📐 Moon altitude and azimuth

The project also serves as a foundation for connecting lunar information with **stargazing recommendations**.

---

## Astronomy Concepts Used

This project applies concepts learned while studying astronomy and Skyfield:

* Celestial coordinates
* Right Ascension (RA)
* Declination (Dec)
* Horizontal coordinates
* Altitude
* Azimuth
* Moon phases
* Lunar illumination
* Moonrise and moonset
* Observer location
* UTC and local time
* Earth–Moon geometry

---

## Technologies Used

* **Python**
* **NumPy**
* **Matplotlib**
* **Skyfield**
* **Datetime**

---

## Project Structure

05_Moon_Calendar/
│
├── README.md
├── moon_calendar.py
├── requirements.txt

---

## How It Works

The basic workflow of the project is:

User Input(Year, Month, Latitude, Longitude)
    ↓
Skyfield Astronomy Calculations
    ↓
Moon Position(Altitude, Azimuth, Moonrise, Moonset)
    ↓
Moon Phase & Illumination -> Moon Calendar -> 
    ↓
Visualization

---

## Moon Phases

The Moon appears to change shape during its approximately **29.5-day synodic cycle**.

The major phases represented in this project are:

| Phase           | Symbol | Description                                 |
| --------------- | ------ | ------------------------------------------- |
| New Moon        | 🌑     | Moon is approximately between Earth and Sun |
| Waxing Crescent | 🌒     | Illuminated portion is increasing           |
| First Quarter   | 🌓     | Approximately half illuminated              |
| Waxing Gibbous  | 🌔     | More than half illuminated                  |
| Full Moon       | 🌕     | Almost completely illuminated               |
| Waning Gibbous  | 🌖     | Illuminated portion is decreasing           |
| Last Quarter    | 🌗     | Approximately half illuminated              |
| Waning Crescent | 🌘     | Small illuminated portion remains           |

---

## Important Calculations

### Moon Altitude

Altitude represents how high the Moon is above the observer's horizon.

Altitude = 0°
    → Moon is on the horizon

Altitude = 90°
    → Moon is directly overhead

### Moon Azimuth

Azimuth describes the direction of the Moon along the horizon.

Using the common astronomical convention:

0°   → North
90°  → East
180° → South
270° → West

### Moon Illumination

Moon illumination represents the fraction of the Moon's visible disk that is illuminated by sunlight.

Conceptually:

Illumination = Illuminated Area / Visible Lunar Disk Area

and can be expressed as a percentage:

Illumination (%) = Illumination × 100

---

## Skyfield

The project uses **Skyfield** to perform astronomical calculations rather than manually implementing orbital mechanics.

Skyfield allows the program to determine the Moon's position for a given:

Date + Time + Observer Location

and obtain useful observational quantities such as:

Altitude
Azimuth
Moonrise
Moonset

---

## Example Output

A typical calendar will provide information similar to:

          🌙 MOON CALENDAR
          September 2026

Sun   Mon   Tue   Wed   Thu   Fri   Sat
             1     2     3     4     5
             🌒    🌒    🌒    🌓

6     7     8     9     10    11    12
🌔    🌔    🌔    🌔    🌔    🌕    🌕

13    14    15    16    17    18    19
🌖    🌖    🌖    🌗    🌘    🌘    🌘

The final version will additionally display Moon visibility information such as illumination, moonrise, and moonset.

---

## Connection to AI Stargazing Assistant

The Moon Calendar is not an isolated project. It is one building block of the larger **AI-Powered Stargazing Assistant**.

The eventual system will combine:

Astronomy + Weather + Moon Conditions + Celestial Object Visibility + Machine Learning
    ↓
Intelligent Stargazing Recommendation

For example:

New Moon + Clear Weather + Low Light Pollution
    ↓
Excellent conditions
    ↓
Recommend Deep-Sky Objects

Whereas:

Full Moon + High Moon Illumination
    ↓
Bright Night Sky
    ↓
Avoid faint Deep-Sky Objects
    ↓
Recommend brighter targets

---

## What I Learned

Through this project, I practiced:

* Working with astronomical time
* Using Skyfield for real astronomical calculations
* Understanding lunar phases
* Working with observer coordinates
* Calculating Moon altitude and azimuth
* Working with Moonrise and moonset
* Converting astronomical calculations into a user-friendly visualization
* Structuring an astronomy project for GitHub

---

## Part of My Learning Journey

This project is part of my ongoing journey to build an **AI-Powered Stargazing Assistant** by combining:

**Astronomy + Python + Data Analysis + Machine Learning**

The project is being developed step by step, with each mini-project focusing on a specific component required for the final system.

---

## ⭐ Future Goal

> **Build an intelligent AI-powered assistant that can analyze astronomical conditions, weather, and celestial-object visibility to recommend what, when, and where to observe in the night sky.**

---