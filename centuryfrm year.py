


def centuryFromYear(year):
    yearint= int(year)
    if yearint in range(1,100):
        return 1
    else:
        yy = year[2:]
        yy = int(yy)
        cen = ((yearint-yy)/100)+1
        return int(cen)

year = input()
centuryFromYear(year)

