import pandas as pd

#------------------- .csv Import ---------- #
imported_data= pd.read_csv("data/raw/customers.csv")
print(imported_data.head())

#------------------- Concatination (Joining) Function ---------- #

# data2= pd.DataFrame(
#     {
#         "Employe ID" : [10,11,12,13,15]
#     }
# )
# # data3=pd.concat([data,data2], axis=1)
# # print(data3.head())
# # print(data.head())
# # print(imported_data[imported_data["Age(Years)"] <= 19])
# # print(imported_data["CustomerId"])
# print(imported_data.loc[:, ["CustomerId", "Surname"]])
# print(imported_data.iloc[0, 0])

#------------------- GroupBy Function ---------- #
# print(imported_data.groupby(["HasCrCard", "Gender"]).size())
#------------------- Date-Range Function ---------- #

# data_dates=pd.date_range(start="2026-01-01", end="2026-01-30")
# data_dates2=pd.date_range("2026-02-01", periods=5, freq="7D")
# data_dates3=pd.date_range("2026-03-01", periods=7, freq="ME")
# print(data_dates, data_dates2, data_dates3)