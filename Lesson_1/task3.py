seconds = int(input("Enter number of seconds: "))
minutes = 0
hours = 0
days = 0

while seconds > 60:
    seconds -= 60
    minutes += 1
if seconds < 10:
    seconds = "0" + str(seconds)

while minutes > 60:
    minutes -= 60
    hours += 1
if minutes < 10:
    minutes = "0" + str(minutes)

while hours > 24:
    hours -= 24
    days += 1
if hours < 10:
    hours = "0" + str(hours)

print(str(days) + " Day " + str(hours) + ":" + str(minutes) + ":" + str(seconds))
