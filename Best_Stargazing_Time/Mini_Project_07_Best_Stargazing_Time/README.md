# Mini Project 07: Best Stargazing Time

A Python astronomy mini-project that calculates the best time for stargazing at a given location and date by analyzing **sunrise, sunset, golden hour, and the different stages of twilight**.

This project is part of my **AI-Powered Stargazing Assistant learning journey**, where I am building astronomy and Python concepts step by step before combining them with weather data, Moon information, and machine learning.

---

## Project Objective

The goal of this project is to determine when the sky becomes sufficiently dark for astronomical observation.

The program calculates:

* ☀️ Sunrise
* 🌅 Morning Golden Hour
* 🌇 Sunset
* 🌅 Evening Golden Hour
* 🌆 Civil Twilight
* 🌃 Nautical Twilight
* 🌌 Astronomical Twilight
* 🌠 Astronomical Night
* ⭐ Best Dark-Sky Period

The main criterion used for astronomical darkness is:

**Sun altitude < -18°**

When the Sun is more than 18° below the horizon, astronomical twilight has ended and the sky can reach its darkest natural state.

---

## 🧠 Astronomy Concept

The Sun's altitude determines how dark the sky is after sunset.

Sun altitude
     ↓
   0° ───────── Sunset
     │
     │  Civil Twilight
     │
  -6° ───────── Civil Twilight ends
     │
     │  Nautical Twilight
     │
 -12° ───────── Nautical Twilight ends
     │
     │  Astronomical Twilight
     │
 -18° ───────── Astronomical Twilight ends
     ↓
🌌 Astronomical Night

### Twilight Definitions

| Period                | Approximate Sun Altitude |
| --------------------- | -----------------------: |
| Sunset                |                       0° |
| Civil Twilight        |                0° to -6° |
| Nautical Twilight     |              -6° to -12° |
| Astronomical Twilight |             -12° to -18° |
| Astronomical Night    |               Below -18° |

Therefore:

Best Dark-Sky Period = Sun altitude < -18°

---

## 📥 Inputs

The program requires:

* **Date**
* **Latitude**
* **Longitude**
* **Time zone**

Example:

Date: 25 September 2026
Location: Coimbatore, Tamil Nadu
Time zone: Asia/Kolkata

The program is designed so that the location can be changed, allowing the calculation to be used for different observing locations.

---

## Example Output

🌌 BEST STARGAZING TIME
────────────────────────────────

📅 Date: 25 September 2026
📍 Location: Coimbatore, Tamil Nadu

☀️ Sunrise
    06:02

🌅 Morning Golden Hour
    06:02 – 06:28

🌇 Sunset
    18:15

🌅 Evening Golden Hour
    17:50 – 18:15

🌆 Civil Twilight
    18:15 – 18:40

🌃 Nautical Twilight
    18:40 – 19:05

🌌 Astronomical Twilight
    19:05 – 19:35

🌠 Astronomical Night
    19:35 – 05:30

⭐ BEST DARK-SKY PERIOD
    19:35 – 05:30

*The times above are an example of the intended output format. Actual results depend on the selected date and location.*

---

## Project Workflow

Date + Location
       ↓
Calculate Solar Events
       │
       ├── Sunrise
       ├── Sunset
       ├── Golden Hour
       └── Twilight
              │
              ├── Civil
              ├── Nautical
              └── Astronomical
                       ↓
              Sun < -18°
                       ↓
             🌌 Astronomical Night
                       ↓
          ⭐ Best Dark-Sky Period

---

## Technologies Used

* **Python**
* **Skyfield**
* **NumPy**
* **Matplotlib**

### Python Concepts

This project also applies:

* Functions
* Date and time handling
* Conditional logic
* Variables and data structures
* Mathematical calculations
* Formatted output

---

## Project Structure

Best-Stargazing-Time/
│
├── README.md
│
└── best_stargazing_time.py

---

## What I Learned

Through this mini-project, I learned how to connect individual astronomy concepts into a practical application.

### Astronomy

* Solar altitude
* Sunrise and sunset
* Golden hour
* Civil twilight
* Nautical twilight
* Astronomical twilight
* Astronomical night
* Determining astronomical darkness

### Python

* Working with dates and times
* Handling geographic coordinates
* Organizing calculations into functions
* Processing astronomical results
* Creating readable scientific output

Most importantly, I learned how **Sun position can be converted into a practical recommendation for astronomical observation**.

---

## Future Improvements

This project will eventually become part of my larger **AI-Powered Stargazing Assistant**.

Possible future improvements include:

* 🌙 Moon phase and Moon illumination
* 🌙 Moonrise and Moonset
* 🌙 Moon altitude
* ☁️ Weather conditions
* 💡 Light pollution
* ⭐ Visible celestial objects
* 🪐 Planet visibility
* 🤖 Machine-learning-based observation recommendations

The long-term goal is:

Sun Conditions
       +
Moon Conditions
       +
Weather
       +
Light Pollution
       +
Celestial Objects
       ↓
🤖 AI Stargazing Assistant
       ↓
🌌 "What is the best thing to observe tonight?"

---

## 📚 Learning Journey

This project is part of my astronomy learning journey toward building an **AI-powered stargazing assistant**.

**Learn → Understand → Implement → Build → Improve**

---