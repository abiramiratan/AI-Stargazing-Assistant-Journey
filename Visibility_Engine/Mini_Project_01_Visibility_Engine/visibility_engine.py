import math

def calculate_hour_angle(lst_hours, ra_hours):
    ha_hours = lst_hours - ra_hours

    if ha_hours < 0:
        ha_hours += 24
    #converting hrs -> degree    
    return ha_hours * 15

def calculate_altitude(lat_deg, dec_deg, ha_deg):
    lat = math.radians(lat_deg)
    dec = math.radians(dec_deg)
    ha = math.radians(ha_deg)

    sin_alt = (math.sin(lat) * math.sin(dec) + 
                math.cos(lat) * math.cos(dec) * math.cos(ha))
    
    alt = math.degrees(math.asin(sin_alt))

    return alt

def is_visible(alt_deg):
    return alt_deg > 0

def main():
    print('=' * 40)
    print("AI Stargazing Assistant")
    print("Mini Project 01 - Visibility Engine")
    print('=' * 40)

    lat = float(input("Observer Latitude (deg): "))
    ra = float(input("Object Right Ascension (hr): "))
    dec = float(input("Object Declination (deg): "))
    lst = float(input("Local Sidereal Time (hr): "))

    ha = calculate_hour_angle(lst, ra)

    alt = calculate_altitude(lat, dec, ha)

    print("\nResults")
    print('-' * 20)
    print(f"Hour Angle: {ha:.2f}°")
    print(f"Altitude: {alt:.2f}°")

    if is_visible(alt):
        print("Status: VISIBLE")
    else:
        print("Status: NOT VISIBLE")

if __name__ == "__main__":
    main()