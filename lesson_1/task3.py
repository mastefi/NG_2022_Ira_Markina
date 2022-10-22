seconds = int(input('enter number of seconds: '))
day = seconds // 86400
seconds %= 86400
seconds = seconds % (24 * 3600) # we limit the number of seconds in one day
hour = seconds // 3600
seconds %= 3600
min = seconds // 60
seconds %= 60
print(day,'days',hour,'hours',min,'minutes',seconds,'seconds')
