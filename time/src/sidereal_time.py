

def sidereal_time(julian_day):
    t = (julian_day - 2451545.0) / 36525.0
    mean_sidereal_time = 100.46061837 + (36000.770053608 * t) + \
                         (0.000387933 * t ^ 2) - ((t ^ 3) / 38710000.0)

    return mean_sidereal_time
