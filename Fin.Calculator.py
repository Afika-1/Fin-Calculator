import math


def simple_int(principal_amount, int_rate, time):
  
  """ Simple interest calculation on a principal amount.
          Key:
            principal_amount: The amount of money deposited.
            int_rate: The interest rate (as a percentage).
            time: The number of years the money is being invested for.

      Returns:    The total amount of interest earned. 
  
  """


  
  int_rate = int_rate / 100
  return principal_amount * int_rate * time

def compound_interest(principal_amount, int_rate, time):
 

  int_rate = int_rate / 100
  return principal_amount * math.pow((1 + int_rate), time)

def bond_repayment(current_value, int_rate, months):
  
  """Calculates the monthly bond repayment.
  Key:
    current_value: The present value of the house.
    int_rate: The interest rate.
    months: The number of months to repay the bond.

  Returns:
    The monthly bond repayment.
  """

  int_rate = int_rate / 1200
  monthly_interest = int_rate * current_value
  return monthly_interest / (1 - math.pow(1 + int_rate, -months))

def main():
  """The main function."""

  print("Welcome to the financial calculator!")

  while True:
    print("What would you like to calculate? (Investment/Bond)")
    choice = input()

    if choice.lower() == "investment":
      print("Please enter the following information:")
      principal_amount = float(input("Amount of money deposited: "))
      int_rate = float(input("Interest rate (as a percentage; DO NOT include the '%' sign): "))
      time = int(input("Number of years investing for: "))

      print("Would you like to calculate 'simple' or 'compound' interest?")
      interest_type = input()

      if interest_type.lower() == "simple":
        interest = simple_int(principal_amount, int_rate, time)
        print(f"The total amount of interest earned is: R{interest:.2f}")

      elif interest_type.lower() == "compound":
        interest = compound_interest(principal_amount, int_rate, time)
        print("The total amount of interest earned is: R", interest)
        print(f"The total amount is: R{principal_amount+interest:.2f}")

      else:
        print("Invalid input. Please try again.")

    elif choice.lower() == "bond":
      print("Please enter the following information:")
      current_value = float(input("Present value of the house: "))
      int_rate = float(input("Interest rate: "))
      months = int(input("Number of months to repay the bond: "))

      monthly_repayment = bond_repayment(current_value, int_rate, months)
      print(f"The monthly bond repayment is: R{monthly_repayment:.2f}")
      

    else:
      print("Invalid input. Please try again.")

    # print("Would you like to calculate something else? (y/n)")
    # answer = input()

    # if answer.lower() == "n" or "N" or "NO":
    #   break

if __name__ == "__main__":
  
  main()