# Write a program to convert the 24 hour format time string into 12 hour format time

def to_12Hour(time):                            # Function that takes a 24 hour format string and converts it into 12 hour format time
    hour = int(time[:2])                # variable to take the first 2 parts of a string as an hours
    minute = int(time[2:])              # variable to take the second 2 parts of a string as minutes
    ra = 12         # variable to count how many hours after the 12 is given
    change = 0      # variable for converting the 13 to 1 and so on..
    if hour >= 12 and hour <= 24:               
        while hour >= 12:                           # Loop to conert the hours into PM 
            if hour == ra:
                return f"{change}:{minute} PM"
                break
            ra += 1
            change += 1
    if hour < 12:                       # Loop to convert the hours into AM
        if hour == 00:
            hour = 12
        for i in range(0,13):
            if hour == i:
                return f"{hour}:{minute} AM"


def main():             # Main function that runs the code
    ti = "0060"
    result = to_12Hour(ti)      # Function call for the converter
    print(result)

main()