#defining the function calculate_pay and passing an argument of hours_worked and pay_per_hour
#return statement that multiplies the two arguments together
def calculate_pay(hours_worked, pay_per_hour):
  total_pay = hours_worked * pay_per_hour
  return total_pay
# Worked 40 hours at $20 an hour
print(calculate_pay(40,20))
# Worked 50 hours at $20 an hour
print(calculate_pay(50,20))
# Worked 40 hours at $12 an hour
print(calculate_pay(40,12))
