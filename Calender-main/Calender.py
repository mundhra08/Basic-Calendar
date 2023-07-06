d={1:"Mon", 2:"Tue", 3:"Wed",4:"Thurs",5:"Fri",6:"Sat",7:"Sun",0:"Sun"}
def L_Y():
  Leap_Year={"Jan":5,"Feb":1,"Mar":2,"Apr":5,"May":7,"June":3,"July":5,"Aug":1,"Sept":4,"Oct":6,"Nov":2,"Dec":4}

  Day=int(input("Enter a day."))
  Month=input("Enter a month:")
  year=input("Enter a year:")

  century=int(year[0:2])
  year_main=int(year[2:])
  a=year_main//4

  F1=(Day+Leap_Year[Month]+year_main+a)%7
  F2=(Day+Leap_Year[Month]+year_main+a)%7+1
  F3=(Day+Leap_Year[Month]+year_main+a)%7+3
  F4=(Day+Leap_Year[Month]+year_main+a)%7+5
  if century==12 or century==16 or century==20 or century==24:
    print(d[F1])
  elif century==11 or century==15 or century==19 or century==23:
    print(d[F2])
  elif century==10 or century==14 or century==18 or century==22:
    print(d[F3])
  elif century==9 or century==13 or century==17 or century==21:
    print(d[F4])

def NL_Y():
  Non_Leap_Year={"Jan":6,"Feb":2,"Mar":2,"Apr":5,"May":7,"June":3,"July":5,"Aug":1,"Sept":4,"Oct":6,"Nov":2,"Dec":4}

  Day=int(input("Enter a day."))
  Month=input("Enter a month:")
  year=input("Enter a year:")

  century=int(year[0:2])
  year_main=int(year[2:])
  a=year_main//4

  F1=(Day+Non_Leap_Year[Month]+year_main+a)%7
  F2=(Day+Non_Leap_Year[Month]+year_main+a)%7+1
  F3=(Day+Non_Leap_Year[Month]+year_main+a)%7+3
  F4=(Day+Non_Leap_Year[Month]+year_main+a)%7+5
  if century==12 or century==16 or century==20 or century==24:
    print(d[F1])
  elif century==11 or century==15 or century==19 or century==23:
    print(d[F2])
  elif century==10 or century==14 or century==18 or century==22:
    print(d[F3])
  elif century==9 or century==13 or century==17 or century==21:
    print(d[F4])


y = int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (y % 400 == 0) and (y % 100 == 0):
    print("{0} is a leap year".format(y))
    L_Y()


# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (y % 4 ==0) and (y % 100 != 0) :
    print("{0} is a leap year".format(y))
    L_Y()

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(y))
    NL_Y()
