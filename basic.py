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

# IsActiveMember = int(input("Enter the no. of active members:"))
# Balance= int(input("ENter the balance for the member:"))
# if IsActiveMember == 1 :e!")
#     if Balance >= 1000 :
#     print("Success: The Member is activ
#         print("Success : The Balance is greater than 1000!")
#     else :
#         print("Failure : The Balance is lesser than 1000!")
# else :
#     print("Failure: The Member is Inactive!")

# ================= Python Functions logic =================

# def engagement_label(balance, is_active):
#     if is_active == False:
#         return "Inactive"
#     elif balance >= 1000:
#         return "High Engagement"
#     elif balance >= 500:
#         return "Medium Engagement"
#     else:
#         return "Low Engagement"


# print(engagement_label(1500, True))
# print(engagement_label(700, True))
# print(engagement_label(200, True))
# print(engagement_label(1500, False))

# ================= Python Loops =================

# customers = [
#     ("Rishi", 1000, True),
#     ("Rahul", 500, False),
#     ("Priya", 1000, True)
# ]

# print("\nName\tBalance\tActive/Inactive\tEngagement")

# for name, balance, is_active in customers:
#     label = engagement_label(balance, is_active)
#     print(f"{name}\t{balance}\t{is_active}\t\t{label}")


# ================= Python Tuple & Dicionary(Dict inside a Bracket (not considered as inside Tuple because no ',')) =================


customer_records = (
    {
        "CUST001": {
            "Name": "Rishi",
            "Balance": 1000
        },
        "CUST002": {
            "Name": "Rahul",
            "Balance": 5000
        },
        "CUST003": {
            "Name": "Priya",
            "Balance": 500
        }
    }
)

print(customer_records["CUST001"]["Balance"])


#================ Python Tuple & Dicionary(Dict inside a Tuple) =================
records = (
    {
        "CustomersDetails": {
            "CUST001": {
                "Name": "Rishi",
                "Balance": 1000
            },
            "CUST002": {
                "Name": "Rahul",
                "Balance": 5000
            }
        },

        "EmployeesDetails": {
            "EMP001": {
                "Name": "Aman",
                "Department": "Data Analytics",
                "Salary": 20000
            },
            "EMP002": {
                "Name": "Priya",
                "Department": "HR",
                "Salary": 25000
            }
        }
    },
)

# 1. Access customer balance
print(records[0]["CustomersDetails"]["CUST001"]["Balance"])

# 2. Add a new customer
records[0]["CustomersDetails"]["CUST003"] = {
    "Name": "Neha",
    "Balance": 3000
}

# 3. Update customer balance
records[0]["CustomersDetails"]["CUST001"]["Balance"] = 2000

# 4. Add a new employee
records[0]["EmployeesDetails"]["EMP003"] = {
    "Name": "Karan",
    "Department": "IT",
    "Salary": 30000
}

# 5. Update employee salary
records[0]["EmployeesDetails"]["EMP002"]["Salary"] = 28000

# 6. Delete a customer
del records[0]["CustomersDetails"]["CUST002"]

# 7. Display all customer IDs
print(records[0]["CustomersDetails"].keys())

# 8. Display all employee records
print(records[0]["EmployeesDetails"].items())

# 9. Count customers and employees
print(len(records[0]["CustomersDetails"]))
print(len(records[0]["EmployeesDetails"]))



