#defining the function calculate_pay and passing an argument of hours_worked and pay_per_hour.
#return statement that multiplies the two arguments together.
#if statement calculates overtime
def calculate_pay(hours_worked, pay_per_hour):
  if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_pay = 40 * pay_per_hour
    overtime_pay = overtime_hours * pay_per_hour * 2
    return overtime_pay, regular_pay
  else: 
    total_pay = hours_worked * pay_per_hour
    return total_pay
<<<<<<< HEAD
print("Here is your pay!")    
print(calculate_pay(70, 20))
=======
    
print(calculate_pay(30, 30))
print(calculate_pay(60, 20))
>>>>>>> 5d9aae72bfd540dd6b6eb96b42129eb02d10bdfa

