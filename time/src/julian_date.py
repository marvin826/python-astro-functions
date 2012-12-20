from time_exceptions import InputError

# define some constants (need to put these in a database somewhere)
days_per_year = 365.25
year_offset = 4716.0
ave_month_days = 30.6001
day_offset = 1524.5


def julian_date(o_cal_y, o_cal_m, o_cal_d, \
                o_cal_h=0, o_cal_min=0, o_cal_s=0.0):

    # preserve the original input date
    cal_y = o_cal_y
    cal_m = o_cal_m
    cal_d = o_cal_d
    if(o_cal_m == 1 or o_cal_m == 2):
        cal_m = o_cal_m + 12
        cal_y = o_cal_y - 1
        cal_d = o_cal_d

    # divide the year by 100
    cal_y_divh = int(float(cal_y / 100.0))

    # calculate the offset. If the date we're working with is
    # on or before October 4, 1582, the offset is zero.
    offset = 0
    if(o_cal_y >= 1582):
        offset = 2 - cal_y_divh + int(cal_y_divh / 4.0)

    if(o_cal_y == 1582):
        if(o_cal_m <= 10 and o_cal_d <= 4):
            offset = 0

        # check for invalid dates. The dates of Oct 5-14 1582
        # don't exist due to the change from the Julian to the
        # Gregorian calendars
        if(o_cal_m == 10 and (o_cal_d >= 5 and o_cal_d <= 14)):
            date_str = str(o_cal_y) + "/" + str(o_cal_m) + "/" + str(o_cal_d)
            raise InputError("Invalid date:" + date_str)

    julian_days = int(days_per_year * (float(cal_y) + year_offset)) + \
                  int(ave_month_days * (cal_m + 1)) + \
                  cal_d + offset - day_offset

    seconds = o_cal_s + (o_cal_h * 3600.0) + (o_cal_min * 60.0)
    fraction = (seconds / 86400.0)

    return julian_days + fraction
