seconds = int(input("Enter number of seconds: "))

buf1 = seconds % 86400
days = int((seconds - buf1) / 86400)
seconds = buf1

buf2 = seconds % 3600
hours = int((seconds - buf2) / 3600)
seconds = buf2

buf3 = seconds % 60
minutes = int((seconds - buf3) / 60)
seconds = buf3

print("{0} Days {1:02d}:{2:02d}:{3:02d}".format(days, hours, minutes, seconds))
