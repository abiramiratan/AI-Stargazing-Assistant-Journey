# Formulas - Observer_Distance

## Earth Radius

The average radius of the Earth used in this project:

```text
R = 6371 km
```

---

## Observer Position Vector

A geographic location can be converted into a 3D Cartesian coordinate using:

```text
x = R × cos(latitude) × cos(longitude)

y = R × cos(latitude) × sin(longitude)

z = R × sin(latitude)
```

Where:

* R = Earth's radius
* Latitude and Longitude are measured in radians

---

## Latitude and Longitude Differences

```text
Δlat = lat₂ − lat₁

Δlon = lon₂ − lon₁
```

These values represent the angular separation between two locations.

---

## Haversine Formula

```text
a = sin²(Δlat / 2)
    +
    cos(lat₁) × cos(lat₂)
    ×
    sin²(Δlon / 2)
```

---

## Central Angle

```text
c = 2 × atan2(√a, √(1 − a))
```

Where:

* c = Central angle between the two observatories (in radians)

---

## Great Circle Distance

```text
Distance = R × c
```

Where:

* R = Earth's radius
* c = Central angle

The result gives the shortest distance along Earth's surface between the two observatories.

---

## Output Quantities

The program calculates:

```text
1. Observer Vector A

2. Observer Vector B

3. Central Angle

4. Great Circle Distance
```

These values describe the geometric relationship between the two observatories on Earth.
