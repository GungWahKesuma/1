iguana = 2169
days = 276
daycount = 92
death = (11.1/100)
temp = iguana
day = 0


while(days>day):
    temp = temp - round(temp*death)
    temp = temp+temp
    day = day+daycount
    print("total iguana (day %d) is = %d" % (day, temp))
