import pandas as pd

data = pd.DataFrame(
    {
        'CustomerId': [1001, 1002, 1003, 1004, 1005],
        'Surname': ['Yadav', 'Sharma', 'Jaat', 'Lawrence', 'Goyal'],
        'Balance(INR)': [1000, 2000, 5000, 7000, 9000],
        'NumOfProducts': [1, 2, 6, 8, 10],
        'HasCrCard': ['Yes', 'No', 'Yes', 'Yes', 'Yes'],
        'IsActiveMember': ['True', 'False', 'False', 'False', 'True'],
        'CreditScore': [11.10, 12.6, 33, 65.7, 22],
        'Geography': ['France', 'Spain', 'Germany', 'Germany', 'Spain'],
        'Gender': ['Male', 'Female', 'Female', 'Male', 'Female'],
        'Age(Years)': [19, 18, 20, 22, 35],
        'Tenure(Months)': [2, 4, 5, 6, 10],
        'EstimatedSalary': [15000, 18000, 20000, 5000, 10000],
        'Exited': ['No', 'No', 'Yes', 'Yes', 'Yes']
    }
)


# data.to_csv("data/raw/customers.csv", index=False)  //  created a csv file of dataset