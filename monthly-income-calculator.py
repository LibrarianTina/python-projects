#defining the function calculate_pay and passing an argument of hours_worked and pay_per_hour.
#return statement that multiplies the two arguments together.
#if statement calculates overtime
def calculate_pay(hours_worked, pay_per_hour):
  if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_pay = 40 * pay_per_hour
    overtime_pay = overtime_hours * pay_per_hour * 2
    return overtime_pay + regular_pay
  else: 
    total_pay = hours_worked * pay_per_hour
    return total_pay
#defining the function calculate_monthly_pay and writing a variable for each week and assigning it to the result 
#of the calculate_pay() function.
def calculate_monthly_pay(wk_1_hours, wk_2_hours, wk_3_hours, wk_4_hours, pay_per_hour):
  week1_pay = calculate_pay(wk_1_hours, pay_per_hour)
  week2_pay = calculate_pay(wk_2_hours, pay_per_hour)
  week3_pay = calculate_pay(wk_3_hours, pay_per_hour)
  week4_pay = calculate_pay(wk_4_hours, pay_per_hour)
  return week1_pay, week2_pay, week3_pay, week4_pay
print(calculate_monthly_pay(40,50,35,40,50))

