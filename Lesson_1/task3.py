seconds = int(input("Enter number of seconds: "))

excessiveSecondsInDays = seconds % 86400
days = int((seconds - excessiveSecondsInDays) / 86400)
seconds = excessiveSecondsInDays

excessiveSecondsInHours = seconds % 3600
hours = int((seconds - excessiveSecondsInHours) / 3600)
seconds = excessiveSecondsInHours

excessiveSecondsInMinutes = seconds % 60
minutes = int((seconds - excessiveSecondsInMinutes) / 60)
seconds = excessiveSecondsInMinutes

print("{0} Days {1:02d}:{2:02d}:{3:02d}".format(days, hours, minutes, seconds))
