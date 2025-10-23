def to_12Hour(time):
    hour = int(time[:2])
    minute = int(time[2:])
    ra = 12
    change = 0
    if hour >= 12 and hour <= 24:
        while hour >= 12:
            if hour == ra:
                return f"{change}:{minute} PM"
                break
            ra += 1
            change += 1
    if hour < 12:
        if hour == 00:
            hour = 12
        for i in range(0,13):
            if hour == i:
                return f"{hour}:{minute} AM"



ti = "0060"
result = to_12Hour(ti)
print(result)