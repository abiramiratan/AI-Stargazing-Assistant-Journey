from visibility_engine import (
    calculate_hour_angle,
    calculate_altitude,
    is_visible
)


def run_test(name, latitude, ra, dec, lst):
    """
    Run visibility calculation for a single object.
    Returns True if the object is visible.
    """

    ha = calculate_hour_angle(lst, ra)

    altitude = calculate_altitude(
        latitude,
        dec,
        ha
    )

    status = "VISIBLE" if is_visible(altitude) else "NOT VISIBLE"

    print("=" * 50)
    print(name)
    print("=" * 50)
    print(f"RA         : {ra} h")
    print(f"Dec        : {dec}°")
    print(f"LST        : {lst} h")
    print(f"Hour Angle : {ha:.2f}°")
    print(f"Altitude   : {altitude:.2f}°")
    print(f"Status     : {status}")
    print()

    return is_visible(altitude)


def main():

    print("=" * 50)
    print("MINI PROJECT 01 - VISIBILITY ENGINE")
    print("=" * 50)

    latitude = 9.93      # Madurai
    lst = 12.0           # Example Local Sidereal Time

    print("\nObserver Information")
    print("-" * 50)
    print(f"Latitude : {latitude}°")
    print(f"LST      : {lst} h")

    objects = [
        ("Object A", 8, 20),
        ("Object B", 15, -10),
        ("Object C", 12, 45),
        ("Object D", 2, 60),
        ("Object E", 20, -40)
    ]

    visible_objects = []

    print("\nVisibility Results\n")

    for name, ra, dec in objects:

        visible = run_test(
            name,
            latitude,
            ra,
            dec,
            lst
        )

        if visible:
            visible_objects.append(name)

    print("=" * 50)
    print("SUMMARY")
    print("=" * 50)

    if visible_objects:
        print("Visible Objects Tonight:\n")

        for obj in visible_objects:
            print(f"✓ {obj}")

        print(f"\nTotal Visible Objects: {len(visible_objects)}")

    else:
        print("No objects are visible.")


if __name__ == "__main__":
    main()
