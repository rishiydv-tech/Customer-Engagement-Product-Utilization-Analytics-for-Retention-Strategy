customerId = "CUST001"
Surname = "Yadav"
CreditScore = 750
Geography = ["France", "Spain", "Germany"]
Gender = ["Male", "Female"]
Age = 20
Tenure = 6
Balance = 2000
NumOfProducts = 2
HasCrCard = True
IsActiveMember = True
EstimatedSalary = 9000
Exited = False

# Check data types
print(type(customerId))
print(type(Surname))
print(type(CreditScore))
print(type(Geography))
print(type(Gender))
print(type(Age))
print(type(Tenure))
print(type(Balance))
print(type(NumOfProducts))
print(type(HasCrCard))
print(type(IsActiveMember))
print(type(EstimatedSalary))
print(type(Exited))


# Python Operators

# Addition operator
TotalAmount = EstimatedSalary + Balance
print("Total Amount:", TotalAmount)

# Assignment operator
CreditScore += 50
print("Updated Credit Score:", CreditScore)

# Comparison operator
print("Age is 20 or above:", Age >= 20)

# Logical operator
print("Products = 2 and Tenure = 6:",
      NumOfProducts == 2 and Tenure == 6)

# Membership operator
print("Gender not in Geography:",
      Gender[0] not in Geography)

# Comparison operator
print("Balance is greater than 1000:",
      Balance > 1000)