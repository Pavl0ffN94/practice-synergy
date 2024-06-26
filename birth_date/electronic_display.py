def display_date(day, month, year):
    num_to_star = {
        '0': [" *** ", "*   *", "*   *", "*   *", " *** "],
        '1': ["  *  ", " **  ", "  *  ", "  *  ", " *** "],
        '2': [" *** ", "*   *", "  ** ", " *   ", "*****"],
        '3': [" *** ", "*   *", "  ** ", "*   *", " *** "],
        '4': ["*  * ", "*  * ", "*****", "   * ", "   * "],
        '5': ["*****", "*    ", "**** ", "    *", "**** "],
        '6': [" *** ", "*    ", "**** ", "*   *", " *** "],
        '7': ["*****", "    *", "   * ", "  *  ", " *   "],
        '8': [" *** ", "*   *", " *** ", "*   *", " *** "],
        '9': [" *** ", "*   *", " ****", "    *", " *** "]
    }

    date_str = f"{day:02d}{month:02d}{year:4d}"

    for row in range(5):
        line = " ".join(num_to_star[digit][row] for digit in date_str)
        print(line)