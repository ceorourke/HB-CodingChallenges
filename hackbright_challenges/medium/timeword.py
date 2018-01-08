"""Turn a string of 24h time into words.

You can trust that you'll be given a valid string (it will
always have a two-digit hour 00-23, and a two-digit minute
00-59). Hours 0-11 are am, and hours 12-23 are pm.

Handle noon and midnight specially:

    >>> time_word("00:00")
    'midnight'

    >>> time_word("12:00")
    'noon'

Otherwise, convert times to text:

    >>> time_word("01:00")
    "one o'clock am"

    >>> time_word("06:01")
    'six oh one am'

    >>> time_word("06:10")
    'six ten am'

    >>> time_word("06:18")
    'six eighteen am'

    >>> time_word("06:30")
    'six thirty am'

    >>> time_word("10:34")
    'ten thirty four am'

Don't forget to handle early morning properly:

    >>> time_word("00:12")
    'twelve twelve am'

For times after noon, add 'pm'

    >>> time_word("12:09")
    'twelve oh nine pm'

    >>> time_word("23:23")
    'eleven twenty three pm'

By Joel Burton <joel@joelburton.com>.
"""


def time_word(time):
    """Convert time to text."""

    times = time.split(':')
    hour_to_word = {"00": "twelve", "01": "one", "02": "two", "03": "three", "04": "four",
                    "05": "five", "06": "six", "07": "seven", "08": "eight",
                    "09": "nine", "10": "ten", "11": "eleven", "12": "twelve"}
    first_digit_in_minute = {"0": "oh", "2": "twenty", "3": "thirty", "4": "forty",
                             "5": "fifty"}
    second_digit_in_minute = {"1": "one", "2": "two", "3": "three", "4": "four",
                              "5": "five", "6": "six", "7": "seven", "8": "eight",
                              "9": "nine", "0": ""}
    teens_in_minute = {"10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen",
                       "14": "fourteen", "15": "fifteen", "16": "sixteen",
                       "17": "seventeen", "18": "eighteen", "19": "nineteen"}

    timewords = []
    if times[0] == "00" and times[1] == "00":
        timewords.append('midnight')
    elif times[0] == "12" and times[1] == "00":
        timewords.append('noon')
    else:
        hour = int(times[0])
        if hour > 12:
            hour -= 12
        if hour < 10:
            hour = "0" + str(hour)
        else:
            hour = str(hour)
        timewords.append(hour_to_word[hour]) # add the hour

        if times[1] == "00": # i.e. Five o'clock
            timewords.append("o'clock")
        elif times[1][0] == "1": # it's a -teen
            timewords.append(teens_in_minute[times[1]])
        else:
            timewords.append(first_digit_in_minute[times[1][0]])
            timewords.append(second_digit_in_minute[times[1][1]])
        if int(times[0]) <= 11: # midnight as 12 am and noon as 12 pm.
            timewords.append("am")
        else:
            timewords.append("pm")
    # this removes the blank space if it's, for example, ['five', 'thirty', '']
    timewords2 = [timeword for timeword in timewords if timeword != ""]
    return ' '.join(timewords2)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. YOU'RE A TIME WIZARD!\n"