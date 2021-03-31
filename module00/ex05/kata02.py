t = (3, 30, 2019, 9, 25)
hour = t[0]
minutes = t[1]
year = t[2]
month = t[3]
day = t[4]
print(str(month).zfill(2) + '/' + str(day).zfill(2) + '/' + str(year).zfill(4)
      + ' ' + str(hour).zfill(2) + ':' + str(minutes).zfill(2))
