t = (0, 4, 132.42222, 10000, 12345.67)
print('day_' + str(t[0]).zfill(2) + ', ex_' + str(t[1]).zfill(2) + ' : ' +
      "{:.2f}".format(t[2]) + ' ' + "{:.2e}".format(t[3]) + ' ' +
      "{:.2e}".format(t[4]))
