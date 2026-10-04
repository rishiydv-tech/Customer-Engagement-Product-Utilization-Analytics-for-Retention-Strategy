# ============================================================== Python DataTypes ==================================================================#
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

# # Check data types
# print(type(customerId))
# print(type(Surname))
# print(type(CreditScore))
# print(type(Geography))
# print(type(Gender))
# print(type(Age))
# print(type(Tenure))
# print(type(Balance))
# print(type(NumOfProducts))
# print(type(HasCrCard))
# print(type(IsActiveMember))
# print(type(EstimatedSalary))
# print(type(Exited))

# ============================================================== Python Operators ==================================================================#

# # Addition operator
# TotalAmount = EstimatedSalary + Balance
# print("Total Amount:", TotalAmount)

# # Assignment operator
# CreditScore += 50
# print("Updated Credit Score:", CreditScore)

# # Comparison operator
# print("Age is 20 or above:", Age >= 20)

# # Logical operator
# print("Products = 2 and Tenure = 6:",
#       NumOfProducts == 2 and Tenure == 6)

# # Membership operator
# print("Gender not in Geography:",
#       Gender[0] not in Geography)

# # Comparison operator
# print("Balance is greater than 1000:",
#       Balance > 1000)

# ============================================================== List Operations ==================================================================#

# customerIds = [f"CUST{x}" for x in input("Enter Customer IDs: ").split()]
# print("The Customer IDs are:", customerIds)
# apnd = [f"CUST{x}" for x in input("Enter the adding Customer ID/IDs: ").split()]
# customerIds.extend(apnd)
# print("The New Customer IDs are:", customerIds)


# index = int(input("Enter the Index for Insertion:"))
# custid = input("ENter the Customer Id:")
# custid= f"CUST{custid}"
# customerIds.insert(index, custid)
# print(f"The {custid} Inserted in the list!")
# print("The New CustomerIDs Are: ", customerIds)
# Loop logic needed to be performed because if you dont want to insert any customerid it throws error

# index2= int(input("Enter the Index to pop:"))
# customerIds.pop(index2)
# print(f"The {index2}'s CustomerId is Removed Successfully!")
# print(f"The new CustomerIDs are :{customerIds}")
# Loop logic needed to be performed because if you dont want to insert any customerid it throws error

# rmv= input("Enter the CustomerId to remove:")
# rmv= f"CUST{rmv}"
# customerIds.remove(rmv)
# print(f"The {rmv} is Removed Successfully!")
# print(f"The new CustomerIDs are :{customerIds}")
# customerIds.reverse()
# print(f"The Reversed order of CustomerIds is:{customerIds}")

# EmployeeId= ["A1", "B2", "C3"]
# customerIds.extend(EmployeeId)
# print(f"The Complete List of Company is:{customerIds}")
# customerIds.sort()
# print(f"The Sorted Order of the Company List: {customerIds}")
# print(f"The Count of Cust001 is: {customerIds.count("CUST001")}")
# customerIds.copy()
# customerIds.append("Error Maker")
# customerIds.clear()
# print(customerIds)

# ============================================================== String Operations ==================================================================#

# surname = "yadav Saini Rathore Sharma"
# print(surname.upper())
# print(surname.isupper())
# print(surname.capitalize())
# print(surname.find("yadav"))
# print(surname.isalnum())
# print(surname.replace("Rathore","Jaat"))
# start = surname.startswith("Saini")
# end = surname.endswith("Sharma")
# print(start)
# print(end)
# print("_" .join(surname))
# surname_list = surname.split()
# print(surname_list)
# print(surname_list.count("yadav"))
# print(surname_list.index("yadav"))

# ============================================================== Conditional Statements ==================================================================#

IsActiveMember = int(input("Enter the no. of active members:"))
Balance= int(input("ENter the balance for the member:"))
if IsActiveMember == 1 :
    print("Success: The Member is active!")
    if Balance >= 1000 :
        print("Success : The Balance is greater than 1000!")
    else :
        print("Failure : The Balance is lesser than 1000!")
else :
    print("Failure: The Member is Inactive!")
        



