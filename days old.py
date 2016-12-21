#================
#<<Days Old>>
#================
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 

# Assume that the birthday and current date are correct dates (and no 
# time travel). 


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
    leap=(int)(year2-year1) / 4
    if (month1>2) or (day1==29 and month1==2) :
      if(year1%4==0):
        if(year1%100==0 and year1%400!=0):
          leap=0
        else:
          leap+=1
    if (month2>2) or (day2==29 and month2==2) :
      if(year2%4==0):
        if(year2%100==0 and year2%400!=0):
          leap=0
        else:
          leap+=1
    m=[31,28,31,30,31,30,31,31,30,31,30,31]
    tot = ((year2-year1)*365) + (sum(m[0:month2-1]) - sum(m[0:month1-1])) + (day2-day1) + int(leap)
    return tot



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
            print "Test case success!”

test()

# Test Cases

#>>>Test case success!
#>>>Test case success!
#>>>Test case success!
#>>>Test case success!
#>>>Test case success!