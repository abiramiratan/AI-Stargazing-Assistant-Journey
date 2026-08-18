# Mini Project 03: Observatory Distance Calculator

## Project Overview

The Observatory Distance Calculator is a Python application that calculates the shortest surface distance between two observatories on Earth using their geographic coordinates.

The project demonstrates how geographic locations can be represented mathematically and how distances between locations can be computed using Earth geometry and coordinate transformations. It also converts each observatory's location into a three-dimensional position vector relative to the center of the Earth.

This project is part of my AI-Powered Stargazing Assistant learning journey and serves as a foundation for future astronomy and visibility calculations.

---

## Features

* Accepts latitude and longitude for two observatories
* Calculates the central angle between locations
* Computes the Great Circle Distance
* Generates 3D observer position vectors
* Displays results in a simple and user-friendly format

---

## Concepts Covered

* Latitude and Longitude
* Earth Radius
* Cartesian Coordinates
* Observer Position Vectors
* Great Circle Distance
* Haversine Formula
* Vector Geometry

---

## Project Structure

Mini_Project_04_Observatory_Distance/

│
├── README.md
├── observatory_distance.py
├── formulas.md
├── theory.md
├── requirements.txt
│
└── screenshots/

---

## How It Works

1. Enter the latitude and longitude of the first observatory.
2. Enter the latitude and longitude of the second observatory.
3. The program converts both locations into 3D position vectors.
4. It calculates the central angle between the locations.
5. The shortest distance along Earth's surface is determined.
6. The results are displayed, including the observer vectors and distance in kilometers.

---

## Sample Output

===== RESULTS =====

Central Angle : 74.50°

Distance      : 8287.00 km

Observer Vector A
(1040, 6075, 1441)

Observer Vector B
(3964, 0, 4989)

---

## Applications

* Observatory Planning
* Telescope Network Analysis
* Astronomy Research
* Satellite Ground Station Planning
* Geographic Distance Calculations
* Earth Observation Projects

---

## Learning Outcomes

Through this project, I learned how to:

* Work with geographic coordinates
* Represent Earth locations in 3D space
* Calculate distances on a spherical surface
* Apply vector-based thinking to real-world problems
* Connect Earth geometry concepts with astronomy applications

---

## Future Improvements

* Interactive graphical user interface (GUI)
* Observatory database integration
* World map visualization
* 3D Earth visualization
* Multiple observatory comparisons
* Integration with astronomy libraries such as Skyfield

---

## About the Journey

This project is part of my **AI-Powered Stargazing Assistant** project series, where I am learning the mathematics, astronomy, and programming concepts required to build intelligent astronomy applications.

Each mini project focuses on a specific concept and contributes to the final goal of developing a complete AI-assisted stargazing platform.

---
