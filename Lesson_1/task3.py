seconds = int(input("Enter number of seconds: "))

buf1 = seconds % 86400
seconds = seconds - buf1
days = seconds / 86400
seconds = buf1

buf2 = seconds % 3600
seconds = seconds - buf2
hours = seconds / 3600
seconds = buf2

buf3 = seconds % 60
seconds = seconds - buf3
minutes = seconds / 60
seconds = buf3

if seconds < 10:
    seconds = "0" + str(seconds)

if minutes < 10:
    minutes = '%.0f' % minutes
    minutes = "0" + str(minutes)
else:
    minutes = '%.0f' % minutes

if hours < 10:
    hours = '%.0f' % hours
    hours = "0" + str(hours)
else:
    hours = '%.0f' % hours

print(('%.0f' % days) + " Day " + hours + ":" + minutes + ":" + str(seconds))
