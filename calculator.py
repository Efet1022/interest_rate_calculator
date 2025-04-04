#Greeting the user to the program.
print("Welcome to interest rate calculator! Let me help you calculate your interest rate.")

#Asking for the inputs to calculate the interest rate.
total_amount = float(input("How much is the total amount?"))
interest_rate = float(input("How much is the monthly interest rate?"))
month = int(input("In how many months do you want to payback?"))

#Calculating the monthly payment and total interest payment.
monthly_payment = int((total_amount * (1 + interest_rate / 100)) - total_amount)
total_payment = int((monthly_payment * month))

print("Your monthly payment will be {m}.Your total interest payment will be {t}.".format(m = monthly_payment,t = total_payment))
print("Thank you for using the interest rate calculator!")