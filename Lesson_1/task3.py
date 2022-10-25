seconds = int(input("Enter number of seconds: "))

buf1 = seconds % 86400
seconds = seconds - buf1
days = int(seconds / 86400)
seconds = buf1

buf2 = seconds % 3600
seconds = seconds - buf2
hours = int(seconds / 3600)
seconds = buf2

buf3 = seconds % 60
seconds = seconds - buf3
minutes = int(seconds / 60)
seconds = buf3

print("{0} Days {1:02d}:{2:02d}:{3:02d}".format(days, hours, minutes, seconds))
