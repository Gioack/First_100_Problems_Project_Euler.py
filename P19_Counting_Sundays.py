def get_months_lenghts_based_on_year(year):
    lenghts_months_in_normal_year = [
        31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    lenghts_months_in_leap_year = [
        31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 != 0:
        lenghts_months = lenghts_months_in_normal_year
    else:
        lenghts_months = lenghts_months_in_leap_year
    return lenghts_months


def counting_sundays():
    starting_day = 2  # because it was tuesday
    year = 1900
    count_sundays = 0
    while year < 2000:
        year += 1
        lenghts_months = get_months_lenghts_based_on_year(year)
        for lenght_month in lenghts_months:
            starting_day = (starting_day + lenght_month) % 7
            if starting_day == 0:
                count_sundays += 1
    return count_sundays


print(counting_sundays())
