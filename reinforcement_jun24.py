print("Please enter a number")
number = input()
firstpart, secondpart = number[:int(len(number)/2)], number[int(len(number)/2):]

def luck_check(number):
  
  try:
    sum1 = 0
    for i in firstpart:
      sum1 += int(i)
    
    sum2 = 0
    for i in secondpart:
      sum2 += int(i)

    if sum1 == sum2:
      print("This is a lucky number set!")
    elif sum1 != sum2:
      print("This ain't your luck. =(")
  
  except ValueError:
    print("Enter a NUMBER bruh.")


luck_check(number)