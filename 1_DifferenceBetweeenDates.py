#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates.
#

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days_in_months=[31,28,31,30,31,30,31,31,30,31,30,31]

    years_inbetween = year2-year1 - 1
    print years_inbetween

    months = 12 - month1 + (years_inbetween * 12) + month2 - 1
#    print(month1,months,month2)

    days = 0

    year = year1
    for i in range(month1+1,month1+months+1):
        m = i % 12
    #    print("m: ",m)
        if m == 2:
            if  (year % 100)%2==0 and (year % 400)%2 == 0:
                days += 29
    #            print('added days: ',29)
            else:
                days += days_in_months[m-1]
    #            print('added days: ',days_in_months[m-1])
        else:
            days+=days_in_months[m-1]
    #        print('added days: ',days_in_months[m-1])

        if m==0:
            year+=1

    #print days
    days=days + (days_in_months[month1-1] - day1) + day2

    print days
    return days


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"


test()
